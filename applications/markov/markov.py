import random

# 1. Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    split_words = words.split()
    # print(split_words, end=" ")

# TODO: analyze which words can follow other words
# Your code here
""" 
POPULAR WORDS in TXT file
kitten
the
little
sleep
day
"""

# build a list for words that can follow other words
words_that_follow = "kitten the little sleep day"
split_follow_words = words_that_follow.split()
# print(split_follow_words)

start_word = random.choice(split_words)
# print(type(start_word))
# print(start_word[0])
if start_word[0].isupper() == True:
    print(start_word[0])
# print("START WORD", start_word)


# TODO: construct 5 random sentences
# Your code here
