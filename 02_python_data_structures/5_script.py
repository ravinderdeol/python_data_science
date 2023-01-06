task_list = ["pay bills", "tidy up", "walk the dog", "go to the pharmacy", "cook dinner"]

time_list = ["08:00", "08:30", "09:30", "10:00", "10:30"]

# create a list of tuples containing the time and task for each scheduled event 
scheduled_list = [(time, task) for time, task in zip(time_list, task_list)]

# print the time of the second scheduled event
print(scheduled_list[1][0])

# print the task of the second scheduled event
print(scheduled_list[1][1])

# notes
    # tuples are immutable
    # the zip function takes two or more iterables and returns an iterator of tuples
    # tuples are useful for storing data that represent real-world objects like car information