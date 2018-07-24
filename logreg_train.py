import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("ressources/dataset_train.csv")
line, col = np.shape(data)
Y = data["Hogwarts House"]
Y= np.reshape(Y, (line, 1))
X = [np.insert(row, 0, 1) for row in data.drop(["Hogwarts House", "First Name",
    "Last Name", "Birthday", "Index", "Best Hand", "Arithmancy",
    "Care of Magical Creatures"], axis=1).values]

col -= 7
X = np.reshape(X, (line, col))

theta = [[0.0] * col]
theta = np.reshape(theta, (col, 1))

_min = [[0.0] * col]
_min = np.reshape(_min, (col, 1))

_max = [[0.0] * col]
_max = np.reshape(_max, (col, 1))

_mean = [[0.0] * col]
_mean = np.reshape(_mean, (col, 1))

def moy(X, line):
    count = 0
    _sum = 0
    for l in range(0, line):
        if (X[l] == X[l]):
            _sum += X[l]
            count += 1
    return (_sum / count)

def change_nan(X, col, line):
    a = 0
    for c in range(0, col):
        _moy = moy(X[:,c], line)
        for l in range(0, line):
            if (X[l][c] != X[l][c]):
                X[l][c] = _moy
                a = a + 1
    return (X)

def scale(X, line, col):
    for c in range(1, col):
        _min[c] = X[0][c]
        _max[c] = X[0][c]
    for c in range(1, col):
        for l in range(0, line):
            if (X[l][c] < _min[c]):
                _min[c] = X[l][c]
            if (X[l][c] > _max[c]):
                _max[c] = X[l][c]
            _mean[c] += X[l][c]
    for c in range(1, col):
        _mean[c] /= line
    for c in range(1, col):
        for l in range(0, line):
            X[l][c] = (X[l][c] - _mean[c]) / (_max[c] - _min[c])
    return (X)

def hypothese(Xline, theta, l):
    TX = Xline
    p = TX.dot(theta)
    ret = 1 / (1 + np.exp(-p))
    return (ret)

def cost(X, Y, theta, line, c, expected):
    som = 0
    for l in range(0, line):
        if (Y[l] == expected):
            y = 0
        else:
            y = 1
        hyp = hypothese(X[l], theta, l)
        res = (hyp - y) * X[l][c]
        som += res
    return (som)

def log_reg(X, Y, theta, line, col, alpha, num_iters, result):
    temp = [[0.0] * col]
    temp = np.reshape(temp, (col, 1))
    for i in range(0, num_iters):
        print(i)
        for exp in range(0, 3):
            for c in range(0, col):
                temp[c] = theta[c] - (alpha * cost(X, Y, theta, line, c, result[exp]))
            for c in range(0, col):
                theta[c] = temp[c]
    return (theta)

result = ['Hufflepuff', 'Gryffindor', 'Slytherin', 'Ravenclaw']
alpha = 0.01
num_iters = 1500
X = change_nan(X, col, line)
X = scale(X, line, col)
theta = log_reg(X, Y, theta, line, col, alpha, num_iters, result)
