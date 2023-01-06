text = "python is one of the most promising programming languages today. due to the simplicity of python syntax, many researchers and scientists prefer python over many other languages."

# remove periods and commas from the text string
text = text.replace(".", "").replace(",", "")

# split the text string into a list of words
list = text.split()

# initialize an empty dictionary to store the word counts
dictionary = {}

# iterate over the list of words
for word in list:

    # if the word is not in the dictionary, add it with a count of 0
    count = dictionary.setdefault(word, 0)
    
    # increment the count for the word
    dictionary[word] += 1

# Sort the dictionary by value in descending order
dictionary_sorted = dict(sorted(dictionary.items(), key = lambda x: x[1], reverse = True))

# print the sorted dictionary
print(dictionary_sorted)

# notes
    # the set default method returns a value for a key if it exists otherwise it adds the key value pair to the dictionary
    # the set default method is useful in avoiding overwriting existing values in a dictionary
    # lambda functions are often small and anonymous functions that take any number of arguments but only have one expression