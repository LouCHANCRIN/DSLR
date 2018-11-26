import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

ressource = sys.argv[1]
data = pd.read_csv(ressource)
line, col = np.shape(data)

def count(X, line, col):
    lst = []
    for c in range(0, col):
        a = 0
        for l in range(0, line):
            if (X[l][c] == X[l][c]):
                a += 1
        lst.append(a)
    return (lst)

def moy(X, line):
    count = 0
    _sum = 0
    for l in range(0, line):
        if (X[l] == X[l]):
            _sum += X[l]
            count += 1
    return (_sum / count)

def change_nan(X, col, line, data, name):
    a = 0
    for c in range(0, col):
        if (name[c] != "First Name" and name[c] != "Last Name" and name[c] != "Birthday"
            and name[c] != 'Index' and name[c] != 'Hogwarts House'
            and name[c] != 'Best Hand'):
                _moy = moy(data[name[c]], line)
                for l in range(0, line):
                    if (X[l][c] != X[l][c]):
                        X[l][c] = _moy
                        a = a + 1
    return (X)

def scatter_plot(X, name, index, line, Y):
    H1 = {'Hufflepuff' : [], 'Gryffindor' : [], 'Slytherin' : [], 'Ravenclaw' : []}
    H2 = {'Hufflepuff' : [], 'Gryffindor' : [], 'Slytherin' : [], 'Ravenclaw' : []}
    for l in range(0, line):
        for key in H1:
            if (Y[l] == key):
                    H1[key].append(X[l][index[0]])
                    H2[key].append(X[l][index[1]])
    plt.xlabel(name[index[0]])
    plt.ylabel(name[index[1]])
    plt.scatter(H1['Hufflepuff'], H2['Hufflepuff'], color='yellow', edgecolor='black')
    plt.scatter(H1['Gryffindor'], H2['Gryffindor'], color='red', edgecolor='black')
    plt.scatter(H1['Slytherin'], H2['Slytherin'], color='green', edgecolor='black')
    plt.scatter(H1['Ravenclaw'], H2['Ravenclaw'], color='blue', edgecolor='black')
    plt.legend(['Hufflepuff', 'Gryffindor', 'Slytherin', 'Ravenclaw'])

    plt.show()

if __name__ == '__main__':
    Y = data["Hogwarts House"]
    Y = np.reshape(Y, (line, 1))
    X = [np.insert(row, 0, 1) for row in data.drop(["Hogwarts House"], axis=1).values]
    X = np.reshape(X, (line, col))

    name = []
    for key in data:
        name.append(key)

    i = 0
    index = []
    similar = ['Defense Against the Dark Arts', 'Astronomy']
    for key in data:
        for c in range(0, np.shape(similar)[0]):
            if (key == similar[c]):
                index.append(i)
        i += 1

    X = change_nan(X, col, line, data, name)
    scatter_plot(X, name, index, line, Y)

