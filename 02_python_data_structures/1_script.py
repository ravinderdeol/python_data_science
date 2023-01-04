# create an empty list
cars = []

# append adds an item to the end of a list
cars.append("ferrari")
cars.append("lamborghini")
cars.append("porsche")
cars.append("bugatti")

# index method returns the index of the first item with a matching value
i = cars.index("porsche")

# insert method inserts an item at the defined index
cars.insert(i, "maserati")

# slice notation and len function to add an item to the first unused index at the end of the list
cars[len(cars):] = ["aston martin"]

# zero index prints the first item in the list
print(cars[0])

# count method returns the number of times a value appears in the list
print(cars.count("ferrari"))

# slice notation to print the first two items in the list
print(cars[0:2])

# notes
    # always consider the best data structure for your data
    # start and end indices in slice notations are optional
    # you can use the slice notation to also remove items from a list