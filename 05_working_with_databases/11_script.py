import redis
from datetime import timedelta

# values to default to localhost when they are not specified
r = redis.Redis()

# use the setex method to set a key value pair with an expiry time after which the key value pair is deleted
set_setex = r.setex("cab26", timedelta(minutes = 1), value = "in the area now")

# prints true if the operation was successful
print(set_setex)

# get method is used to retrieve the value of a key
get_setex = r.get("cab26")

# prints the value of the key
print(get_setex)

# notes
    # redis script to insert and set an expiry time for a key value pair
    # the setex method is used to set a key value pair with an expiry time