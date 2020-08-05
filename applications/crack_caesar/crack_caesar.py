# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

# hash table as a map between data values

# GOATS ~~>  JEHFN

encode_table = {
    'A': 'H',
    'B': 'Z',
    'C': 'Y',
    'D': 'W',
    'E': 'O',
    'F': 'R',
    'G': 'J',
    'H': 'D',
    'I': 'P',
    'J': 'T',
    'K': 'I',
    'L': 'G',
    'M': 'L',
    'N': 'C',
    'O': 'E',
    'P': 'X',
    'Q': 'K',
    'R': 'U',
    'S': 'N',
    'T': 'F',
    'U': 'A',
    'V': 'M',
    'W': 'B',
    'X': 'Q',
    'Y': 'V',
    'Z': 'S'
}


def encode(s):
    result = ""

    for i in s:
        result += encode_table[i]

    return result


decode_table = {}

for k, v in encode_table.items():
    decode_table[v] = k


def decode(s):
    r = ""

    for c in s:
        r += decode_table[c]

    return r


print(encode("GOATS"))
print(decode("JEHFN"))
