import azureml
from azureml.core import Workspace

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

workspace.delete(delete_dependent_resources=True)