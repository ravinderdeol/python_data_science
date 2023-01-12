list_of_dicts = [
 {
  "name": "photo1.jpg",
  "tags": {'coffee', 'breakfast', 'drink', 'table', 'tableware', 'cup', 'food'}
 },
 {
  "name": "photo2.jpg",
  "tags": {'food', 'dish', 'meat', 'meal', 'tableware', 'dinner', 'vegetable'}
 },
 {
  "name": "photo3.jpg",
  "tags": {'city', 'skyline', 'cityscape', 'skyscraper', 'architecture', 'building', 'travel'}
 },
 {
  "name": "photo4.jpg",
  "tags": {'drink', 'juice', 'glass', 'meal', 'fruit', 'food', 'grapes'}
 }
]

# create an empty dictionary
photo_groups = {}

# loop through the list of dictionaries
for i in range(len(list_of_dicts)):

    # nested loop to go through the list of dictionaries starting from i + 1
    for x in range(i + 1, len(list_of_dicts)):

        # find the intersection of the two tags
        intersection = list_of_dicts[i]['tags'].intersection(list_of_dicts[x]['tags'])

        # if there is an intersection
        if intersection:

            # loop through the intersection
            for tag in intersection:

                # if the tag is not in the photo groups dictionary
                if tag not in photo_groups:

                    # create a new key in the dictionary with the tag and the value of the two names
                    photo_groups[tag] = [list_of_dicts[i]['name'], list_of_dicts[x]['name']]
                
                else:

                    # if the name of the first item is not in the list of values for the tag key
                    if list_of_dicts[i]['name'] not in photo_groups[tag]:

                        # add the name to the list of values for the tag key
                        photo_groups[tag].append(list_of_dicts[i]['name'])

                    # if the name of the second item is not in the list of values for the tag key
                    if list_of_dicts[x]['name'] not in photo_groups[tag]:

                        # add the name to the list of values for the tag key
                        photo_groups[tag].append(list_of_dicts[x]['name'])

# join the key and value from the photo groups dictionary into a string and print it
print('\n'.join([f"{key}: {', '.join(value)}" for key, value in photo_groups.items()]))

# notes
    # this code could be useful for identification and organization of photos and similar items