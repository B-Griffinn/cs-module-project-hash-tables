Linked List Collision Solution:

PUT:
Find the hash index
Search the list for the given key,
If given key already exists: simply overwrite / repalce the value of that key
It it's not: append the new record to the list

GET:
Find the hash index
Search list for the given key,
If given key does not exist return None
If it does exist: retrun the value

DELETE:
Find the hash index
Search the list for the given key,
If given key exists, delete node from list
Else: return None
