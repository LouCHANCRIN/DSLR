import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#help(plt.hist)

data = pd.read_csv("ressources/dataset_train.csv")
line, col = np.shape(data)
Y = data["Hogwarts House"]
Y= np.reshape(Y, (line, 1))
X = [np.insert(row, 0, 1) for row in data.drop(["Hogwarts House"], axis=1).values]
X = np.reshape(X, (line, col))

name = []
for key in data:
    name.append(key)

def change_nan(X, col, line, data, name):
    a = 0
    for i in range(0, col):
        for j in range(0, line):
            if (X[j][i] != X[j][i]):
                X[j][i] = data[name[i]].mean()
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
        if (name[j] != "First Name" and name[j] != "Last Name" and name[j] != "Birthday"
                and name[j] != "Hogwarts House" and name[j] != 'Index'
                and name[j] != 'Best Hand'):
            a += 1
            plt.subplot(4, 4, a)
            plt.xlabel(name[j])
            plt.ylabel("Number of students")
            plt.hist([house_1, house_2, house_3, house_4], bins = 'auto',
                    color = ['yellow', 'red', 'green', 'blue'], edgecolor = 'black',
                    density=True)
#            l1 = plt.bar(range(1), width=0, height=0, color='yellow')
#            l2 = plt.bar(range(1), width=0, height=0, color='red')
#            l3 = plt.bar(range(1), width=0, height=0, color='green')
#            l4 = plt.bar(range(1), width=0, height=0, color='blue')
#            plt.legend([l1, l2, l3 ,l4], ['Hufflepuff', 'Gryffindor', 'Slytherin', 'Ravenclaw'])
            plt.legend(['Hufflepuff', 'Gryffindor', 'Slytherin', 'Ravenclaw'])

plot_histogramme(X, Y, name)
plt.show()
