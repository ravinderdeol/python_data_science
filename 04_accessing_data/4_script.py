# import the csv and json modules
import csv
import json

# set the file path of the input csv file
path = ""

# open the csv file and return a file object which is passed to the csv modules dict reader function
# this creates a csv reader object that maps data in each row to a dict using the corresponding headers as keys
with open(path, "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # create an empty list to hold dicts of car data
    cars = []

    # iterate over each row in the csv reader object and append the resulting dict to the cars list
    for row in csv_reader:
        cars.append(row)

# open the output json file in write mode and dump the cars list to JSON format
with open("", "w") as json_file:
    json.dump(cars, json_file)

# open the json file in read mode and parse its contents as a json object which is stored in records
with open("", "r") as json_file:
    records = json.load(json_file)

    # iterate over each record in the json array and print the relevant data to the console
    for record in records:
        print(f"year: {record['year']}\nmake: {record[' make'].strip()}\nmodel: {record[' model']}\nprice: {record[' price'].strip()}\n")

# notes
    # script to read a csv file and writes data to a json file then prints it to the console