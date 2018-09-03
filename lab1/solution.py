

import matplotlib.pyplot as plt
import numpy as np
import pandas
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import csv
import math

def load_data():
    data = None
    with open("/Users/nate/Downloads/Admission_Predict.csv") as fin:
        data = pandas.read_csv(fin, header=0)
    return data

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
    print(num_windows)

    for i in range(num_windows):
        train_X, train_Y, test_X, test_Y = prepare_data(
            data,
            independent_var_index,
            int(len(data.columns) * 0.8),
            int(len(data.columns) * 1.0)
        )

        regr = linear_model.LinearRegression()
        regr.fit(train_X, train_Y)
        pred_Y = regr.predict(test_X)

        print('Coefficients: \n', regr.coef_)
        print("Mean squared error: %.5f" % mean_squared_error(test_Y, pred_Y))
        print('r squared score: %.5f' % r2_score(test_Y, pred_Y))

        if plot:
            plt.scatter(test_X, test_Y[:,0],  color='black')
            plt.plot(test_X, admissions_y_pred[:,0], color='blue', linewidth=3)

            plt.xticks(())
            plt.yticks(())

            plt.show()


given_data = load_data()

# For each column, run a regression
for i in range(1, len(given_data.columns) - 1):
    print("Evaluating ", given_data.columns[i])
    run_regression(given_data, i)