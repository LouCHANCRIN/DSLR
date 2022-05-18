import numpy as np

def precision(theta, expected_results, matrix, lines):
    my_y = []
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

        # We check our prediction with the reality
        if (myguess == hufflepuff and list_expected_results[l] == 'Hufflepuff'):
            correct_prediction += 1
        if (myguess == gryffindor and list_expected_results[l] == 'Gryffindor'):
            correct_prediction += 1
        if (myguess == slytherin and list_expected_results[l] == 'Slytherin'):
            correct_prediction += 1
        if (myguess == ravenclaw and list_expected_results[l] == 'Ravenclaw'):
            correct_prediction += 1

    # print("Accuracy  : ", correct_prediction / lines)
    return correct_prediction / lines
