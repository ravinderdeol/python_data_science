orders_2022_02_04 = [
    (9423517, "2022-02-04", 9001),
    (4626232, "2022-02-04", 9003),
    (9423534, "2022-02-04", 9001)
]

orders_2022_02_05 = [
    (9423679, "2022-02-05", 9002),
    (4626377, "2022-02-05", 9003),
    (4626412, "2022-02-05", 9004)
]

orders_2022_02_06 = [
    (9423783, "2022-02-06", 9002),
    (4626490, "2022-02-06", 9004)
]

# combine lists into a single list using the addition operator
orders = orders_2022_02_04 + orders_2022_02_05 + orders_2022_02_06

print(orders)

# notes
    # easiest way to combine two or more lists or tuples is by using the addition operator
    # works well when you need to put elements from the structures being combined into a single new structure without changes
    # the process in this script is often called concatenation