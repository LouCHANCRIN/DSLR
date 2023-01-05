import numpy as np

'''
array = {
            'Hufflepuff': np.reshape([[0.0] * length], (length, 1)),
            'Gryffindor': np.reshape([[0.0] * length], (length, 1)),
            'Slytherin': np.reshape([[0.0] * length], (length, 1)),
            'Ravenclaw': np.reshape([[0.0] * length], (length, 1))
        }
'''
def initialize_arrays(length: int, houses: list):
    array = {}
    for house in houses:
        array[house] = np.reshape([[0.0] * length], (length, 1))
    return array

def set_house(house, expected_results):
    i = 0
    for expected in expected_results:
        house[expected][i] = 1
        i += 1
    return (house)

def scale(matrix, line, col):
    # We've added a column for the bias and we dont want to scale it
    col -= 1
    col_mean = np.nanmean(matrix, axis=0)
    inds = np.where(np.isnan(matrix))
    matrix[inds] = np.take(col_mean, inds[1])

    _min = np.reshape([[0.0] * col], (col, 1))
    _max = np.reshape([[0.0] * col], (col, 1))
    _mean = np.reshape([[0.0] * col], (col, 1))
    for c in range(1, col):
        _min[c] = matrix[0][c]
        _max[c] = matrix[0][c]
    for c in range(1, col):
        for l in range(0, line):
            if (matrix[l][c] < _min[c]):
                _min[c] = matrix[l][c]
            if (matrix[l][c] > _max[c]):
                _max[c] = matrix[l][c]
            _mean[c] += matrix[l][c]
    for c in range(1, col):
        _mean[c] /= line
    for c in range(1, col):
        for l in range(0, line):
            matrix[l][c] = (matrix[l][c] - _mean[c]) / (_max[c] - _min[c])
    return (matrix)
