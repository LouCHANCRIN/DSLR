import numpy as np
import pandas as pd

def precision(theta, expected_results, matrix, lines):
    object_to_write = {'Hogwarts House': []}
    correct_prediction = 0

    # Turn into a list to avoid issue with indexes when using early stopping
    list_expected_results = expected_results.to_list()

    # For each student we predict the probabilty that he will be in each house
    for l in range(0, lines):
        hufflepuff = 1 / (1 + np.exp(-(matrix[l].dot(theta['Hufflepuff']))))[0]
        gryffindor = 1 / (1 + np.exp(-(matrix[l].dot(theta['Gryffindor']))))[0]
        slytherin = 1 / (1 + np.exp(-(matrix[l].dot(theta['Slytherin']))))[0]
        ravenclaw = 1 / (1 + np.exp(-(matrix[l].dot(theta['Ravenclaw']))))[0]

        # The most probable house will be our prediction
        myguess = max(hufflepuff, gryffindor, slytherin, ravenclaw)

        if myguess == hufflepuff:
            prediction = 'Hufflepuff'
        if myguess == gryffindor:
            prediction = 'Gryffindor'
        if myguess == slytherin:
            prediction = 'Slytherin'
        if myguess == ravenclaw:
            prediction = 'Ravenclaw'

        # We check our prediction with the reality
        if prediction == list_expected_results[l]:
            correct_prediction += 1

        object_to_write['Hogwarts House'].append(prediction)

    df = pd.DataFrame(object_to_write)

    df.to_csv('house.csv', index_label='Index')

    # print("Accuracy  : ", correct_prediction / lines)
    return correct_prediction / lines
