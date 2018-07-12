import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
#help(plt.hist)
data = pd.read_csv("ressources/dataset_train.csv")
print(data)
line, col = np.shape(data)
print(line, col)
Y = data["Hogwarts House"]
Y= np.reshape(Y, (line, 1))
X = [np.insert(row, 0, 1) for row in data.drop(["Hogwarts House"], axis=1).values]
test = [np.insert(row, 0, 1) for row in data.drop(["Hogwarts House"], axis=1).values]
X = np.reshape(X, (line, col))

name = []
q = 0
for key in data:
    name.append(key)
    print(q, "  ", key)
    q = q + 1

a = 0
for i in range(0, col):
    for j in range(0, line):
        if (X[j][i] != X[j][i]):
            X[j][i] = 0
            a = a + 1

_min = 0.0
_max = 0.0
for i in range(0, line):
    if (_min > X[i][15]):
        _min = X[i][15]
    if (_max < X[i][15]):
        _max = X[i][15]

print("\n\nnb_nan = ", a, "\n\n")
print(_min, _max)
#plt.xlabel('Result')
#plt.ylabel('Number of student')
age = [10, 25, 10.1, 10.2, 10.3, 10.4, 45, 65, 74 ,21 ,35 ,21 ,21 ,35, 28, 29]
#bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]
#plt.hist(age, bins, histtype='bar', rwidth=0.8)
bins = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#plt.hist(X[:,15], bins, histtype='bar', cumulative=True)
#for i in range(0, col):
#    plt.hist(X[:,i], bins = 'auto')
#x = []
#for i in range(0, line):
#    x.append(X[i, 16])
#plt.hist(x, edgecolor = 'red', color = 'black')
#plt.hist([x], bins = 'auto', color = ['blue', 'red'])

Huffle = 0
Gryffin = 0
Slyther = 0
Raven = 0
for i in range(0, line):
    if (Y[i] == 'Hufflepuff'):
        Huffle = Huffle + 1
    if (Y[i] == 'Slytherin'):
        Gryffin = Gryffin + 1
    if (Y[i] == 'Gryffindor'):
        Slyther = Slyther + 1
    if (Y[i] == 'Ravenclaw'):
        Raven = Raven + 1

print("Huffle = ", Huffle)
print("Gryffin = ", Gryffin)
print("Slyther = ", Slyther)
print("Raven = ", Raven)
o = 0
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
    if (name[j] != "First Name" and name[j] != "Last Name" and name[j] != "Birthday"
            and name[j] != "Hogwarts House"):
        o += 1
        plt.subplot(4, 4, o)
        plt.xlabel(name[j])
        plt.ylabel("Number of students")
        plt.hist([house_1, house_2, house_3, house_4], bins = 'auto', color = ['yellow', 'red', 'green', 'black'], edgecolor = 'blue')
plt.show()
