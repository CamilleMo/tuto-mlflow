import mlflow
from mlflow.tracking import MlflowClient

mlflow.set_tracking_uri("http://localhost:5000")
client = MlflowClient()
model_name_to_deploy = "LinearRegressionModel"
client.transition_model_version_stage(
    name=model_name_to_deploy, version=1, stage="staging"
)

client.update_model_version(
    name=model_name_to_deploy,
    version=1,
    description="This is the first version of our model",
)
