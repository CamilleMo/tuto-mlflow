import azureml
from azureml.core import Workspace

import mlflow
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

#version = 1
#model_name = "LinearRegressionModel"
#model_uri = f"models:/{model_name}/{version}"

experiment_name = "scikit_project"
current_experiment=dict(mlflow.get_experiment_by_name(experiment_name))
experiment_id=current_experiment['experiment_id']


df = mlflow.search_runs([experiment_id], order_by=["metrics.training_mse ASC"])
# df.to_csv("all_runs.csv")
best_run_id = df.iloc[0, df.columns.get_loc("run_id")]
print("=" * 40)
print("Best run has an MSE of ", df.iloc[0, df.columns.get_loc("metrics.training_mse")])
print("ID: ", best_run_id)
print("=" * 40)
print("Registration of the model :")
try:
    model_name_in_artifacts = "lin_reg_model"
    model_name_to_deploy = "LinearRegressionModel"
    mlflow.azureml.mlflow_register_model(f"runs:/{best_run_id}/{model_name_in_artifacts}",model_name_to_deploy,)
except Exception as e:
    print(e)


#model_image, azure_model = mlflow.azureml.build_image(
#    model_uri=model_uri,
#    workspace=workspace,
#    model_name=model_name,
#    image_name=f"{model_name.lower()}-img",
#    description="This model will be deployed on Azure !",
#    synchronous=False,
#)

#model_image.wait_for_creation(show_output=True)
