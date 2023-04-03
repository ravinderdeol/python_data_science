import redis

# values to default to localhost when they are not specified
r = redis.Redis()

# create a dictionary with the key value pairs to be stored in the hash
cabDict = {"id": "cab48", "driver": "dan varsky", "brand": "volvo"}

# use the hset method to set the key value pairs in the hash
for key, value in cabDict.items():
    r.hset("cab48", key, value)

# use the hgetall method to retrieve all the key value pairs in the hash
get_cabdict = r.hgetall("cab48")

# prints the dictionary
print(get_cabdict)

# notes
    # script store multiple pieces of information about the same object using redis
    # the h in hset stands for hash