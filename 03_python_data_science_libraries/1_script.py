# import the numpy library as np
import numpy as np

# define a list of salaries for employees
employee_one_salary = [2700, 3000, 3000]
employee_two_salary = [2600, 2800, 2800]
employee_three_salary = [2300, 2500, 2500]

# define a list of bonuses for employees
employee_one_bonus = [500, 400, 400]
employee_two_bonus = [600, 300, 400]
employee_three_bonus = [200, 500, 340]

# convert the lists into numpy arrays
salary = np.array([employee_one_salary, employee_two_salary, employee_three_salary])
bonus = np.array([employee_one_bonus, employee_two_bonus, employee_three_bonus])

# perform element-wise addition operation on the arrays
salary_bonus = salary + bonus

print(salary)
print(bonus)

print(salary_bonus)

# find the maximum value in the 'salary bonus' array
print(salary_bonus.max())

# find the maximum value in each row horizontally in the 'salary bonus' array
print(np.amax(salary_bonus, axis = 1))

# notes
    # numpy is useful when working with arrays