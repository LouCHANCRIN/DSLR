import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

ressource = sys.arg[1]
data = pd.read_csv(ressource)
line, col = np.shape(data)
Y = data["Hogwarts House"]
Y= np.reshape(Y, (line, 1))
X = [np.insert(row, 0, 1) for row in data.drop(["Hogwarts House", "First Name",
    "Last Name", "Birthday", "Index", "Best Hand", "Arithmancy", "Astronomy",
    "Care of Magical Creatures"], axis=1).values]

col -= 8
X = np.reshape(X, (line, col))

theta = {}
theta['Hufflepuff'] = np.reshape([[0.0] * col], (col, 1))
theta['Gryffindor'] = np.reshape([[0.0] * col], (col, 1))
theta['Slytherin'] = np.reshape([[0.0] * col], (col, 1))
theta['Ravenclaw'] = np.reshape([[0.0] * col], (col, 1))

house = {}
house['Hufflepuff'] = np.reshape([[0.0] * line], (line, 1))
house['Gryffindor'] = np.reshape([[0.0] * line], (line, 1))
house['Slytherin'] = np.reshape([[0.0] * line], (line, 1))
house['Ravenclaw'] = np.reshape([[0.0] * line], (line, 1))

for key in house:
    for i in range(0, line):
        if (Y[i] == key):
            house[key][i] = 1

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

def hypothese(Xline, theta):
    return (1 / (1 + np.exp(-(Xline.dot(theta)))))

def cost(X, Y, theta, line, c):
    hyp = hypothese(X, theta) #hypothese
    XX = np.reshape(X[:,c], (1, line))
    ret = XX.dot(hyp - Y) #cost
    return (ret)

def log_reg(X, theta, line, col, alpha, num_iters, landa, house):
    temp = [[0.0] * col]
    temp = np.reshape(temp, (col, 1))
    for i in range(0, num_iters):
        for key in theta:
            for c in range(0, col):
                temp[c] = theta[key][c] - (alpha * cost(X, house[key], theta[key], line, c))
            for c in range(0, col):
                theta[key][c] = temp[c]
    return (theta)

alpha = 0.01
num_iters = 11
landa = 5
X = change_nan(X, col, line)
X = scale(X, line, col)
theta = log_reg(X, theta, line, col, alpha, num_iters, landa, house)

def precision(theta, Y, X, line):
    for key in theta:
        print(key)
        a = 0
        b = 0
        for l in range(0, line):
            if (key == Y[l]):
                b += 1
                if (1 / (1 + np.exp(-(X[l].dot(theta[key])))) >= 0.5):
                    a += 1
        print(a)
        print(b)
        print((a * 100 / b))

def precision_global(theta, Y, X, line):
    a = 0
    print("global precision :")
    for l in range(0, line):
        for key in theta:
            if (1 / (1 + np.exp(-(X[l].dot(theta[key])))) >= 0.5):
                if (Y[l] == key):
                    a += 1
    print(a)
    print(a * 100 / line)

precision(theta, Y, X, line)
precision_global(theta, Y, X, line)
