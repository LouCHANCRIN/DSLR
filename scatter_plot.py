import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

def scatter_plot(df):
    hufflepuff_defense = df[df['Hogwarts House']=='Hufflepuff']['Defense Against the Dark Arts']
    gryffindor_defense = df[df['Hogwarts House']=='Gryffindor']['Defense Against the Dark Arts']
    slytherin_defense = df[df['Hogwarts House']=='Slytherin']['Defense Against the Dark Arts']
    ravenclaw_defense = df[df['Hogwarts House']=='Ravenclaw']['Defense Against the Dark Arts']

    hufflepuff_astro = df[df['Hogwarts House']=='Hufflepuff']['Astronomy']
    gryffindor_astro = df[df['Hogwarts House']=='Gryffindor']['Astronomy']
    slytherin_astro = df[df['Hogwarts House']=='Slytherin']['Astronomy']
    ravenclaw_astro = df[df['Hogwarts House']=='Ravenclaw']['Astronomy']

    plt.scatter(hufflepuff_defense, hufflepuff_astro, color='yellow', edgecolor='black')
    plt.scatter(gryffindor_defense, gryffindor_astro, color='red', edgecolor='black')
    plt.scatter(slytherin_defense, slytherin_astro, color='green', edgecolor='black')
    plt.scatter(ravenclaw_defense, ravenclaw_astro, color='blue', edgecolor='black')
    plt.legend(['Hufflepuff', 'Gryffindor', 'Slytherin', 'Ravenclaw'])
    plt.xlabel('Defense Against the Dark Arts')
    plt.ylabel('Astronomy')

    plt.show()

if __name__ == '__main__':
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
    similar_classes = ['Defense Against the Dark Arts', 'Astronomy']

    scatter_plot(df)