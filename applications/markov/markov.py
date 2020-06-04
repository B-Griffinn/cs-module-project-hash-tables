import random

# 1. Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    split_words = words.split()
    # print(split_words, end=" ")

# 2. TODO: analyze which words can follow other words
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
words_that_follow = '"kitten?" The. Little" sleep!" day!'

# split the words_that_follow in order to check a list
split_this = words_that_follow.split()
# test_list = random.choice(split_this)


# Create a start word at random from our split_words list
word_list = random.choice(split_words)

# create vars for start and stop words
start = ""
stop = ""

# check which words are start words
if (word_list[0].isupper() == True) or (word_list[0] == '\"'):
    start = word_list
    # print('START', start)


stop_puncs = ['.', '?', '!', '"', '."', '?"', '!"']
if (word_list[-1] in stop_puncs):
    stop = word_list
    # print('STOP', stop)

# TODO: construct 5 random sentences
# Your code here
for i in word_list:
    if i is start:
        print(f"{start} {random.choice(split_words)} {random.choice(split_words)} {random.choice(split_words)} {random.choice(split_words)} {random.choice(split_words)} {random.choice(split_words)} {random.choice(split_words)} {random.choice(split_words)} {random.choice(split_words)}")
        print(f"{start} {random.choice(split_words)} {random.choice(split_words)} {random.choice(split_words)} {random.choice(split_words)} {random.choice(split_words)} {random.choice(split_words)} {random.choice(split_words)} {random.choice(split_words)} {random.choice(split_words)}")
        print(f"{start} {random.choice(split_words)} {random.choice(split_words)} {random.choice(split_words)} {random.choice(split_words)} {random.choice(split_words)} {random.choice(split_words)} {random.choice(split_words)} {random.choice(split_words)} {random.choice(split_words)}")
        print(f"{start} {random.choice(split_words)} {random.choice(split_words)} {random.choice(split_words)} {random.choice(split_words)} {random.choice(split_words)} {random.choice(split_words)} {random.choice(split_words)} {random.choice(split_words)} {random.choice(split_words)}")
        print(f"{start} {random.choice(split_words)} {random.choice(split_words)} {random.choice(split_words)} {random.choice(split_words)} {random.choice(split_words)} {random.choice(split_words)} {random.choice(split_words)} {random.choice(split_words)} {random.choice(split_words)}")
    else:
        break
