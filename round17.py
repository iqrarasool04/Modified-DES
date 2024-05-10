from algorithm import xor
from algorithm import hex2bin


import random

# def round_17(ciphertext, key):
#     # Divide ciphertext into 16 sub-frames of 4 bits each
#     subframes = [ciphertext[i:i+4] for i in range(0, len(ciphertext), 4)]
#     print(subframes)

#     # Create output sub-frames list
#     output_subframes = ['0'] * 32
#     print(output_subframes)

#     # # Pad the key with zeros if it's shorter than 80 bits
#     # key = key.zfill(80)
#     # Map each input sub-frame to an output sub-frame using the key
#     for i in range(32):
#         key_subframe = int(key[i*5:i*5+5], 2)
#         print(key_subframe)
#         output_subframes[key_subframe] = subframes[i]
#         print(output_subframes)
#         if i == 15:
#             break


#     # Fill the remaining 16 sub-frames randomly with zeros and ones
#     # for i in range(16, 32):
#     #     output_subframes[i] = str(random.randint(0, 1)) * 4
#     # Add random 4-bit subframes where there are no bits (0)
#     for i in range(32):
#         if output_subframes[i] == '0':
#             output_subframes[i] = format(random.randint(0, 15), '04b')
#             print('full',output_subframes)

#     # Concatenate output sub-frames to get the final ciphertext
#     final_ciphertext = ''.join(output_subframes)

#     return final_ciphertext

def round_17(ciphertext, key):
    # Divide ciphertext into 16 sub-frames of 4 bits each
    subframes = [ciphertext[i:i+4] for i in range(0, len(ciphertext), 4)]
    # print(subframes)

    # Create output sub-frames list
    output_subframes = ['0'] * 32
    # print(output_subframes)

    # Map each input sub-frame to an output sub-frame using the key
    for i in range(32):
        key_subframe = int(key[i*5:i*5+5], 2)
        # print(key_subframe)
        # Perform XOR operation if there is an existing value
        if output_subframes[key_subframe] != '0':
            output_subframes[key_subframe] = xor(output_subframes[key_subframe], subframes[i])
        else:
            output_subframes[key_subframe] = subframes[i]
        # print(output_subframes)
        if i == 15:
            break

    # Fill the remaining 16 sub-frames randomly with zeros and ones
    for i in range(32):
        if output_subframes[i] == '0':
            output_subframes[i] = format(random.randint(0, 15), '04b')
    # print('full',output_subframes)

    # Concatenate output sub-frames to get the final ciphertext
    final_ciphertext = ''.join(output_subframes)

    return final_ciphertext



# def inverse_round_17(ciphertext, key):
#     # Divide ciphertext into 32 sub-frames of 4 bits each
#     subframes = [ciphertext[i:i+4] for i in range(0, len(ciphertext), 4)]

#     # Create input sub-frames list
#     input_subframes = ['0'] * 16

#     # Map each output sub-frame to an input sub-frame using the key
#     for i in range(16):
#         key_subframe = int(key[i*5:i*5+5], 2)
#         input_subframes[key_subframe] = subframes[i]

#     # Concatenate input sub-frames to get the original plaintext
#     original_plaintext = ''.join(input_subframes)

#     return original_plaintext
# def inverse_round_17(ciphertext, key):
#     # Divide ciphertext into 32 sub-frames of 4 bits each
#     subframes = [ciphertext[i:i+4] for i in range(0, len(ciphertext), 4)]

#     # Create input sub-frames list
#     input_subframes = ['0'] * 16

#     # Map each output sub-frame to an input sub-frame using the key
#     for i in range(16):
#         key_subframe = int(key[i*5:i*5+5], 2)
#         input_subframes[key_subframe] = subframes[i]

#     # Concatenate input sub-frames to get the original plaintext
#     original_plaintext = ''.join(input_subframes)

#     return original_plaintext

# Example usage
# print(remaining_80_bits)
# print(len(remaining_80_bits))
# print(hex2bin(cipher_text))
# print(len(hex2bin(cipher_text)))
# key = "00101010101010101010101010101010101010101010101010101010101010101010101010"  # 80-bit key
# ciphertext = "1100110011001100110011001100110011001100110011001100110011001100"  # 64-bit ciphertext
# cipher_text = hex2bin(cipher_text)
# output_cipher = round_17(cipher_text, remaining_80_bits)
# print("Output Cipher Text:", output_cipher)
# print("Output Cipher Text (hex):", bin2hex(output_cipher))
# print(len(output_cipher))
# original_text = hex2bin(original_text)
# original_text = inverse_round_17(text, remaining_80_bits)
# print("Original Text:", original_text)
