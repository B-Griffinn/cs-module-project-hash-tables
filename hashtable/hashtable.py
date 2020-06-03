class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f"self.key {self.key},  self.value {self.value}, self.next {self.next }"


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        r = ""
        cur = self.head

        while cur is not None:
            r += f"({cur.value})"

            if cur.next is not None:
                r += '~~ >'
            cur = cur.next
        return r


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        # Your code here
        # initiate our table with an array
        self.capacity = capacity
        # UPDATE OUR STORAGE, HASH TABLE, LIST TO BE MADE UP OF A LL
        # self.array = [LinkedList()] * capacity
        self.array = [None] * capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.array)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1.
        Some insight into the magic numbers 5381 and 33:
        https://stackoverflow.com/questions/1579721/why-are-5381-and-33-so-important-in-the-djb2-algorithm
        """

        hashed = 5381

        for byte in key.encode():
            hashed = ((hashed << 5) + hashed) + byte
            # this ^^^ is an optimized version of: hashed = hashed * 33 + byte
            hashed &= 0xffffffff

        return hashed

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        """

        hash_value = self.djb2(key)
        # return self.fnv1(key) % self.capacity
        return hash_value % len(self.array)

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """

        # Your NAIVE code here
        # slot = self.hash_index(key)
        # self.array[slot] = HashTableEntry(key, value)

        # Find the hash index
        index = self.hash_index(key)

        if self.array[index] == None:
            # set empty arr
            self.array[index] = []
            # print("self.array[index]", self.array[index])
        self.array[index].append([key, value])
        # print("AFTER", self.array[index])

        for i in range(0, len(self.array[index])):
            if self.array[index][i][0] == key:
                self.array[index][i][1] = value

        return index

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # find the hash index
        index = self.hash_index(key)

        # store our var out of loop before effecting it
        delete_me = []

        if self.array[index] == None:
            return None

        for i in range(0, len(self.array[index])):
            for i in self.array[index]:
                # if self.array[index][j][0] == key:
                delete_me.append(i)

        self.array.remove(delete_me)

        print('DELETE ME')

        # Your code here
        # self.put(key, None)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """

        # find the hash index / HASH THE KEY
        index = self.hash_index(key)

        if self.array[index]:
            for i in range(0, len(self.array[index])):
                if self.array[index][i][0] == key:
                    return self.array[index][i][1]
        return None

        # # find the key index
        # hash_entry = self.array[index]

        # DAY 1
        # slot = self.hash_index(key)
        # hash_entry = self.array[slot]

        # # check if hash entry is present in hash list
        # if hash_entry is not None:
        #     return hash_entry.value

        # # if hash_entry does not exists return none
        # return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here


ht = HashTable(10)
print("PUT return", ht.put("dogs", "are cool"))
print("PUT return", ht.put("hello world", "goodbye!!"))
print("PUT return", ht.put("cats", "are fine"))
print("PUT return", ht.put("i love", "pizza"))
print("PUT return", ht.put("hello", "ben"))

print('GET', ht.get("hello"))

print('GET', ht.get("cats"))
print("DEL", ht.delete("cats"))
print('GET', ht.get("cats"))


# if __name__ == "__main__":
#     ht = HashTable(8)

#     ht.put("line_1", "'Twas brillig, and the slithy toves")
#     ht.put("line_2", "Did gyre and gimble in the wabe:")
#     ht.put("line_3", "All mimsy were the borogoves,")
#     ht.put("line_4", "And the mome raths outgrabe.")
#     ht.put("line_5", '"Beware the Jabberwock, my son!')
#     ht.put("line_6", "The jaws that bite, the claws that catch!")
#     ht.put("line_7", "Beware the Jubjub bird, and shun")
#     ht.put("line_8", 'The frumious Bandersnatch!"')
#     ht.put("line_9", "He took his vorpal sword in hand;")
#     ht.put("line_10", "Long time the manxome foe he sought--")
#     ht.put("line_11", "So rested he by the Tumtum tree")
#     ht.put("line_12", "And stood awhile in thought.")

#     print("")

#     # Test storing beyond capacity
#     for i in range(1, 13):
#         print(ht.get(f"line_{i}"))

#     # Test resizing
#     old_capacity = ht.get_num_slots()
#     ht.resize(ht.capacity * 2)
#     new_capacity = ht.get_num_slots()

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     for i in range(1, 13):
#         print(ht.get(f"line_{i}"))

#     print("")


"""
PUT approach


Store the value with the given key.
Hash collisions should be handled with Linked List Chaining.
Implement this.

        # Search the list for the given key,
        # hash_entry = self.array[index]
        # print('hash_entry', hash_entry)
        # DAY 2 approach
        # # check if index is empty set a new LL add a new node and make it the head of index
        # if hash_entry == None:
        #     hash_entry = LinkedList()
        #     # print('newLL', new_ll)
        #     new_node = HashTableEntry(key, value)
        #     # print("new_node", new_node)
        #     hash_entry = new_node
        #     # print("NEW LL", new_ll)
        #     hash_entry.head = new_node
        #     new_node.next = None
        #     print("asfadsfdsafaf", hash_entry)
        #     # print("new_node.next", new_node.next)
        # # if our index == key: we want to update our value with value
        # elif hash_entry == key:
        #     self.array[index].value = value

        # return index


GET approach:

        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.

        # find the hash index
        index = self.hash_index(key)

        # hash_entry is our index in the arr that our key is mapped to
        hash_entry = self.array[index]

        # If it does exist: retrun the value
        if hash_entry == key:
            for i in range(0, len(self.array) - 1):
                if hash_entry[index][i][0] == key:
                    return hash_entry[index][i][1]
        if hash_entry != key:
            return None

"""
