import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
#help(plt.hist)
data = pd.read_csv("ressources/dataset_test.csv")
line, col = np.shape(data)
print(line, col)
Y = data["Hogwarts House"]
Y= np.reshape(Y, (line, 1))
X = [np.insert(row, 0, 1) for row in data.drop(["Hogwarts House"], axis=1).values]
test = [np.insert(row, 0, 1) for row in data.drop(["Hogwarts House"], axis=1).values]
X = np.reshape(X, (line, col))
#test = np.reshape(X, (line, col))
q = 0
for key in data:
    print(q, "  ", key)
    q = q + 1
plt.xlabel('Result')
plt.ylabel('Number of student')
#nan = np.arange(line * col).reshape(line, col)
#print(np.isnan(nan))
a = 0
for i in range(0, col):
    for j in range(0, line):
        if (X[j][i] != X[j][i]):
            X[j][i] = 0
            a = a + 1
            
print("\n\nnb_nan = ", a, "\n\n")
print(X[:,15])
#plt.hist(X[:,15])
plt.hist(X[:,15], bins=1)
plt.show()
