# import the numpy library and give it the alias 'np'
import numpy as np

# create a list of monthly salaries
jeff_salary = [2700, 3000, 3000]
nick_salary = [2600, 2800, 2800]
tom_salary = [2300, 2500, 2500]

# create a numpy array with the salaries above as rows
base_salary1 = np.array([jeff_salary, nick_salary, tom_salary])

# create a list of more monthly salaries
maya_salary = [2200, 2400, 2400]
john_salary = [2500, 2700, 2700]

# create a numpy array with the salaries above as rows
base_salary2 = np.array([maya_salary, john_salary])

# concatenate the base salaries vertically
base_salary = np.concatenate((base_salary1, base_salary2), axis = 0)

# print the base salary array
print(base_salary)

# create a numpy array with the new monthly salaries
new_month_salary = np.array([[3000], [2900], [2500], [2500], [2700]])

# concatenate the new monthly salaries to the base salaries horizontally
base_salary_updated = np.concatenate((base_salary, new_month_salary), axis = 1)

# print the updated base salary array
print(base_salary_updated)

# notes
    # script details concatenating numpy arrays
    # you can not use the addition operator to concatenate numpy arrays
    # axis is used specify whether arrays should be concatenated horizontally or vertically
    # axis zero is the vertical axis and axis one is the horizontal axis