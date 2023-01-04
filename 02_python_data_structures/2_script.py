# completed tasks drop off at the beginning while new tasks are added at the end
from collections import deque

my_list = ["pay bills", "tidy up", "walk the dog", "go to the pharmacy", "cook dinner", "mow the lawn", "water the plants"]

# convert the list into a deque object
queue = deque(my_list)

# add a new element to the end of the queue
queue.append("wash the car")

# removes the first element from the queue and returns it
print(queue.popleft(), " - Done")

# convert the deque object back into a list
my_list_updated = list(queue)

print(my_list_updated)

# notes
    # deque stands for double-ended queue
    # deque simulates a queue thus following the fifo principle