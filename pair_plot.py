import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

ressource = sys.argv[1]
data = pd.read_csv(ressources)
line, col = np.shape(data)
Y = data["Hogwarts House"]
Y= np.reshape(Y, (line, 1))
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
        if (name[c] != "First Name" and name[c] != "Last Name" and name[c] != "Birthday"
            and name[c] != 'Index' and name[c] != 'Hogwarts House'
            and name[c] != 'Best Hand'):
                _moy = moy(data[name[c]], line)
                for l in range(0, line):
                    if (X[l][c] != X[l][c]):
                        X[l][c] = _moy
                        a = a + 1
    return (X)

def pair_plot(X, name, col, line, Y):
    a = 1
    for c in range(1, col):
        for c2 in range (0, col):
            if (name[c] != 'First Name' and name[c] != 'Last Name'
                and name[c] != 'Birthday' and name[c] != 'Index'
                and name[c] != 'Hogwarts House' and name[c] != 'Best Hand'
                and name[c2] != 'First Name' and name[c2] != 'Last Name'
                and name[c2] != 'Birthday' and name[c2] != 'Index'
                and name[c2] != 'Hogwarts House' and name[c2] != 'Best Hand'):
                H1 = {}
                H2 = {}
                H1['Hufflepuff'] = []
                H1['Gryffindor'] = []
                H1['Slytherin'] = []
                H1['Ravenclaw'] = []
                H2['Hufflepuff'] = []
                H2['Gryffindor'] = []
                H2['Slytherin'] = []
                H2['Ravenclaw'] = []
                for l in range(0, line):
                    if (Y[l] == 'Hufflepuff'):
                        if (X[l][c] == X[l][c]):
                            H1['Hufflepuff'].append(X[l][c])
                        if (X[l][c2] == X[l][c2]):
                            H2['Hufflepuff'].append(X[l][c2])
                    if (Y[l] == 'Gryffindor'):
                        if (X[l][c] == X[l][c]):
                            H1['Gryffindor'].append(X[l][c])
                        if (X[l][c2] == X[l][c2]):
                            H2['Gryffindor'].append(X[l][c2])
                    if (Y[l] == 'Slytherin'):
                        if (X[l][c] == X[l][c]):
                            H1['Slytherin'].append(X[l][c])
                        if (X[l][c2] == X[l][c2]):
                            H2['Slytherin'].append(X[l][c2])
                    if (Y[l] == 'Ravenclaw'):
                        if (X[l][c] == X[l][c]):
                            H1['Ravenclaw'].append(X[l][c])
                        if (X[l][c2] == X[l][c2]):
                            H2['Ravenclaw'].append(X[l][c2])
                if (c == c2):
                    plt.subplot(5, 5, a)
                    plt.xlabel(name[c])
                    plt.ylabel(name[c2])
                    plt.hist([H1['Hufflepuff'], H1['Gryffindor'], H1['Slytherin'],
                        H1['Ravenclaw']], bins='auto', density='true',
                        color=['yellow', 'red', 'green', 'blue'], edgecolor='black')
                    plt.legend(['Hufflepuff', 'Gryffindor', 'Slytherin', 'Ravenclaw'])
                    a += 1
                else:
                    plt.subplot(5, 5, a)
                    plt.xlabel(name[c])
                    plt.ylabel(name[c2])
                    plt.scatter(H1['Hufflepuff'], H2['Hufflepuff'], color='yellow',
                            edgecolor='black')
                    plt.scatter(H1['Gryffindor'], H2['Gryffindor'], color='red', edgecolor='black')
                    plt.scatter(H1['Slytherin'], H2['Slytherin'], color='green', edgecolor='black')
                    plt.scatter(H1['Ravenclaw'], H2['Ravenclaw'], color='blue', edgecolor='black')
                    plt.legend(['Hufflepuff', 'Gryffindor', 'Slytherin', 'Ravenclaw'])
                    a += 1

                if (a == 26):
                    a = 1
                    plt.show()
    plt.show()

X = change_nan(X, col, line, data, name)
pair_plot(X, name, col, line, Y)
