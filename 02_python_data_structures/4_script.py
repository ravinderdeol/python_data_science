import spacy

# store a string of text in a variable
text = "list is a ubiquitous data structure in the python programming language"

# load the english language model
nlp = spacy.load("en_core_web_sm")

# process the text with the model
doc = nlp(text)

# create a list of noun chunks from the document
noun_chunks = [chunk.text for chunk in doc.noun_chunks]

# use a generator expression to print each noun chunk on a separate line
print(*(chunk for chunk in doc.noun_chunks), sep='\n')

# notes
    # the code creates a list of noun chunks from the input text
    # refer to the spacy documentation for more information at spacy.io/api/doc
    # useful for varios nlp tasks such as information extraction and summarization