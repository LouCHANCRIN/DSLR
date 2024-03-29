import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import argparse
import json

import format_data
import metrics

# Excluded because it is not usefull for the learning process
TO_EXCLUDE = ["Hogwarts House", "First Name", "Last Name", "Birthday", "Index", "Best Hand", "Arithmancy", "Astronomy", "Care of Magical Creatures"]
COLORS = {'Hufflepuff': 'yellow', 'Gryffindor': 'red', 'Slytherin': 'green', 'Ravenclaw': 'blue'}
HOUSES = ['Hufflepuff', 'Gryffindor', 'Slytherin', 'Ravenclaw']

alpha = 0.4


def plot(cost_plot, num_iters):
    legend = []

    plt.ylabel('Loss per houses')
    plt.xlabel('Epoch')
    for key in cost_plot:
        cost_plot[key] = np.reshape(cost_plot[key], (num_iters, 1))
        plt.plot(cost_plot[key], c=COLORS[key], label=key)
        legend.append(key)
    plt.legend(legend)
    plt.show()

def sigmoid_function(alpha, matrix, theta, args=None):
    # h
    result = 1 / (1 + np.exp(-(matrix.dot(theta))))
    regularization = 0
    if args:
        # Add the absolute values of the coeficient to shrink the less improtant features
        if args.l1:
            regularization = (alpha / (2 * line_train)) * np.sum(np.abs(theta))

        # Add the square value of the coeficient to minimize the impact of the b
        elif args.l2:
            regularization = (alpha / (2 * line_train)) * np.sum(np.square(theta))
        
    return result + regularization

def cost_function(alpha, theta, matrix, expected_results, args):
    sigmoid_result = sigmoid_function(alpha, matrix, theta, args)
    #     cost if expected_result = 1          cost if expected_result = 0
    som = (expected_results * np.log10(sigmoid_result)) + ((1 - expected_results) * np.log10(1 - sigmoid_result)) #cost function
    som = np.sum(som)
    som = -1 / line_train * som

    return som

def gradient(alpha, matrix, expected_results, theta, c, args):
    sigmoid_result = sigmoid_function(alpha, matrix, theta, args)

    column_data = np.reshape(matrix[:,c], (1, line_train))
    updated_weigths = column_data.dot(sigmoid_result - expected_results)
    return updated_weigths

def log_reg(matrix_train, theta, alpha, num_iters, train_expected_house_object, args, matrix_test=None, test_expected_house_object=None, test_expected_house_list=None):
    temp = np.reshape([[0.0] * col_train], (col_train, 1))
    if args.loss:
        loss_plot = {'Hufflepuff': [], 'Gryffindor': [], 'Slytherin': [], 'Ravenclaw': []}
    if args.early_stopping:
        best_loss = None
        unchanged_epoch = 0

    for i in range(0, num_iters):
        # Loop on houses for the one vs all algorithm
        for key in theta:
            current_general_loss = 0
            
            # Recalculate the weights (theta) for each feature and save it in a temporary variable
            for index in range(0, col_train):
                temp[index] = theta[key][index] - ((alpha  / line_train) * gradient(alpha, matrix_train, train_expected_house_object[key], theta[key], index, args))
            
            # Update all the theta at once
            for index in range(0, col_train):
                theta[key][index] = temp[index]

            # Plot the loss on the training set after updating the weights
            if args.loss:
                loss = cost_function(alpha, theta[key], matrix_train, train_expected_house_object[key], args)
                loss_plot[key].append(loss)
            
            # Calculate the total loss (loss for each house) on the testing set
            if args.early_stopping:
                current_general_loss += cost_function(alpha, theta[key], matrix_test, test_expected_house_object[key], args)

        # Stop the loop if the loss doesnt decrease for 5 iteration
        if args.early_stopping:
            # Intialize the loss
            if best_loss == None:
                best_loss = current_general_loss
            
            # If current loss is barely smaller or equal to best loss, we consider it unchanged
            # If the current loss is much higher than the best loss, we will exit in a further if
            elif current_general_loss + 0.00001 > best_loss or current_general_loss == best_loss:
                unchanged_epoch += 1

            # If current loss < best loss, we update best loss and reset unchanged epoch
            elif current_general_loss < best_loss:
                best_loss = current_general_loss
                unchanged_epoch = 0

            # If the loss has not changed for 5 iterations or started to increase, we stop the training
            if unchanged_epoch == 5 or current_general_loss > best_loss:
                break

    if args.early_stopping:
        print(f"Total epoch performed : {i}")
    if args.loss:
        plot(loss_plot, i + 1)
    
    for key in theta:
        theta[key] = theta[key].tolist()
    with open(args.path_to_weights, 'w') as f:
        json.dump(theta, f)

    return theta

def main(matrix_train, train_houses_list, args, matrix_test=None, test_houses_list=None):
    num_iters = 2000
    test_expected_house = None

    # Initialize the weights
    theta = format_data.initialize_arrays(col_train, HOUSES)

    # Initialize the training houses for the one vs all algorithm
    train_expected_house = format_data.initialize_arrays(line_train, HOUSES)
    matrix_train = format_data.scale(np.reshape(matrix_train, (line_train, col_train)), line_train, col_train)
    train_expected_house_object = format_data.set_house(train_expected_house, train_houses_list)

    # Initialize the testing houses for the one vs all algorithm
    if args.early_stopping:
        test_expected_house = format_data.initialize_arrays(line_test, HOUSES)
        matrix_test = format_data.scale(np.reshape(matrix_test, (line_test, col_test)), line_test, col_test)
        test_expected_house_object = format_data.set_house(test_expected_house, test_houses_list)
    else:
        test_expected_house_object = None

    # Launch the logistic regression
    theta = log_reg(matrix_train, theta, alpha, num_iters, train_expected_house_object, args, matrix_test, test_expected_house_object, test_houses_list)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parse for bonus')
    parser.add_argument('--path', dest='path', help='Path to csv data')
    parser.add_argument('--path_to_weights', dest='path_to_weights', help='Path to save the weights')
    parser.add_argument('--loss', dest='loss', default=False, action='store_true', help='Used to show the loss function graph when training is over')
    parser.add_argument('--l1', dest='l1', default=False, action='store_true', help='Used to reduce the impact of huge weights to prevent overfitting')
    parser.add_argument('--l2', dest='l2', default=False, action='store_true', help='Used to reduce the impact of huge weights to prevent overfitting')
    parser.add_argument('--early_stopping', dest='early_stopping', default=False, action='store_true', help='Split the training data set in training and testsing set so that we can measure how our model perform on data that it hasn\'t used to train and stop when the loss on the testing dataset to prevent overfitting')

    args = parser.parse_args()
    if sum([args.l1, args.l2]) > 1:
        sys.exit('You can use only one regularization at a time')

    if not args.path:
        sys.exit("No file given")

    if not args.path_to_weights:
        sys.exit("No path to save weights have been given")
    else:
        if len(args.path_to_weights) < 6 or not args.path_to_weights[-5:] == '.json':
            sys.exit("Weights must be saved in a json file")

    try:
        df = pd.read_csv(args.path)
        number_of_examples, _ = df.shape
        df['Bias'] = [1.0] * number_of_examples
    except:
        sys.exit(f"Failed to read file {args.path}")

    if args.early_stopping:
        train = df.sample(frac=0.8)
        test = df.drop(train.index)

        line_train, col_train = np.shape(train)
        line_test, col_test = np.shape(test)

        houses_list_train = np.reshape(train["Hogwarts House"], (line_train))
        houses_list_test = np.reshape(test["Hogwarts House"], (line_test))

        matrix_train = [np.insert(row, 0, 1) for row in train.drop(TO_EXCLUDE, axis=1).values]
        matrix_test = [np.insert(row, 0, 1) for row in test.drop(TO_EXCLUDE, axis=1).values]

        line_train, col_train = np.shape(matrix_train)
        line_test, col_test = np.shape(matrix_test)

        main(matrix_train, houses_list_train, args, matrix_test, houses_list_test)

    else:
        line, col_before_drop = np.shape(df)

        houses_list_train = np.reshape(df["Hogwarts House"], (line))

        matrix_train = [np.insert(row, 0, 1) for row in df.drop(TO_EXCLUDE, axis=1).values]

        line_train, col_train = np.shape(matrix_train)

        main(matrix_train, houses_list_train, args)
