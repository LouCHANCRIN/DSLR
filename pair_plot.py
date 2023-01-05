import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

def main():
    if (len(sys.argv) <= 1):
        sys.exit("No name file")
    if (len(sys.argv) >= 3):
        sys.exit("too much file")

    ressource = sys.argv[1]
    try:
        data = pd.read_csv(ressource)
    except:
        sys.exit(f"Failed to read file {sys.argv[1]}")
    data = data.drop(['First Name', 'Last Name', 'Birthday', 'Index'], axis=1)
    data['Best Hand'] = data['Best Hand'].map({'Right': 0, 'Left': 1})
    # Remove best hand, arithmancy and care of magical creatures because
    # they have an omogenous distribution across houses
    # Remove Astronomy because it is similar to defense against the dark arts
    data = data.drop(['Best Hand', 'Arithmancy', 'Care of Magical Creatures'], axis=1)
    # data = data.drop(['Best Hand', 'Astronomy', 'Arithmancy', 'Care of Magical Creatures'], axis=1)
    sns.pairplot(data, hue="Hogwarts House")
    plt.show()

if __name__ == "__main__":
    main()