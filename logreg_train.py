import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

ressource = sys.argv[1]
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

def somme(Yline, hypline):
    return ((Yline * np.log10(hypline)) + ((1 - Yline) * np.log10(1 - hypline)))

def cost(theta, X, Y, line):
    som = 0
    hyp = hypothese(X, theta)
    som = somme(Y, hyp)
    som = np.sum(som)
    return (-1 / line * som)

def hypothese(Xline, theta):
    return (1 / (1 + np.exp(-(Xline.dot(theta)))))

def gradient(X, Y, theta, line, c):
    hyp = hypothese(X, theta) #hypothese
    XX = np.reshape(X[:,c], (1, line))
    ret = XX.dot(hyp - Y) #cost
    return (ret)

def log_reg(X, theta, line, col, alpha, num_iters, landa, house):
    temp = [[0.0] * col]
    temp = np.reshape(temp, (col, 1))
    cost_gen = []
    cost_plot = {}
    cost_plot['Hufflepuff'] = []
    cost_plot['Gryffindor'] = []
    cost_plot['Slytherin'] = []
    cost_plot['Ravenclaw'] = []
    for i in range(0, num_iters):
        for key in theta:
            cout = 0
            for c in range(0, col):
                gradient(X, house[key], theta[key], line, c)
                temp[c] = theta[key][c] - (alpha * gradient(X, house[key], theta[key], line, c))
            for c in range(0, col):
                theta[key][c] = temp[c]
            cout = cost(theta[key], X, house[key], line)
            cost_plot[key].append(cout)
        cost_gen.append(cout / 4)
    for key in cost_plot:
        cost_plot[key] = np.reshape(cost_plot[key], (num_iters, 1))
        plt.xlabel(key)
        plt.plot(cost_plot[key])
        plt.show()
    cost_gen = np.reshape(cost_gen,(num_iters, 1))
    plt.xlabel("general")
    plt.plot(cost_gen)
    plt.show()
    return (theta)

alpha = 0.05 / line
num_iters = 2300
landa = 5
X = change_nan(X, col, line)
X = scale(X, line, col)
#X_train, X_cost = X[ : floor(row * 0.85)], X[floor(row * 0.85) :]
#Y_train, Y_cost = Y[ : floor(row * 0.85)], Y[floor(row * 0.85) :]
theta = log_reg(X, theta, line, col, alpha, num_iters, landa, house)

def precision(theta, Y, X, line):
    my_y = []
    for l in range(0, line):
        H = 0
        G = 0
        S = 0
        R = 0
        for key in theta:
            if (key == 'Hufflepuff'):
                H = 1 / (1 + np.exp(-(X[l].dot(theta[key]))))
            if (key == 'Gryffindor'):
                G = 1 / (1 + np.exp(-(X[l].dot(theta[key]))))
            if (key == 'Slytherin'):
                S = 1 / (1 + np.exp(-(X[l].dot(theta[key]))))
            if (key == 'Ravenclaw'):
                R = 1 / (1 + np.exp(-(X[l].dot(theta[key]))))
        myguess = H
        if (G > H and G > myguess):
            myguess = G
        if (S > G and S > myguess):
            myguess = S
        if (R > S and R > myguess):
            myguess = R
        if (myguess == H):
            my_y.append("Hufflepuff")
        if (myguess == G):
            my_y.append("Gryffindor")
        if (myguess == S):
            my_y.append("Slytherin")
        if (myguess == R):
            my_y.append("Ravenclaw")
    a = 0
    for l in range(0, line):
        if (my_y[l] == Y[l]):
            a += 1
    print(a)
    print("Accuracy  : ", a * 100 / line)
    print("Precision : ", a / (a - (line - a)))

precision(theta, Y, X, line)
