import pandas as pd
import numpy as np
import sys
import argparse
import json

import format_data
import metrics
from logreg_train import TO_EXCLUDE, HOUSES

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parse for bonus')
    parser.add_argument('--path', dest='path', help='Path to csv data')
    parser.add_argument('--path_to_weights', dest='path_to_weights', help='Path to load the weights')

    args = parser.parse_args()

    if not args.path:
        sys.exit("No file given")

    if not args.path_to_weights:
        sys.exit("No path to load weights have been given")
    else:
        if len(args.path_to_weights) < 6 or not args.path_to_weights[-5:] == '.json':
            sys.exit("Weights must be loaded from a json file")

    try:
        df = pd.read_csv(args.path)
    except:
        sys.exit(f"Failed to read file {args.path}")

    
    line, col = np.shape(df)

    houses_list = np.reshape(df["Hogwarts House"], (line))

    matrix = [np.insert(row, 0, 1) for row in df.drop(TO_EXCLUDE, axis=1).values]

    line, col = np.shape(matrix)

    matrix = format_data.scale(np.reshape(matrix, (line, col)), line, col)

    with open(args.path_to_weights, 'r') as f:
        theta = json.load(f)

    for key in theta:
        theta[key] = np.array(theta[key])

    metrics.precision(theta, houses_list, matrix, line)