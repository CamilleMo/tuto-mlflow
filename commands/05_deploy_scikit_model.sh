#export MLFLOW_TRACKING_URI=http://localhost:5000
pipenv run python mlflow_projects/05_register_a_model/register.py 
pipenv run python mlflow_projects/05_register_a_model/deploy_uat.py
export MLFLOW_TRACKING_URI=sqlite:///mlflow.db
pipenv run mlflow models serve -m "models:/LinearRegressionModel/staging" -p 1234 --no-conda

