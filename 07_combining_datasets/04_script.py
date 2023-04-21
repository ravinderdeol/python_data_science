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

# appends a tuple containing five values to details
details.append((4626592, "Shorts", "Protest", 48.0, 1))

# creates a list called order details using a nested list comprehension
# iterates over the details list and for each item checks if the first element (is in the first element of any of the orders items
# appends matching order item to the order details list followed by the remaining elements of the details item
order_details = [[o for o in orders if d[0] in o][0] + d[1:] for d in details if d[0] in [o[0] for o in orders]]

# creates a new list called orders details right similar to the order details list
# if no matching order item is found it adds a new tuple with the first element of the details item and none values for other elements
orders_details_right = [[o for o in orders if d[0] in o][0] + d[1:] if d[0] in [o[0] for o in orders] else (d[0], None, None) + d[1:] for d in details]

# calculates total cost of orders in orders details right
# uses a generator expression to multiply the price and quantity for each order item then adds the results using sum
print(sum(pr*qt for _, _, _, _, _, pr, qt in orders_details_right))

# notes
    # example script of implementing different types of joins for lists