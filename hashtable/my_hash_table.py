# Plan
# 1. initiaite our class
# 2.

# Hash Class


class HashTable(object):
    def __init__(self, length=4):
        # initiate our arr with None values
        self.array = [None] * length

    # 001 HASH an index for the incoming data
    def hashing_function(self, s):
        # encode our input into an integer
        string_bytes = s.encode()

        # prepare to count bytes
        total = 0

        # loop thru the string bytes
        for i in string_bytes:
            # increment total per str.byte
            total += i
        # returning the index of where our hash value
        return total % len(self.array)

    # 002 SET the hashed value in its correct index
    def set_data(self, key, value):
        # use our hashing fucntion above to assing index to a var
        index = self.hashing_function(value)

        # check if the arr[index] is none. if it is none then the index has not been taken
        if self.array[index] is not None:
            # this means our index is taken and we now check our key already exists
            # loop thru the index we are given above
            for kvp in self.array[index]:
                # if key is found, then update its curr value to the new val
                if kvp[0] == key:
                    kvp[1] = value
                    break
            else:
                # otherwise add key to end
                self.array[index].append((key, value))
        else:
            # this index is empty so we can initiate a list and append the key/value to it
            self.array[index] = []
            self.array[index].append((key, value))

    def get_value_by_key(self, key):
        index = self.hashing_function(key)

        if self.array[index] is None:
            raise KeyError()
        else:
            # loop thru all key / val pairs and find if our key exists
            # if it exists return its value
            for kvp in self.array[index]:
                if kvp[0] == key:
                    return kvp[1]

            # if no return was done in our loop then our key doesnt exists
            print("Key does not exist")


#### TESTS ####
#  Testing my hashing_function()
hasht = HashTable(4)
# x = hasht.hashing_function("ben")
# print('Hashed str', x)

hasht.set_data(2, "ben")
print(hasht.array)
