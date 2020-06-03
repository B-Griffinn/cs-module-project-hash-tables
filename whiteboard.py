# 1:1 whiteboard challenge
# 06-02-2020
"""
Print out all of the numbers in the following array that are divisible by 3:
[85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
The expected output for the above input is:
27
81
9
27
99
63
42
You may use whatever programming language you wish.
Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.
"""

# data type is an arr - we can loop through each index
# we loop thru our arr
# print every index value that can % 3 == 0

arr = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]

for i in range(0, len(arr)-1):
    # print(i)
    if arr[i] % 3 == 0:
        print(arr[i])
