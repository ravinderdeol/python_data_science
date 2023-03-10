# import the certifi module that provides mozillas curated collection of root certificates 
import certifi

# import the urllib3 module that allows making http requests in python
import urllib3

# create a pool manager object to manage http connections and specify certificate verification settings
http = urllib3.PoolManager(cert_reqs = "CERT_REQUIRED", ca_certs = certifi.where())

# make a get request to the specified url using the created http object
r = http.request("GET", "https://raw.githubusercontent.com/pythondatabook/sources/main/ch4/excerpt.txt")

# loop through each line in the response text decoding the bytes to utf-8 and split the lines by newline character
for i, line in enumerate(r.data.decode('utf-8').split('\n')):

    # check if the stripped line is not empty
    if line.strip():
        
        # print the line number and the stripped line
        print("line %i: " %(i), line.strip())

# notes
    # urllib3 library is designed to manipulate http requests using thread safe connection pooling minimizing resource needed on your end
    # urllib3 requires more manual work than requests library but it gives you more control over the requests
    # the pool manager instance is how urllib3 makes requests