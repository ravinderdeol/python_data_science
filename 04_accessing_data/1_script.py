# specify the path to the file
path = ""

# pass the path to the open function in read only mode which returns a file object
with open(path, "r") as f:
    
    # use the read method of the file object to read the contents of the file
    content = f.read()

print(content)

# notes
    # accessing data is the first step of data analysis
    # text files are a sequence of string objects to python
    # by default the open function opens a file in read only mode
    # using the open function ensures the file is closed after it is read