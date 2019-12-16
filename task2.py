import multicriterial as mo
import numpy as np


if __name__ == '__main__':
    names = np.array(list('ABCD'))
    criteria_matrix = np.array([[0, 9, 1, 9],
                                [9, 7, 3, 7],
                                [5, 5, 5, 5],
                                [3, 3, 9, 3]])
    dist = mo.pareto_set(criteria_matrix, [1, 2], (10, 10), ['Diploma', 'Scholarship'], names)
    index = np.argmin(dist)

    # Report
    print('TASK 2')
    print('CRITERIA MATRIX:')
    for i, row in zip(names, criteria_matrix):
        print(i, *row, sep=' | ')
    print('VARIANT DISTANCES:')
    for i, d in zip(names, dist):
        print(i, d, sep=' | ')
    print('OPTIMAL VARIANT:')
    print(names[index], *criteria_matrix[index], sep=' | ')