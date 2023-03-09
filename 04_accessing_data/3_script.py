import csv

path = ""

# open function returns a file object which is passed to reader from the csv module
with open(path, "r") as csv_file:

    # dict reader maps the data in each row to a dict using the corresponding headers from the first line as keys
    csv_reader = csv.DictReader(csv_file)


    cars = []
    for row in csv_reader:

        # append the dicts to a list
        cars.append(row)

# prints a list of dictionaries
print(cars)

# notes
    # tabular data files are structured into rows
    # flat files are the most common type of tabular data file
    # flat files are often plain text files, in csv, or tab separated values format with one record per line
    # alternative to the code above would be to turn the csv into a list of lists
    # dict reader and reader methods have an optional delimiter parameter to specify the character that separates fields which is a comma by default