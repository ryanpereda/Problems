#  Write a function that takes a paragraph of text as input 
# and returns a dictionary containing the count of each word.

# paragraph = 'a pie dies pie pies 1 12 1'

# print(paragraph)

def word_count(para):
    paragraph_words = para.split()
    paragraph_dictionary = {}
    for word in paragraph_words:
        if word in paragraph_dictionary:
            paragraph_dictionary[word] += 1
        else:
            paragraph_dictionary[word] = 1
    return paragraph_dictionary

# print(word_count(paragraph))