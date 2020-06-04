"""
PLAN
- create global cache for memoization
- check if string is empty - base case
- check if string in cache
- if not, add to cache
- if so, return cache
"""


def no_dups(s):
    # create a cache to quicly create a way to count dupes similar to word count
    count_dupes = {}
    # create a list that will return our original input order without the dupes
    dupe_free = []

    # split our sentence on a space
    split_str = s.split()

    # base case if our input is empty
    if s == "":
        return ""

    # loop thru the sentence word by word
    for i in split_str:
        # if a word is not in the cache
        if i not in count_dupes:
            count_dupes[i] = 1
            dupe_free.append(i)

    return ' '.join(dupe_free)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
