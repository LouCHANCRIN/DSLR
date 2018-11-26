import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

ressource = sys.argv[1]
data = pd.read_csv(ressource)
line, col = np.shape(data)
X = [np.insert(row, 0, 1) for row in data.drop(["Hogwarts House", "First Name",
    "Last Name", "Birthday", "Index", "Best Hand", "Arithmancy", "Astronomy",
    "Care of Magical Creatures"], axis=1).values]
col -= 8

def set_house(house, Y, line):
    for key in house:
        for i in range(0, line):
            if (Y[i] == key):
                house[key][i] = 1
    return (house)

def precision(theta, Y, X):
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
    print("Accuracy  : ", a / line)

def plot(cost_plot, cost_gen, num_iters):
    for key in cost_plot:
        cost_plot[key] = np.reshape(cost_plot[key], (num_iters, 1))
        plt.xlabel(key)
        plt.plot(cost_plot[key])
        plt.show()
    cost_gen = np.reshape(cost_gen,(num_iters, 1))
    plt.xlabel("general")
    plt.plot(cost_gen)
    plt.show()

def moy(X, line):
    count = 0
    _sum = 0
    for l in range(0, line):
        if (X[l] == X[l]):
            _sum += X[l]
            count += 1
    return (_sum / count)

def change_nan(X):
    a = 0
    for c in range(0, col):
        _moy = moy(X[:,c], line)
        for l in range(0, line):
            if (X[l][c] != X[l][c]):
                X[l][c] = _moy
                a = a + 1
    return (X)

def scale(X):
    X = change_nan(X)
    _min = np.reshape([[0.0] * col], (col, 1))
    _max = np.reshape([[0.0] * col], (col, 1))
    _mean = np.reshape([[0.0] * col], (col, 1))
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

def cost(theta, X, Y):
    hyp = 1 / (1 + np.exp(-(X.dot(theta)))) #hypothese sigmoid
    som = (Y * np.log10(hyp)) + ((1 - Y) * np.log10(1 - hyp)) #cost function
    som = np.sum(som)
    return (-1 / line * som)

def gradient(X, Y, theta, c):
    hyp = 1 / (1 + np.exp(-(X.dot(theta)))) #hypothese sigmoid
    XX = np.reshape(X[:,c], (1, line))
    ret = XX.dot(hyp - Y)
    return (ret)

def log_reg(X, theta, alpha, num_iters, house):
    temp = np.reshape([[0.0] * col], (col, 1))
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
                gradient(X, house[key], theta[key], c)
                temp[c] = theta[key][c] - ((alpha  / line) * gradient(X, house[key], theta[key], c))
            for c in range(0, col):
                theta[key][c] = temp[c]
            cout = cost(theta[key], X, house[key])
            cost_plot[key].append(cout)
        cost_gen.append(cout / 4)
    plot(cost_plot, cost_gen, num_iters)
    return (theta)

def main(X):
    alpha = 0.4
    num_iters = 300
    theta = {'Hufflepuff': np.reshape([[0.0] * col], (col, 1)),
            'Gryffindor': np.reshape([[0.0] * col], (col, 1)),
            'Slytherin': np.reshape([[0.0] * col], (col, 1)),
            'Ravenclaw': np.reshape([[0.0] * col], (col, 1))}
    house = {'Hufflepuff': np.reshape([[0.0] * line], (line, 1)),
            'Gryffindor': np.reshape([[0.0] * line], (line, 1)),
            'Slytherin': np.reshape([[0.0] * line], (line, 1)),
            'Ravenclaw': np.reshape([[0.0] * line], (line, 1))}
    Y = np.reshape(data["Hogwarts House"], (line, 1))
    X = scale(np.reshape(X, (line, col)))
    house = set_house(house, Y, line)
    theta = log_reg(X, theta, alpha, num_iters, house)
    precision(theta, Y, X)

if __name__ == "__main__":
    main(X)
