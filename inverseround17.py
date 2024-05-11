# from round17 import output_cipher as ciphertext

def flatten(lst):
    """Flatten a list of lists"""
    return [item for sublist in lst for item in sublist]


def b2d(binary):
    decimal = 0
    power = len(binary) - 1
    for digit in binary:
        decimal += int(digit) * (2 ** power)
        power -= 1
    return decimal

def inverse_round_17(ciphertext, key):
    subframes = [ciphertext[i:i+4] for i in range(0, len(ciphertext), 4)]
    keyframes = [b2d(key[i:i+5]) for i in range(0, len(key), 5)]

    _CT_a = [chr(65+i) for i in range(16)]
    # print(_CT_a)
    
    _CT_b = [[] for _ in range(32)]

    _finalCT = []

    randomsAdded = 0

    for i in range(16):
        _CT_b[keyframes[i]].append(_CT_a[i])
        # print(_CT_b)
            
    for i in range(32):
        # print(i)
        for j in range(len(_CT_b[i])):
            _finalCT.append(_CT_b[i][j])
            # print(_finalCT)

        if len(_CT_b[i]) == 0 and len(_finalCT) <= i and randomsAdded < 16:
            _finalCT.append(None)
            randomsAdded+=1    

    CT_a = [None for _ in range(16)]
    for i in range(32):
        if _finalCT[i] != None:
            CT_a[ord(_finalCT[i])-65] = subframes[i]

    # print("64 bit:")
    # print(CT_a)

    return ''.join([''.join(item) for item in CT_a])

# output = inverse_round_17(ciphertext, remaining_80_bits)
# print('Cipher Text (Round 17 undone)',bin2hex(output))