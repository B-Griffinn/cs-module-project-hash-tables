# Expensive Function using memoization
"""
PLAN
- create a cache that will hold our expensive_seq fn 
- set our base case
- set our key to be a tuple with our 3 inputs
- loop throuh our tuple and check if any of those are in the cache yet
- - if they are not: add to cache
- else: return cache index
"""

cache = {}


def expensive_seq(x, y, z):
    # Your code here
    if x <= 0:
        return y + z
    key = (x, y, z)

    if x > 0:
        if key not in cache:
            cache[key] = expensive_seq(
                x-1, y+1, z) + expensive_seq(x-2, y+2, z*2) + expensive_seq(x-3, y+3, z*3)
    return cache[key]

    # Day 1 APPROACH
    # if x > 0 and x not in cache:
    #     cache[x] = expensive_seq(x-1, y+1, z) + expensive_seq(x-2, y+2, z*2) + \
    #         expensive_seq(x-3, y+3, z*3)

    # return cache[x]


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
