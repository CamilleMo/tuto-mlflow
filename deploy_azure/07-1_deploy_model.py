import sys

from azureml.core import Workspace
from azureml.core.model import Model
from azureml.core.webservice import AciWebservice, Webservice, AksWebservice
from azureml.core.compute import AksCompute, ComputeTarget
from azureml.exceptions import ComputeTargetException

import mlflow.azureml

from xx_secrets import subscription_id

workspace_name = "ml-deployment-platform"
workspace_location = "West Europe"
resource_group = "mlflow-tuto-rg"

workspace = Workspace.create(
    name=workspace_name,
    location=workspace_location,
    resource_group=resource_group,
    subscription_id=subscription_id,
    exist_ok=True,
)

model_name = sys.argv[1]  # "LinearRegressionModel"
model_uri = f"models:/{model_name}/{sys.argv[2]}"

env = "prod" if sys.argv[3].lower() == "prod" else "uat"

service_name = f"lr-{env}"
try:
    Webservice(workspace, service_name).delete()
except:
    print("The service does not exist yet.")
# Webservice.check_for_existing_webservice(workspace=workspace, name=service_name, check_func=Webservice.delete)
service = AksWebservice if env == "prod" else AciWebservice
service_config = service.deploy_configuration(cpu_cores=1, memory_gb=1)
AksWebservice.deploy_configuration

if env == "prod":
    
    aks_name = "aks-mlflow"

    # Create the cluster
    try:  
        cpu_cluster = ComputeTarget(workspace=workspace, name=aks_name)  
        print('Found existing cluster, use it.')  
    except ComputeTargetException:
        prov_config = AksCompute.provisioning_configuration(3,"Standard_DS2_v2")
        aks_target = ComputeTarget.create(
            workspace=workspace, name=aks_name, provisioning_configuration=prov_config
        )
        aks_target.wait_for_completion(show_output=True)
        print(aks_target.provisioning_state)
        print(aks_target.provisioning_errors)

    service_config = service.deploy_configuration(
        cpu_cores=1, memory_gb=1, compute_target_name=aks_name,
    )

azure_service, azure_model = mlflow.azureml.deploy(
    model_uri=model_uri,
    service_name=service_name,
    model_name=model_name,
    workspace=workspace,
    deployment_config=service_config,
    synchronous=True,
)
