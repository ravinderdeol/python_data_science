import requests

r = requests.get("https://raw.githubusercontent.com/pythondatabook/sources/main/ch4/excerpt.txt")

for i, line in enumerate(r.text.split('\n')):

    # check if the stripped line is not empty
    if line.strip():
        
        # print the line number and the stripped line
        print("line %i: " %(i), line.strip())

# notes
    # requests uses urllib3 under the hood
    # you do not have to manually add query parameters to the url when using the requests library
    # you can pass parameters as a dictionary of strings using the requests library
    # requests automatically decodes the retrieved content making guesses about the encoding