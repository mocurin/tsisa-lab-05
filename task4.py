import multicriterial as mo
import numpy as np


def print_matrix(matrix, columns=None, form='.3f', sep=' | '):
    if columns is not None:
        print(*columns, sep=sep)
    for row in matrix:
        print(*[format(e, form) for e in row], sep=sep)


if __name__ == '__main__':
    # Random consistency criteria for 4x4 matrix
    rci = 0.90
    names = np.array(list('ABCD'))
    columns = ['A    ', 'B    ', 'C    ', 'D    ', 'GM   ', 'Norm ']

    print('Scholarship criteria')
    criteria = [1/7, 1/5, 1/3, 3., 5., 3.]
    criteria_weights = mo.create_weights_matrix(4,
                                                criteria,
                                                lambda x: 1 / x)
    means, npv_1 = mo.normalized_priority_vector(criteria_weights)
    print_matrix(np.hstack([criteria_weights,
                            means[:, np.newaxis],
                            npv_1[:, np.newaxis]]),
                 columns)
    cons = mo.consistency(criteria_weights, npv_1, rci)
    print('First criteria consistency: {}'.format(round(cons, 3)))

    print('Qualification criteria')
    criteria = [5, 7, 9, 3, 7, 5]
    criteria_weights = mo.create_weights_matrix(4,
                                                criteria,
                                                lambda x: 1 / x)
    means, npv_2 = mo.normalized_priority_vector(criteria_weights)
    print_matrix(np.hstack([criteria_weights,
                            means[:, np.newaxis],
                            npv_2[:, np.newaxis]]),
                 columns)
    cons = mo.consistency(criteria_weights, npv_2, rci)
    print('Second criteria consistency: {}'.format(round(cons, 3)))

    print('Town living cost')
    criteria = [1/3, 1/5, 1/9, 1/3, 1/7, 1/5]
    criteria_weights = mo.create_weights_matrix(4,
                                                criteria,
                                                lambda x: 1 / x)
    means, npv_3 = mo.normalized_priority_vector(criteria_weights)
    print_matrix(np.hstack([criteria_weights,
                            means[:, np.newaxis],
                            npv_3[:, np.newaxis]]),
                 columns)
    cons = mo.consistency(criteria_weights, npv_3, rci)
    print('Third criteria consistency: {}'.format(round(cons, 3)))

    print('Diploma prestige')
    criteria = [5, 7, 9, 3, 7, 5]
    criteria_weights = mo.create_weights_matrix(4,
                                                criteria,
                                                lambda x: 1 / x)
    means, npv_4 = mo.normalized_priority_vector(criteria_weights)
    print_matrix(np.hstack([criteria_weights,
                            means[:, np.newaxis],
                            npv_4[:, np.newaxis]]),
                 columns)
    cons = mo.consistency(criteria_weights, npv_4, rci)
    print('Fourth criteria consistency: {}'.format(round(cons, 3)))

    print('Total criteria')
    criteria = [1/9, 1/3, 1/9, 7, 1, 1/7]
    criteria_weights = mo.create_weights_matrix(4,
                                                criteria,
                                                lambda x: 1 / x)
    means, npv = mo.normalized_priority_vector(criteria_weights)
    print_matrix(np.hstack([criteria_weights,
                            means[:, np.newaxis],
                            npv[:, np.newaxis]]),
                 columns)
    cons = mo.consistency(criteria_weights, npv, rci)
    print('Overall criteria consistency: {}'.format(round(cons, 3)))

    print('Normal priority matrix:')
    npv_matrix = np.transpose([npv_1, npv_2, npv_3, npv_4])
    print_matrix(npv_matrix)
    print('RESULTS')
    for i, j in zip(names, np.dot(npv_matrix, npv)):
        print(i, format(j, '.3f'), sep='|')