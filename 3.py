'''
Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170

Рост матерей  178, 165, 165, 173, 168, 155, 160, 164, 178, 175

Используя эти данные построить 95% доверительный интервал для разности среднего роста родителей и детей.
'''


import numpy as np
from scipy import stats
mothers = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])
daughters = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])

difference_of_means = np.mean(mothers) - np.mean(daughters)
standard_error = np.sqrt(np.var(mothers, ddof=1)/len(mothers) + np.var(daughters, ddof=1)/len(daughters))
t_critical = stats.t.ppf(0.975, len(mothers) + len(daughters) - 2)
left_border = round(difference_of_means - t_critical * standard_error, 2)
right_border = round(difference_of_means + t_critical * standard_error, 2)

print(f'95% доверительный интервал для разности среднего роста родителей и детей: [{left_border}, {right_border}]')