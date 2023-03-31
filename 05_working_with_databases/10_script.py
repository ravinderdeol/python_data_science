import redis

# values to default to localhost when they are not specified
r = redis.Redis()

# mset method is used to set multiple key value pairs
multiple_set = r.mset({"emp1": "maya silver", "emp2": "john jamison"})

# get method is used to retrieve the value of a key
single_get = r.get("emp1")

# multiple set print statement equals true if the operation was successful
print(multiple_set)

# prints the value of the key
print(single_get)

# notes
    # simple script to access the redis server from python
    # no sql databases do not require predetermined organizational schemas for data being stored
    # flexibility of no sql databases are well suited to real time and big data applications
    # good example of a key value store is redis which stands for remote dictionary service
    # the m in mset stands for multiple