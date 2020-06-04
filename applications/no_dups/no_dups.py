"""
PLAN
- create global cache for memoization
- check if string is empty - base case
- check if string in cache
- if not, add to cache
- if so, return cache
"""


def no_dups(s):
    dupes_cache = {}

    # create a var for our non_dupes cache
    non_dupes = []

    # split our input
    split_sentence = s.split()
    # print(split_sentence)

    # base case if input is empty
    if s == "":
        return ""

    # loop throuh our split sentence var
    for i in split_sentence:
        # check if our index is not in the cache yet
        # if not in, add it
        # then append that item to our list which avoids dupes bc we never get here in index is in cache
        if i not in dupes_cache:
            dupes_cache[i] = 1
            non_dupes.append(i)

    # GOTCHA we needed to join our sentenct back with a space
    return ' '.join(non_dupes)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
