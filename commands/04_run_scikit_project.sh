export MLFLOW_TRACKING_URI=http://localhost:5000
rm -rf mlflow_projects/04_scikit_project/artifacts
mkdir mlflow_projects/04_scikit_project/artifacts
mlflow run mlflow_projects/04_scikit_project/ --experiment-name=scikit_project -P intercept=false
mlflow run mlflow_projects/04_scikit_project/ --experiment-name=scikit_project -P intercept=true
(cd mlflow_projects/04_scikit_project/artifacts && tar c .) | (cd artifacts && tar xf -)