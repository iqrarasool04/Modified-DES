from algorithm import hex2bin
from algorithm import permute
from algorithm import shift_left
from algorithm import bin2hex

# Key generation
# --hex to binary
# key = "AABB09182736CCDD"
key = "AABB09182736CCDDAABB09182736AB"
key = hex2bin(key)
print(key)
 
# --parity bit drop table
keyp = [58, 11, 72, 21, 40, 27, 16, 93, 65, 78, 5, 64, 47, 34,
        57, 88, 26, 59, 11, 48, 35, 54, 117, 10, 101, 92, 86, 17,
        4, 56, 94, 41, 87, 71, 96, 25, 79, 46, 109, 39, 107, 80,
        23, 32, 97, 14, 55, 85, 102, 2113, 38, 115, 44, 110, 6,
        12, 84, 50, 77, 66, 20, 118, 74, 81, 51, 106, 103, 24, 63,
        36, 67, 73, 9, 43, 22, 91, 19, 52, 114, 7, 108, 111, 98,
        3, 49, 89, 31, 61, 37, 95, 29, 68, 100, 69, 116, 82, 33,
        42, 18, 70, 53, 76, 8, 83, 28, 112, 99, 13, 119, 104, 62]
 
# getting 112 bit key from 120 bit using the parity bits
key = permute(key, keyp, 112)
print(key)
 
# Number of bit shifts
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
left = key[0:28]    # rkb for RoundKeys in binary
right = key[28:56]  # rk for RoundKeys in hexadecimal
 
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
 

 

