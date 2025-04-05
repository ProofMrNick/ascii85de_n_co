#!/usr/bin/env python3

import sys 
import base64


def handle_input(inp):
    if '-d ' in inp:
        return decode_ascii85(inp.replace('-d ', ''))
    
    else:
        return encode_ascii85(inp.replace('-e ', ''))  # set to encode by default


def encode_ascii85(string):
    hexes = [hex(i) for i in bytearray(string.encode())]
    while len(hexes) % 4 != 0:
        hexes.append('0x00')

    bytes5 = []
    for i in range(0, len(hexes), 4):
        st = '0x'
        for j in range(4):
            st += hexes[i + j][2:]
        bytes5.append(st)
    
    res = []
    for byte in bytes5:
        n10 = int(byte, 16)
        digits = [int((n10 / (85**i)) % 85) + 33 for i in range(4 + 1)][::-1]
        seq = [chr(digit) for digit in digits]
        res.append(seq)

    return ''.join([''.join([j for j in i]) for i in res])


def decode_ascii85(encoded_string):
    bytes5 = []
    while len(encoded_string) % 5 != 0:
        encoded_string += 'u'  # fill in with zeros to make the length divisible by 5

    for i in range(0, len(encoded_string), 5):
        block = encoded_string[i:i + 5]
        n10 = sum((ord(block[j]) - 33) * (85 ** (4 - j)) for j in range(5))
        bytes5.append(n10)

    decoded_bytes = bytearray()
    for n in bytes5:
        decoded_bytes.extend(n.to_bytes(4, 'big'))

    return decoded_bytes.rstrip(b'\x00').decode()


if __name__ == "__main__":
    input_string = sys.stdin.readline()
    try:
        print(handle_input(input_string.strip()))
    except Exception as e:
        print('Error: invalid string for decoding')
        sys.exit(1)
    
'''
[ INSTRUCTIONS ]

1. Pass keyword `-e` (without quotes) if you wish to encode text; otherwise pass keyword `-d`
2. After a whitespace, pass the text (as a string) that you wish to encode / decode

The program is set to encoding mode by default.

### example:
[in]  i love football!
[out] Bcq51G%De.Df9`,@;Ka'
'''
