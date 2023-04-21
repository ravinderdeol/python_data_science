# list of tuples containing the order details
orders = [
    (9423517, '2022-02-04', 9001),
    (4626232, '2022-02-04', 9003),
    (9423534, '2022-02-04', 9001),
    (9423679, '2022-02-05', 9002),
    (4626377, '2022-02-05', 9003),
    (4626412, '2022-02-05', 9004),
    (9423783, '2022-02-06', 9002),
    (4626490, '2022-02-06', 9004)
]

# list of tuples containing order details
details = [
    (9423517, "Jeans", "Rip Curl", 87.0, 1),
    (9423517, "Jacket", "The North Face", 112.0, 1),
    (4626232, "Socks", "Vans", 15.0, 1),
    (4626232, "Jeans", "Quiksilver", 82.0, 1),
    (9423534, "Socks", "DC", 10.0, 2),
    (9423534, "Socks", "Quiksilver", 12.0, 2),
    (9423679, "T-shirt", "Patagonia", 35.0, 1),
    (4626377, "Hoody", "Animal", 44.0, 1),
    (4626377, "Cargo Shorts", "Animal", 38.0, 1),
    (4626412, "Shirt", "Volcom", 78.0, 1),
    (9423783, "Boxer Shorts", "Superdry", 30.0, 2),
    (9423783, "Shorts", "Globe", 26.0, 1),
    (4626490, "Cargo Shorts", "Billabong", 54.0, 1),
    (4626490, "Sweater", "Dickies", 56.0, 1)
]

# create an empty list to store the merged tuples
orders_details = []

# nested pair of for loops to iterate over the lists
for o in orders:
    for d in details:

        # conditional statement to merge tuples with matching order numbers
        if d[0] == o[0]:

            # use slicing to avoid repeating the order number in merged tuples
            orders_details.append(o + d[1:])

# print the merged tuples
print(orders_details)

# notes
    # script to find tuples with matching order numbers and merge them into a single tuple storing them in a new list
    # one line alternative to the nested for loop 'order_details = [[o for o in orders if d[0] == o[0]][o] + d[1:] for d in details]'