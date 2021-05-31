import sys
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

import mlflow
import mlflow.sklearn

mlflow.set_tracking_uri("http://localhost:5000")

n_points=100

if __name__ == "__main__":
    np.random.seed(26)

    fit_intercept = True if sys.argv[1]=="true" else False

    x1 = np.random.randn(n_points)
    x2 = np.random.randn(n_points)
    x3 = np.random.randn(n_points)

    Y = 0.2 * x1 + 2 * x2 + 7 * x3 + 1.2
    Y = Y + (np.random.randn(n_points) / 1)  # adding some noise
    BigX = np.array([x1, x2, x3]).T
    BigX_df = pd.DataFrame(BigX, columns=["B1", "B2", "B3"])

    reg = LinearRegression(fit_intercept=fit_intercept).fit(BigX, Y)
    print("estimated coefficients : ", *reg.coef_)
    if reg.intercept_:
        print("estimated intercept : ", reg.intercept_)
    y_hat = reg.predict(BigX_df)
    y = pd.DataFrame(Y)
    mlflow.log_metric("training_r2", r2_score(y, y_hat))
    mlflow.log_metric("training_mse", mean_squared_error(y, y_hat))
    mlflow.sklearn.log_model(reg, "lin_reg_model")
    print(BigX_df.to_json("file.json", orient='split'))