from collections import Counter
import re

#Create a function that take a txt as a string and count the characters
def count_words(fname):
    words = fname.split()
    return len(words)

def count_char(fname):

    #Clean the text from punctuation and spaces
    cleaned_text = re.sub(r'[^a-zA-Z]', '', fname)
    # Convert the text to lowercase to avoid duplicates and filter only alphabetic characters
    fname = cleaned_text.lower()
    # Count all characters, including punctuation and spaces
    character_counts = Counter(fname)
    return dict(character_counts)

def report(file_name, fname):

    file_reported = file_name[2:]
    words_in_doc = count_words(fname)
    char_in_doc = count_char(content)

    print(f"--- Begin report of {file_reported} ---")
    print(f"{words_in_doc} words found in the document\n")

    for c in char_in_doc:
        print(f"The '{c}' character was found {char_in_doc[c]} times")
    print("--- End report ---")

# Specify the file name (or path if it's not in the same directory)
file_name = "./books/frankenstein.txt"

# Open the file in read mode
try:
    with open(file_name, 'r') as file:
        # Read the content of the file
        content = file.read()
        # Print the content
        #print(content)
        #Call function to count words
        #count_words(content)
        #Call function to count chars
        #count_char(content)
        #Call function to report
        report(file_name, content)

except FileNotFoundError:
    print(f"The file '{file_name}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")