with open('robin.txt', 'r') as f:
    read_file = f.read()
    split_file = read_file.split()

    # print(split_file)

# the = []
# for i in split_file:
#     i.lower()
#     if i == "the":
#         the.append('#')

# print(''.join(the))


""" 
- implement a word count function 
- include ignored values
- sort twice:
-- sort by num of words
-- then sort alpha
- The hash marks should be left justified two spaces after the longest word.
- Case should be ignored, and all output forced to lowercase.
- BASE CASE: If the input contains no ignored characters, print nothing.
"""


def histogram(s):
    # create local cache dict
    cache = {}

    histogram = {}

    # create list to ignore all of our unwanted chars
    ignore = ['"', ':', ';', ',', '.', '-', '+', '=', '/',
              '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']

    # convert ignore chars list into a str using the join method
    ignore_joined = ''.join(ignore)

    # translate our ignore string using maketrans
    tr = s.maketrans('', '', ignore_joined)

    # create a new var to translate our maketrans map
    new_s = s.translate(tr).lower().split()

    # loop thru our robin file aka s
    for i in new_s:
        # check if its already in cache
        if i in cache:
            # if it is already in then we increment that key count to 1
            cache[i] += 1
            histogram.update({cache[i]: '#'})
            # print(f"HERE {i}......{cache[i] * '#'}")
        # othwerwise we want to set the count to be 1 on that index since this is the first we have seen it.
        else:
            cache[i] = 1
            histogram.update({cache[i]: '#'})

    # create a new list out of our dict.items() and assign to var
    items = list(cache.items())

    # TODO i need a function that can be passed to sort that will allow me to

    # take that list and sort it by preference
    # SORT BY ALPHA
    items.sort(key=lambda e: e[0])
    items.sort(reverse=True, key=lambda e: e[1])

    # once
    for j in cache:
        print(f"   {cache[j] * '#'}")

    # return f"\nItems: {items}\n"
    return 'End'


if __name__ == "__main__":
    #     print(histogram(""))
    #     print(histogram("Hello"))
    #     print(histogram('Hello, my cat. And my cat doesn\'t say "hello" back.'))

    print(histogram(
        'Hello, Hello Hello Hello Hello Hello Hello my cat.  And my cat doesn\'t say "hello" back.'))

# joined = ' '.join(split_file)
# # print(type(joined))
# print(histogram(joined))
