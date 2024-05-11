from algorithm import xor
import random
from algorithm import dec2bin

import random

def b2d(binary):
    decimal = 0
    power = len(binary) - 1
    for digit in binary:
        decimal += int(digit) * (2 ** power)
        power -= 1
    return decimal

def round_17(ciphertext, key):
    # Divide ciphertext into 16 sub-frames of 4 bits each
    subframes = [ciphertext[i:i+4] for i in range(0, len(ciphertext), 4)]
    # Divide  into 16 sub-frames of 5 bits each
    keyframes = [b2d(key[i:i+5]) for i in range(0, len(key), 5)]
    # print(subframes)
    # print(keyframes)
    
    CT_b = [[] for _ in range(32)]

    finalCT = []
    randomsAdded = 0

    for i in range(16):
        CT_b[keyframes[i]].append(subframes[i])
            
    for i in range(32):
        for j in range(len(CT_b[i])):
            finalCT.append(CT_b[i][j])

        if len(CT_b[i]) == 0 and len(finalCT) <= i and randomsAdded < 16:
            finalCT.append(dec2bin(random.randint(0, 15)))
            randomsAdded+=1    
    # print(CT_b)
    # print(finalCT, len(finalCT))

    return ''.join([''.join(item) for item in finalCT])


# cipher_text = hex2bin(cipher_text)
# output_cipher = round_17(cipher_text, remaining_80_bits)
# print("Cipher Text (After Round 17)", bin2hex(output_cipher))