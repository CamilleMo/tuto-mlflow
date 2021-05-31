import sys
import numpy as np

import mlflow

mlflow.set_tracking_uri("http://localhost:5000")

mlflow.set_experiment("first_model")
with mlflow.start_run():
    np.random.seed(26)

    eta = float(sys.argv[1])  # 0.1
    mlflow.log_param("learning_rate", eta)
    n_iter = int(sys.argv[2])  # 100
    mlflow.log_param("number_of_epochs", n_iter)
    n_points = 100

    x1 = np.random.randn(n_points)
    x2 = np.random.randn(n_points)
    x3 = np.random.randn(n_points)

    Y = 0.2 * x1 + 2 * x2 + 7 * x3 + 1.2
    Y = Y + (np.random.randn(n_points) / 1)  # adding some noise

    FIT_INTERCEPT = True if sys.argv[3] == "true" else False
    mlflow.log_param("intercept", FIT_INTERCEPT)

    if FIT_INTERCEPT:
        BigX = np.array([np.ones(n_points), x1, x2, x3]).T
    else:
        BigX = np.array([x1, x2, x3]).T

    theta = np.random.randn(4, 1) if FIT_INTERCEPT else np.random.randn(3, 1)
    cost_evo = np.empty(n_iter)
    for iteration in range(n_iter):
        gradients = 2 / n_points * BigX.T.dot(BigX.dot(theta) - Y[:, np.newaxis])
        theta = theta - eta * gradients
        diff = BigX @ theta - Y[:, np.newaxis]
        cost_evo[iteration] = (diff ** 2 / n_points).sum()
        mlflow.log_metric("cost_function", cost_evo[iteration])
        if FIT_INTERCEPT:
            mlflow.log_metrics(
                {
                    "intercept": theta[0][0],
                    "B1": theta[1][0],
                    "B2": theta[2][0],
                    "B3": theta[3][0],
                },
                iteration,
            )
        else:
            mlflow.log_metrics(
                {"B1": theta[0][0], "B2": theta[1][0], "B3": theta[2][0]}, iteration
            )
