import json

# import the certifi module that provides mozillas curated collection of root certificates 
import certifi

# import the urllib3 module that allows making http requests in python
import urllib3

# create a pool manager object to manage http connections and specify certificate verification settings
http = urllib3.PoolManager(cert_reqs = "CERT_REQUIRED", ca_certs = certifi.where())

# make a get request to the news api url defining the search query, api key, and page size parameters
r = http.request("GET", "https://newsapi.org/v2/everything?q=ferrari&apiKey=your_api_key_here&pageSize=5")

articles = json.loads(r.data.decode("utf-8"))

for article in articles["articles"]:
    print(article["title"])
    print(article["publishedAt"])
    print(article["url"])
    print()

# notes
    # integrating the news api into a python application using direct http requests via the urllib3 library
    # an alternative but unofficial python client library can be found at newsapi.org/docs/client-libraries/python