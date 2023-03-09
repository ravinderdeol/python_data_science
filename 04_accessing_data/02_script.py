# specify the path to the file
path = ""

# pass the path to the open function in read only mode which returns a file object
with open(path, "r") as f:
    
    # add line numbers to each line of the file with the enumerate function
    for i, line in enumerate(f):

        # filter out the empty lines using the strip method
        if line.strip():
            
            print(f"line {i}: {line.strip()}")

# notes
    # this code will print only the non-empty lines of the file