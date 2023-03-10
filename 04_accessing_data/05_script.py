# import the requests library
import requests

# define the parameters for the get request as a dictionary
params = {"bibkeys": "ISBN:1718500521", "format": "json"}

# send a get request to the open library api with the given parameters
response = requests.get("https://openlibrary.org/api/books", params = params)

# print the json response received from the API
print(response.text)

# notes
    # http requests sent by a client are requests and the answer messages returned by the server are responses