from algorithm import hex2bin
from algorithm import permute
from algorithm import shift_left
from algorithm import bin2hex
import random

# Key generation

# Parity bit drop table to extract 80 bits from a 144-bit key
keyp_80_bits = [1,2, 3,4, 5,6, 7,8, 9,10, 11,12, 13,14, 15,16, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
                41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 
                79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 103, 105, 107, 109, 111, 113,
                115, 117, 119, 121, 123, 125, 127, 129, 131, 133, 135, 137, 139, 141, 143]

def extract_80_and_64_bit_keys(key):
    # Extracting the 80-bit key using the parity bit drop table
    remaining_80_bits = permute(key, keyp_80_bits,80)

    # Extracting the remaining 64 bits from the key
    remaining_64_bits = ''.join(bit for index, bit in enumerate(key) if index + 1 not in keyp_80_bits)

   

    return remaining_80_bits, remaining_64_bits

# Given key in hexadecimal
key_hex = 'A1B2C3D4E5F67890A1B2C3D4E5F67890A1EA'
# print(len(key_hex))

# Convert key from hexadecimal to binary
key_binary = hex2bin(key_hex)

# Extract 80-bit key and the remaining 64 bits consistently
extract_80_and_64_bit_keys(key_binary)
# Extract 80-bit key and the remaining 64 bits consistently
remaining_80_bits, remaining_64_bits=extract_80_and_64_bit_keys(key_binary)
# print(len(remaining_80_bits))
# print(len(remaining_64_bits))
  # Print the extracted 80-bit key and the remaining 64 bits
# print("80-bit Key:", bin2hex(remaining_80_bits))
# print("Remaining 64 bits:", bin2hex(remaining_64_bits))

# --parity bit drop table
keyp = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]
    
 
# getting 56 bit key from 64 bit using the parity bits
key56 = permute(remaining_64_bits, keyp, 56)
# print(key56)
# print(len(key56))
 
# # Number of bit shifts
shift_table = [1, 1, 2, 2,
               2, 2, 2, 2,
               1, 2, 2, 2,
               2, 2, 2, 1]

# Key- Compression Table : Compression of key from 56 bits to 48 bits
key_comp = [14, 17, 11, 24, 1, 5,
            3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8,
            16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55,
            30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53,
            46, 42, 50, 36, 29, 32]
 
# Splitting
left = key56[0:28]    # rkb for RoundKeys in binary
right = key56[28:56]  # rk for RoundKeys in hexadecimal
 
rkb = []
rk = []
for i in range(0, 16):
    # Shifting the bits by nth shifts by checking from shift table
    left = shift_left(left, shift_table[i])
    right = shift_left(right, shift_table[i])
 
    # Combination of left and right string
    combine_str = left + right
 
    # Compression of key from 56 to 48 bits
    round_key = permute(combine_str, key_comp, 48)
 
    rkb.append(round_key)
    rk.append(bin2hex(round_key))