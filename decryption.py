# def inverse_round_17(ciphertext, key):
#     # Initialize a dictionary to keep count of decimal numbers
#     decimal_count = {}

#     # Divide the key into slots of 5 bits each
#     key_slots = [key[i:i+5] for i in range(0, len(key), 5)]
#     print(key_slots)
#     print(len(key_slots))
#     # Convert bits in each slot to decimal numbers and keep count
#     for slot in key_slots:
#         decimal_num = int(slot, 2)
#         if decimal_num in decimal_count:
#             decimal_count[decimal_num] += 1
#         else:
#             decimal_count[decimal_num] = 1
#     print(decimal_count)

#     # Initialize an array to store decimal numbers
#     decimal_array = []
    
#     # Store decimal numbers in an array
#     for key, value in decimal_count.items():
#         decimal_array.append(key)
#     print('decimal array',decimal_array)

#     # Divide the ciphertext into slots of 4 bits each
#     ciphertext_slots = [ciphertext[i:i+4] for i in range(0, len(ciphertext), 4)]
#     print(ciphertext_slots)

#     # Initialize an output array to store the 32-bit output
#     output_array = ['0'] * 16

#     # Initialize a new array to store the bits
#     new_key_slots = ['0'] * 32
#     for decimal_num in sorted(decimal_array):
#         print(decimal_num)
#         # Check if the decimal number is within the range of key_slots
#         # if decimal_num < len(key_slots):
#             # Get the bits stored at the index in the ciphertext array
#         bits = ciphertext_slots[decimal_num]
#         print(bits)

#         if decimal_count[decimal_num] > 1:
#             repeat_count = decimal_count[decimal_num]

#             # Split the bits into chunks of 4 bits
#             multiplied_bits = ''.join(ciphertext_slots[decimal_num:decimal_num+repeat_count])
#             # Split the multiplied bits into chunks of 4 bits
#             multiplied_bits = [multiplied_bits[i:i+4] for i in range(0, len(multiplied_bits), 4)]

#             print(multiplied_bits)

#             # Store the multiplied bits as separate strings
#             for i, chunk in enumerate(multiplied_bits):
#                 new_key_slots[decimal_num + i] = [bit for bit in chunk]
#                 # print(key_slots)
#         else:
#             # Put the bits where that index is stored in the key array
#             new_key_slots[decimal_num] = [bit for bit in bits]

#     return new_key_slots
from algorithm import bin2hex
def flatten(lst):
    """Flatten a list of lists"""
    return [item for sublist in lst for item in sublist]

def inverse_round_17(ciphertext, key):
    # Initialize a dictionary to keep count of decimal numbers
    decimal_count = {}

    # Divide the key into slots of 5 bits each
    key_slots = [key[i:i+5] for i in range(0, len(key), 5)]
    # Convert bits in each slot to decimal numbers and keep count
    for slot in key_slots:
        decimal_num = int(slot, 2)
        if decimal_num in decimal_count:
            decimal_count[decimal_num] += 1
        else:
            decimal_count[decimal_num] = 1

    # Initialize an array to store decimal numbers
    decimal_array = []
    
    # Store decimal numbers in an array
    for key, value in decimal_count.items():
        decimal_array.append(key)

    # Divide the ciphertext into slots of 4 bits each
    ciphertext_slots = [ciphertext[i:i+4] for i in range(0, len(ciphertext), 4)]

    # Initialize a new array to store the bits
    new_key_slots = ['0'] * 32
    for decimal_num in sorted(decimal_array):
        # Get the bits stored at the index in the ciphertext array
        bits = ciphertext_slots[decimal_num]

        if decimal_count[decimal_num] > 1:
            repeat_count = decimal_count[decimal_num]

            # Join the bits into a single string
            multiplied_bits = ''.join(ciphertext_slots[decimal_num:decimal_num+repeat_count])

            # Split the multiplied bits into chunks of 4 bits
            multiplied_bits = [multiplied_bits[i:i+4] for i in range(0, len(multiplied_bits), 4)]

            # Store the multiplied bits as separate strings
            new_key_slots[decimal_num] = multiplied_bits
        else:
            # Put the bits where that index is stored in the key array
            new_key_slots[decimal_num] = bits
    print(new_key_slots)
    # Concatenate the bits and omit the zeros
    output_bits = ''.join(flatten([bit if isinstance(bit, str) else bit for bit in new_key_slots if bit != '0']))
    return output_bits


# Example usage
ciphertext = "11001100110011001100110011001100110011001100110011001100110011000101010101010111100000001111010101010101011100110010101000110001"  # 128-bit ciphertext
print(len(ciphertext))
key = "01000110010100011110001010001011010001000111001001010001111100101001110100011100"  # 80-bit key
print(len(key))
output = inverse_round_17(ciphertext, key)
print("64 bit Cipher (binary):", output)
print('64 bit cipher',bin2hex(output))
