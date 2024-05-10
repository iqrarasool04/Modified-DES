from algorithm import hex2bin
from algorithm import permute
from algorithm import shift_left
from algorithm import bin2hex
from algorithm import xor
import random

# Key generation
# --hex to binary
# key = "AABB09182736CCDD"
# key = "AABB09182736CCDDAABB09182736AB"
key = 'A1B2C3D4E5F67890A1B2C3D4E5F67890A1EA'
key = hex2bin(key)
print(key)
print(len(key))

# Extract a random 64-bit key from the 136-bit key
start_index = random.randint(0, len(key) - 64)
random_64_bit_key = key[start_index:start_index+64]
print(random_64_bit_key)
print(len(random_64_bit_key))

# Store the remaining 80 bits
remaining_80_bits = key[:start_index] + key[start_index+64:]
print(remaining_80_bits)
print(len(remaining_80_bits))
# def compress_key(original_key, keyp):
#     compressed_key = ""
#     for index in keyp:
     
        
#         # Ensure index is within the range of the original key
#         if adjusted_index < len(original_key):
#             compressed_key += original_key[adjusted_index]
#         else:
#             # Handle the case where the index exceeds the length of the original key
#             # You can choose to ignore or handle this condition based on your requirements
#             pass
#     return compressed_key

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
key56 = permute(key, keyp, 56)
print(key56)
print(len(key56))
 
# # Number of bit shifts
shift_table = [1, 1, 2, 2,
               2, 2, 2, 2,
               1, 2, 2, 2,
               2, 2, 2, 1]
# shift_table = [1, 2, 1, 2,
#                2, 1, 1, 2,
#                2, 2, 1, 1,
#                1, 1, 2, 2]

# left_1 = key[0:56]
# right_1 = key[56:128]

# # Key- Compression Table : Compression of key from 56 bits to 48 bits
# key_comp = [14, 17, 11, 24, 1, 5,
#             3, 28, 15, 6, 21, 10,
#             23, 19, 12, 4, 26, 8,
#             16, 7, 27, 20, 13, 2,
#             41, 52, 31, 37, 47, 55,
#             30, 40, 51, 45, 33, 48,
#             44, 49, 39, 56, 34, 53,
#             46, 42, 50, 36, 29, 32]
 
# # Splitting
# left_l = left_1[0:28]    # rkb for RoundKeys in binary
# right_l = left_1[28:56]  # rk for RoundKeys in hexadecimal

# left_r = right_1[0:28]
# right_r = right_1[28:56]

# rkb = []
# rk = []
# for i in range(0, 16):
#     # Shifting the bits by nth shifts by checking from shift table
#     #left 2 boxes
#     left_l = shift_left(left_l, shift_table[i])
#     right_l = shift_left(right_l, shift_table[i])

#     #right 2 boxes
#     left_r = shift_left(left_r, shift_table[i])
#     right_r = shift_left(right_r, shift_table[i])

 
#     # Combination of left and right string
#     combine_str1 = left_l + right_l

#     combine_str2 = left_r + right_r

    
 
#     # Compression of key from 56 to 48 bits
#     round_key1 = permute(combine_str1, key_comp, 48)
# #     print(round_key1)
#     round_key2 = permute(combine_str2, key_comp, 48)
# #     print(round_key2)

#     round_key = xor(round_key1,round_key2)
#     print(i,round_key)
 
#     rkb.append(round_key)
#     rk.append(bin2hex(round_key))
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
 

 

