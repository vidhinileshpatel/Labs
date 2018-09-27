
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
import pandas as pd
import numpy as np

classification_map = {
    "STAR":     1,
    "GALAXY":   2,
    "QSO":      3
}

def load_data():
    data = pd.read_csv("./sky.csv")
    split_index = int(len(data) * 0.8)
    target_col = len(data.columns) - 1



    all_X = np.array([x[1:target_col] for x in data.values])
    all_Y = np.array([ classification_map[x[target_col]]  for x in data.values])
    return (
        all_X[ : split_index],
        all_Y[ : split_index],
        all_X[split_index : ],
        all_Y[split_index : ]
    )


train_X, train_Y, test_X, test_Y = load_data()

clf = RandomForestClassifier(max_depth=15, random_state=0)
clf.fit(train_X, train_Y)
pred_Y = clf.predict(test_X)

print("Random Forest:")
print("\tMean squared error:", mean_squared_error(test_Y, pred_Y))


knn = KNeighborsClassifier(n_neighbors=15)
knn.fit(train_X, train_Y)
pred_Y = knn.predict(test_X)

print("K Nearest Neighbor:")
print("\tMean squared error:", mean_squared_error(test_Y, pred_Y))

mlp = MLPClassifier(solver='adam', alpha=1e-5, hidden_layer_sizes=(5, 100, 10), random_state=1)
mlp.fit(train_X, train_Y)
pred_Y = mlp.predict(test_X)

print("Multi Layer Perceptron Neural Network:")
print("\tMean squared error:", mean_squared_error(test_Y, pred_Y))

