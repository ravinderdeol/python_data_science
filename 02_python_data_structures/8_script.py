# initialize sets of tags for two photos
photo1_tags = {"coffee", "breakfast", "drink", "table", "tableware", "cup", "food"}
photo2_tags = {"food", "dish", "meat", "meal", "tableware", "dinner", "vegetable"}

# find the intersection of the two sets of tags
intersection = photo1_tags.intersection(photo2_tags)

# if there are two or more tags in the intersection join them and print a message
if len(intersection) >= 2:
    intersection_tags = ", ".join(intersection)
    print(f"the photos contain similar objects: {intersection_tags}.")

# notes
    # the intersection method is a set method that returns a new set with elements that are common to both sets