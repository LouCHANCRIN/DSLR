import pandas as pd
import numpy as np
import math as ma
import cmath as cma

data = pd.read_csv("ressources/dataset_train.csv")
line, col = np.shape(data)

for key in data:
    print(key)

print(line, col)
Y = data["Hogwarts House"]
Y= np.reshape(Y, (line, 1))
X = [np.insert(row, 0, 1) for row in data.drop(["Hogwarts House"], axis=1).values]
test = [np.insert(row, 0, 1) for row in data.drop(["Hogwarts House"], axis=1).values]
X = np.reshape(X, (line, col))
test = np.reshape(X, (line, col))
print(X)
