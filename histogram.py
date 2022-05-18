import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

TO_EXCLUDE = ["First Name", "Last Name", "Birthday", 'Index', 'Hogwarts House', 'Best Hand']


def plot_histogram(data, classes_name):
    a = 0
    for class_name in classes_name:
        if class_name not in TO_EXCLUDE:
            hufflepuff = df[df['Hogwarts House']=='Hufflepuff'][class_name]
            gryffindor = df[df['Hogwarts House']=='Gryffindor'][class_name]
            slytherin = df[df['Hogwarts House']=='Slytherin'][class_name]
            ravenclaw = df[df['Hogwarts House']=='Ravenclaw'][class_name]
            a += 1
            plt.subplot(4, 4, a)
            plt.xlabel(class_name)
            plt.ylabel("Number of students")
            plt.hist([hufflepuff, gryffindor, slytherin, ravenclaw], bins = 'auto',
                    color = ['yellow', 'red', 'green', 'blue'], edgecolor = 'black',
                    density=True)
            plt.legend(['Hufflepuff', 'Gryffindor', 'Slytherin', 'Ravenclaw'])
    plt.show()

if __name__ == "__main__":
    if (len(sys.argv) <= 1):
        sys.exit("No name file")
    if (len(sys.argv) >= 3):
        sys.exit("too much file")

    ressource = sys.argv[1]
    try:
        data = pd.read_csv(ressource)
    except:
        sys.exit(f"Failed to read file {sys.argv[1]}")
    ressource = sys.argv[1]
    df = pd.read_csv(ressource)

    classes_name = list(df.keys())
    plot_histogram(df, classes_name)