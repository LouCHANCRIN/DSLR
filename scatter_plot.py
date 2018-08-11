import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

ressource = sys.argv[1]
data = pd.read_csv(ressource)
line, col = np.shape(data)
Y = data["Hogwarts House"]
Y= np.reshape(Y, (line, 1))
X = [np.insert(row, 0, 1) for row in data.drop(["Hogwarts House"], axis=1).values]
X = np.reshape(X, (line, col))

name = []
for key in data:
    name.append(key)

def count(X, line, col):
    lst = []
    for c in range(0, col):
        a = 0
        for l in range(0, line):
            if (X[l][c] == X[l][c]):
                a += 1
        lst.append(a)
    return (lst)

def check_house(X, line, col, Y, lst):
    same = []
    a = 0
    same.append(0)
    for c in range(0, col):
        for c2 in range(c + 1, col):
            if (name[c] != "First Name" and name[c] != "Last Name" and name[c] != "Birthday"
                    and name[c] != 'Index' and name[c] != 'Hogwarts House'
                    and name[c] != 'Best Hand' and lst[c] == lst[c2]):
                if (lst[c] == lst[c2]):
                    house_1 = 0
                    house_2 = 0
                    house_3 = 0
                    house_4 = 0
                    house_1_2 = 0
                    house_2_2 = 0
                    house_3_2 = 0
                    house_4_2 = 0
                    for l in range(0, line):
                        if (X[l][c] == X[l][c]):
                            if (Y[l] == 'Hufflepuff'):
                                house_1 += 1
                            if (Y[l] == 'Slytherin'):
                                house_2 += 1
                            if (Y[l] == 'Gryffindor'):
                                house_3 += 1
                            if (Y[l] == 'Ravenclaw'):
                                house_4 += 1
                        if (X[l][c2] == X[l][c2]):
                            if (Y[l] == 'Hufflepuff'):
                                house_1_2 += 1
                            if (Y[l] == 'Slytherin'):
                                house_2_2 += 1
                            if (Y[l] == 'Gryffindor'):
                                house_3_2 += 1
                            if (Y[l] == 'Ravenclaw'):
                                house_4_2 += 1
                    if (house_1 == house_1_2 and house_2 == house_2_2
                        and house_3 == house_3_2 and house_4 == house_4_2):
                        same.append(c)
                        same.append(c2)
                        a += 2
    same[0] = a
    return (same)

def scatter_plot(X, name, same, line, Y):
    for c in range(1, same[0]):
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
                if (X[l][same[c]] == X[l][same[c]]):
                    H1['Hufflepuff'].append(X[l][same[c]])
                if (X[l][same[c + 1]] == X[l][same[c + 1]]):
                    H2['Hufflepuff'].append(X[l][same[c + 1]])
            if (Y[l] == 'Gryffindor'):
                if (X[l][same[c]] == X[l][same[c]]):
                    H1['Gryffindor'].append(X[l][same[c]])
                if (X[l][same[c + 1]] == X[l][same[c + 1]]):
                    H2['Gryffindor'].append(X[l][same[c + 1]])
            if (Y[l] == 'Slytherin'):
                if (X[l][same[c]] == X[l][same[c]]):
                    H1['Slytherin'].append(X[l][same[c]])
                if (X[l][same[c + 1]] == X[l][same[c + 1]]):
                    H2['Slytherin'].append(X[l][same[c + 1]])
            if (Y[l] == 'Ravenclaw'):
                if (X[l][same[c]] == X[l][same[c]]):
                    H1['Ravenclaw'].append(X[l][same[c]])
                if (X[l][same[c + 1]] == X[l][same[c + 1]]):
                    H2['Ravenclaw'].append(X[l][same[c + 1]])
        plt.xlabel(name[same[c]])
        plt.ylabel(name[same[c + 1]])
        plt.scatter(H1['Hufflepuff'], H2['Hufflepuff'], color='yellow', edgecolor='black')
        plt.scatter(H1['Gryffindor'], H2['Gryffindor'], color='red', edgecolor='black')
        plt.scatter(H1['Slytherin'], H2['Slytherin'], color='green', edgecolor='black')
        plt.scatter(H1['Ravenclaw'], H2['Ravenclaw'], color='blue', edgecolor='black')
        plt.legend(['Hufflepuff', 'Gryffindor', 'Slytherin', 'Ravenclaw'])

        plt.show()
        c += 1

lst = count(X, line, col)
same = check_house(X, line, col, Y, lst)
scatter_plot(X, name, same, line, Y)
