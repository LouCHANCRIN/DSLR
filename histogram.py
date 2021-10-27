import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

TO_EXCLUDE = ["First Name", "Last Name", "Birthday", 'Index', 'Hogwarts House', 'Best Hand']

ressource = sys.argv[1]
data = pd.read_csv(ressource)
line, col = np.shape(data)
Y = data["Hogwarts House"]
# Y= np.reshape(Y, (line, 1))
X = [np.insert(row, 0, 1) for row in data.drop(["Hogwarts House"], axis=1).values]
X = np.reshape(X, (line, col))

name = []
for key in data:
    name.append(key)

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
        if (name[c] not in TO_EXCLUDE):
            _moy = moy(data[name[c]], line)
            for l in range(0, line):
                if (X[l][c] != X[l][c]):
                    X[l][c] = _moy
                    a = a + 1
    return (X)

X = change_nan(X, col, line, data, name)

def plot_histogramme(X, Y, name):
    a = 0
    for j in range(0, col):
        house_1 = []
        house_2 = []
        house_3 = []
        house_4 = []
        for i in range(0, line):
            if (Y[i] == 'Hufflepuff'):
                house_1.append(X[i, j])
            if (Y[i] == 'Slytherin'):
                house_2.append(X[i, j])
            if (Y[i] == 'Gryffindor'):
                house_3.append(X[i, j])
            if (Y[i] == 'Ravenclaw'):
                house_4.append(X[i, j])
        if (name[j] not in TO_EXCLUDE):
            a += 1
            plt.subplot(4, 4, a)
            plt.xlabel(name[j])
            plt.ylabel("Number of students")
            plt.hist([house_1, house_2, house_3, house_4], bins = 'auto',
                    color = ['yellow', 'red', 'green', 'blue'], edgecolor = 'black',
                    density=True)
            plt.legend(['Hufflepuff', 'Gryffindor', 'Slytherin', 'Ravenclaw'])

plot_histogramme(X, Y, name)
plt.show()
