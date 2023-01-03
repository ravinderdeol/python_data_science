text = "Eight dollars a week or a million a year - what is the difference? A mathematician or a wit would give you the wrong answer. The magi brought valuable gifts, but that was not among them. - The Gift of the Magi, O'Henry"

# 'w' loop splits sentences into words and stores them within the larger list 
# 'text' loop splits text into sentences and stores them in a list
word_list = [[w.replace(",","") for w in line.split() if w not in ["-"]] for line in text.replace("?",".").split('.')]

print(word_list)

# notes
    # the three categories of data are unstructured, semi-structured, and structured
    # the data processing pipeline steps are acquisition, cleaning, transformation, analysis, and storage