my_list = ["pay bills", "tidy up", "walk the dog", "go to the pharmacy", "cook dinner", "mow the lawn", "water the plants"]

# create an empty list
stack = []

# for loop to append items to the end of the list
for task in my_list:
    stack.append(task)

# while loop to remove items from the end of the list
while stack:
    print(stack.pop(), "- done")

print("\nstack is empty")

# notes
    # a stack is an abstract data structure that follows the lifo principle