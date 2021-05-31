import mlflow

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
    mlflow.register_model(f"runs:/{best_run_id}/{model_name_in_artifacts}",
        model_name_to_deploy)
except Exception as e:
    print(e)



