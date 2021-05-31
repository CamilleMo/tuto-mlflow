import os
import random

import mlflow
import numpy as np
import matplotlib.pyplot as plt

mlflow.set_tracking_uri("http://localhost:5000")

mlflow.set_experiment("basic_experiment")
with mlflow.start_run():
    mlflow.log_param("my_parameter", 0.05)
    mlflow.log_param("my_other_parameter", "Hello MLFlow")
    mlflow.log_metric("my_metric", 42)
    for i in range(100):
        mlflow.log_metric("my_evolving_metric", i + random.randint(-1, 1))
    ####### Dummy Plot #########
    x1 = np.linspace(0.0, 5.0)
    x2 = np.linspace(0.0, 2.0)
    y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
    y2 = np.cos(2 * np.pi * x2)
    fig, (ax1, ax2) = plt.subplots(2, 1)
    fig.suptitle("A tale of 2 subplots")
    ax1.plot(x1, y1, "o-")
    ax1.set_ylabel("Damped oscillation")
    ax2.plot(x2, y2, ".-")
    ax2.set_xlabel("time (s)")
    ax2.set_ylabel("Undamped")
    ############################
    mlflow.log_figure(fig, "my_plot.svg")
    # artifacts
    result = "This is an example artifact, an output from the run that should be kept"
    os.makedirs("results", exist_ok=True)
    with open("results/result.txt", "w") as f:
        f.write(result)

    mlflow.log_artifact("results", "artifacts")