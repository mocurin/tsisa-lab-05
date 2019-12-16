import multicriterial as mo
import numpy as np


if __name__ == '__main__':
    names = np.array(list('ABCD'))
    comparisons = [0, 0, 0, 1, 0.5, 0]
    criteria_matrix = np.array([[0, 9, 1, 9],
                                [9, 7, 3, 7],
                                [5, 5, 5, 5],
                                [3, 3, 9, 3]])
    # Normalize matrix
    sums = np.sum(np.transpose(criteria_matrix), axis=1)
    criteria_matrix = np.divide(criteria_matrix, sums)

    # Create weights array from pairwise comparisons
    weights = mo.create_weights_matrix(4, comparisons, lambda x: 1 - x)
    weights = np.sum(weights, axis=1)
    weights = weights / np.sum(weights)
    result = np.dot(criteria_matrix, weights)

    # Report
    print('Task 3')
    print('NOMALIZED WEIGHTS ARRAY:')
    print(weights)
    print('NORMALIZED CRITERIA MATRIX:')
    for i, row in zip(names, criteria_matrix):
        print(i, *[format(e, '.3f') for e in row], sep=' | ')
    print('UNITED CRITERIA:')
    for i, r in zip(names, result):
        print(i, format(r, '.3f'), sep=' | ')