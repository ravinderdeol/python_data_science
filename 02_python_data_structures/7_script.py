customers = ["john silver", "tim jemison", "john silver", "maya smith"]

# create a new list of unique customers sorted by their original order
list = list(sorted(set(customers), key = customers.index))

print(list)

# notes
    # duplicate elements are not allowed in sets
    # sets are unordered collections of unique elements
    # using set alone does not preserve the order of the elements