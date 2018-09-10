

import matplotlib.pyplot as plt
import numpy as np
import pandas
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import csv
import math
import requests
import io
import json

CSV_URL = "https://drive.google.com/uc?export=download&id=1-NRy3Q2AewrnZcenGmf1x48vvj2bxqeb"
JSON_URL = "https://drive.google.com/uc?export=download&id=1OevU8V0tyhF9Sfxs_DzPqz1jBdg4FZBE"

def load_data():
    train_data = None
    app_data = None
    train_data = pandas.read_csv(
        io.StringIO(requests.get(CSV_URL).text),
        header=0
    )
    app_data = json.loads(requests.get(JSON_URL).text)
    
    return (train_data, app_data)

def prepare_data(data, independent_var_index, test_lower_limit, test_upper_limit):
    y_index = len(data.columns) - 1

    all_X = [[x[independent_var_index]] for x in data.values]
    all_Y = [[ x[y_index] ] for x in data.values]

    train_X = np.array(all_X[ : test_lower_limit] + all_X[test_upper_limit : ])
    train_Y = np.array(all_Y[ : test_lower_limit] + all_Y[test_upper_limit : ])
    test_X = np.array(all_X[test_lower_limit : test_upper_limit])
    test_Y = np.array(all_Y[test_lower_limit : test_upper_limit])

    return (train_X, train_Y, test_X, test_Y)


def run_regression(data, independent_var_index, test_window_size=0.2, plot=False):
    num_windows = math.floor(1 / test_window_size)

    chosen_regression = {
        "mse": 1.0,
        "model": None,
        "independent_index": independent_var_index
    }

    for i in range(0, num_windows):
        l = int(len(data) * i * test_window_size)
        u = int(len(data) * (i+1) * test_window_size)

        train_X, train_Y, test_X, test_Y = prepare_data(
            data,
            independent_var_index,
            l,
            u
        )

        regr = linear_model.LinearRegression()
        regr.fit(train_X, train_Y)
        pred_Y = regr.predict(test_X)

        mse = mean_squared_error(test_Y, pred_Y)

        print('Coefficients: \n', regr.coef_)
        print("Mean squared error: %.5f" % mse)
        print('r squared score: %.5f' % r2_score(test_Y, pred_Y))

        if mse < chosen_regression["mse"]:
            chosen_regression["model"] = regr

        if plot:
            plt.scatter(test_X, test_Y[:,0],  color='black')
            plt.plot(test_X, pred_Y[:,0], color='blue', linewidth=3)

            plt.xticks(())
            plt.yticks(())

            plt.show()
    
    return chosen_regression


def apply_regression(regression, data):
    app_data_matrix = []
    for obj in data:
        record = []
        for header in train_data.columns:
            record.append(obj[header.strip()])
        app_data_matrix.append(record[regression["independent_index"]])

    app_df = pandas.DataFrame(app_data_matrix)
    pred_Y = regression["model"].predict(app_df.values)

    return pred_Y

train_data, app_data = load_data()

# For each column, run a regression
regression = None
for i in range(1, len(train_data.columns) - 1):
    print("Evaluating ", train_data.columns[i])
    regression = run_regression(train_data, i)


print(apply_regression(regression, app_data))


