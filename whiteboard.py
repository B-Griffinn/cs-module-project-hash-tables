'''
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
'''

# Add up and print the sum of the all of the minimum elements of each inner array. Each array may contain additional arrays nested arbitrarily deep, in which case the minimum value for the nested array should be added to the total.
# [
#   [8, [4]],
#   [[90, 91], -1, 3],
#   [9, 62],
#   [[-7, -1, [-56, [-6]]]],
#   [201],
#   [[76, 0], 18],
# ]
# The expected output for the above input is:
# 8 + 4 + 90 + -1 + 9 + -7 + -56 + -6 + 201 + 0 + 18 = 260
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.


array = [
    [8, [4]],
    [[90, 91], -1, 3],
    [9, 62],
    [[-7, -1, [-56, [-6]]]],
    [201],
    [[76, 0], 18],
]

for i in array:
    print(i)

# we need to loop thru the entire list `array`
# ??? we need to somehow check if we are still in a nested for loop before finding the min value ???

# for i in array:
    # i == each index which is truly another list that may or may not hold a nested list...
    # how do I check if my index has a nested list?
