import pandas as pd
import numpy as np
import math

data = pd.read_csv("ressources/dataset_train.csv")
print(pd.DataFrame.describe(data))
line, col = np.shape(data)
X = [np.insert(row, 0, 1) for row in data.drop(["Hogwarts House"], axis=1).values]
X = np.reshape(X, (line, col))

name = []
for key in data:
    name.append(key)

def sort_data(X):
    for c in range(0, col):
        for l in range(0, line):
            for l2 in range(l, line):
                if (X[l][c] == X[l][c] and X[l2][c] == X[l2][c]):
                    if (X[l][c] > X[l2][c]):
                        tmp = X[l][c]
                        X[l][c] = X[l2][c]
                        X[l2][c] = tmp
    return (X)

X = sort_data(X)

def fill_feature(X, line, name):
    feature = []
    for j in range(0, col):
        if (name[j] != "First Name" and name[j] != "Last Name" and name[j] != "Birthday"
                and name[j] != "Hogwarts House" and name[j] != 'Index'
                and name[j] != 'Best Hand'):
            count = 0
            mean = 0
            ma = X[0][j]
            mi = X[0][j]
            for i in range(0, line):
                if (X[i][j] == X[i][j]):
                    if (X[i][j] > ma):
                        ma = X[i][j]
                    if (X[i][j] < mi):
                        mi = X[i][j]
                    mean += X[i][j]
                    count += 1
            std = 0
            mean /= count
            for i in range(0, line):
                if (X[i][j] == X[i][j]):
                    std += (X[i][j] - mean) ** 2
            std /= count
            std = math.sqrt(std)
            feature.append(count)
            feature.append(mean)
            feature.append(std)
            feature.append(mi)
#           premier quartil
            q = round(count / 4, 0)
            _25 = 0
            while (_25 < q):
                _25 += 1
#           deuxieme quartil
            q = round(count / 2, 0)
            _50 = 0
            while (_50 < q):
                _50 += 1
#           troisieme quartil
            q = round(count - (count / 4), 0)
            _75 = 0
            while (_75 < q):
                _75 += 1
#           ok
            while (X[_25][j] != X[_25][j]):
                _25 += 1
            while (X[_50][j] != X[_50][j]):
                _50 += 1
            while (X[_75][j] != X[_75][j]):
                _75 += 1
            print("25 = ", _25, "50 = ", _50, "75 = ", _75)
            feature.append(X[_25][j])
            feature.append(X[_50][j])
            feature.append(X[_75][j])
            feature.append(ma)
    return (feature)

feature = fill_feature(X, line, name)

feature = np.reshape(feature, (8, 13))
print(feature)

for l in range(0, 9):
    for c in range(0, col + 1):
        if (c == 0):
            if (l == 0):
                print("         ")
            if (l == 1):
                print("Count    ")
            if (l == 2):
                print("Mean     ")
            if (l == 3):
                print("Std      ")
            if (l == 4):
                print("Min      ")
            if (l == 5):
                print("25%      ")
            if (l == 6):
                print("50%      ")
            if (l == 7):
                print("75%      ")
            if (l == 8):
                print("Max    ")
            
