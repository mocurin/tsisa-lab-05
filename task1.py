import multicriterial as mo
import numpy as np

# Вузы
# А. Oxford
# В. МГУ
# С. МФТИ
# D. ТГУ

# Критерии
# 1. Размер стипендии
# 2. Квалификация преподавателей
# 3. Стоимость жизни в городе
# 4. Престижность диплома

if __name__ == '__main__':
    names = np.array(list('ABCD'))
    criteria_weights = np.array([2, 6, 8, 4])
    criteria_weights = np.divide(criteria_weights, np.sum(criteria_weights))
    criteria_matrix = np.array([[0, 9, 1, 9],
                                [9, 7, 3, 7],
                                [5, 5, 5, 5],
                                [3, 3, 9, 3]])
    lower_thresholds = np.array([0.4, 0.6, 0.3, 1])
    indices = mo.to_restrictions(criteria_matrix, lower_thresholds)

    # Report
    print('TASK 1')
    print('CRITERIA WEIGHTS:')
    print(np.round(criteria_weights, 2))
    print('CRITERIA_THRESHOLDS:')
    print(lower_thresholds)
    print('CRITERIA MATRIX:')
    for i, row in zip(names, criteria_matrix):
        print(str(i), *row, sep=' | ')
    print('VIABLE VARIANTS')
    for i, row in zip(names[indices], criteria_matrix[indices]):
        print(str(i), *row, sep=' | ')
