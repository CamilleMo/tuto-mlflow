pipenv run python register_a_model/register.py 
pipenv run python register_a_model/deploy_uat.py
export MLFLOW_TRACKING_URI=sqlite:///mlflow.db
pipenv run mlflow models serve -m "models:/LinearRegressionModel/staging" -p 1234 --no-conda
# ou pipenv run mlflow models serve -m "models:/LinearRegressionModel/1" -p 1234 --no-conda
