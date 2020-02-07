from collections import *
def word_count(file_name):
    with open(file_name) as f:
        return Counter(f.read().split())
print("The number of words in the given file is:",word_count("text.txt"))