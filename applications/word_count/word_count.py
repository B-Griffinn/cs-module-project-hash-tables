def word_count(s):
    # create local cache dict
    cache = {}

    # create a list of all our unwanted chars
    ignore = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\',
                   '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']

    # convert list into str using the join method
    ignore_chars = ''.join(ignore)

    # translate our stringusing maketrans --> creates a 1:1 relationship for all vals
    tr = s.maketrans('', '', ignore_chars)

    # create new var to translate our translation map --> lower case and split that new str so we can loop thru below
    new_s = s.translate(tr).lower().split()

    # split our str and assign it to a var
    # split_str = s.split()
    # print('SPLIT', split_str)

    # loop thru the split str
    for i in new_s:
        # lowercase our items for output
        i = i.lower()
        # check if that word is in our cache
        if i in cache:
            # if so add 1 to the cache index
            cache[i] += 1
        # otherwise cache index = 1 bc this is the first time seeing it
        else:
            cache[i] = 1

    # create a new list out of our dict.items() and assign to var
    items = list(cache.items())

    # take that list and sort it by preference
    items.sort(key=lambda e: e[1])

    return cache


if __name__ == "__main__":
    # print(word_count(""))
    # print(word_count("Hello"))
    # print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))

    print(word_count('Hello, my cat.  And my cat doesn\'t say "hello" back.'))


"""
DAY ! Attempt:
def word_count(s):
    # create local cache dict
    cache = {}

    # ignored vars
    ignore_vars = list(" \" : ; , . - + = / \ | [ ] { } ( ) * ^ & \' ")
    print(ignore_vars)
    
    if s == "":
        return {}

    # split our str and assign it to a var
    split_str = s.split()

    # loop thru the split str
    for i in split_str:
        # # check last element in index to be False and then remove from str
        for j in i:
            if j in ignore_vars:
                # print("J", j)
                i = i.replace(j, "")
                print("IVVVVVV", i)
        # lowercase our items for output
        i = i.lower()
        # check if that word is in our cache
        if i in cache:
            # if so add 1 to the cache index
            cache[i] += 1
        # otherwise cache index = 1 bc this is the first time seeing it
        else:
            cache[i] = 1

    # create a new list out of our dict.items() and assign to var
    items = list(cache.items())

    # take that list and sort it by preference
    items.sort(key=lambda e: e[1])

    return cache


APPROACH #2 


    to_delete = '" : ; , . - + = / \ | [ ] { } ( ) * \' ^ &'

    tr = s.maketrans('', '', to_delete)
    new_s = s.translate(tr).lower()
    print("SSSSSSSSSSS", new_s)

    # split our str and assign it to a var
    split_str = s.split()
    print('SPLIT', split_str)

"""
