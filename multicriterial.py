import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def to_restrictions(weights, restrictions):
    """Returns indices of viable alternatives
    in order based on main criteria"""
    assert 1. in restrictions, "There is no main criteria"
    main = np.where(restrictions == 1.)
    assert len(main), "There could only be one main criteria"
    maxes = np.max(np.transpose(weights), axis=1)
    indicators = np.array([w >= restrictions * maxes for w in weights.astype(float)])
    indicators[:, main] = True
    return np.flatnonzero(np.all(indicators, axis=1))


def manhattan_dist(s_point, f_point):
    return abs(s_point[0] - f_point[0]) + abs(s_point[1] - f_point[1])


def pareto_set(weights, criteria, utopia, cr_names, names):
    """Plots Pareto set, computes distances and returns index of best solution"""
    assert len(criteria) == 2, "There should only be 2 criteria"
    points = weights[:, criteria]
    dist = [manhattan_dist(point, utopia) for point in points]
    x, y = np.transpose(points)
    colors = np.random.rand(len(x))
    plt.title('Pareto set')
    plt.scatter(x, y, c=colors)
    for i, label in enumerate(names):
        plt.annotate(label, (x[i], y[i]))
    plt.scatter(*utopia, c='red')
    plt.annotate('U. point', utopia)
    plt.xticks(np.arange(0, 11))
    plt.yticks(np.arange(0, 11))
    if cr_names is None:
        names = ['x', 'y']
    plt.xlabel(names[0])
    plt.ylabel(names[1])
    plt.grid(linestyle='--')
    plt.savefig('pareto.png')
    return dist


def create_weights_matrix(amount, pairwise_comparisons, inv_function):
    result = [[1. for _ in range(amount)] for _ in range(amount)]
    offset = 0
    for i in range(amount - 1):
        j = amount - 1 - i
        straight = pairwise_comparisons[offset:offset + j]
        result[i][i + 1:] = straight
        mirrored = [inv_function(elem) for elem in straight[::-1]]
        result[j][:j] = mirrored
        offset += j
    return result


def normalized_priority_vector(matrix):
    geometric_means = np.array([np.prod(row) ** (1. / len(matrix)) for row in matrix])
    geometric_means_sum = np.sum(geometric_means)
    return geometric_means, geometric_means / geometric_means_sum


def consistency(matrix, npv, rci):
    column_sums = np.sum(np.transpose(matrix), axis=1)
    own_value = sum(np.multiply(column_sums, npv))
    cons_i = (own_value - len(npv)) / (len(npv) - 1)
    return cons_i / rci