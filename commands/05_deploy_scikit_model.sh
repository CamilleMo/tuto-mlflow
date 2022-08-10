python register_a_model/register.py 
python register_a_model/deploy_uat.py
export MLFLOW_TRACKING_URI=http://localhost:5000
mlflow models serve -m "models:/LinearRegressionModel/staging" -p 1234 --no-conda