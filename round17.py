from keyy import remaining_80_bits
from main import cipher_text
from algorithm import hex2bin
import random

def round_17(ciphertext, key):
    # Divide ciphertext into 16 sub-frames of 4 bits each
    subframes = [ciphertext[i:i+4] for i in range(0, len(ciphertext), 4)]
    print(subframes)

    # Create output sub-frames list
    output_subframes = ['0'] * 32
    print(output_subframes)

    # # Pad the key with zeros if it's shorter than 80 bits
    # key = key.zfill(80)
    # Map each input sub-frame to an output sub-frame using the key
    for i in range(32):
        key_subframe = int(key[i*5:i*5+5], 2)
        print(key_subframe)
        output_subframes[key_subframe] = subframes[i]
        print(output_subframes)
        zero_count = output_subframes.count('0')  # Count the number of '0000' subframes
        print(zero_count)
        if zero_count == 18:
            break


    # Fill the remaining 16 sub-frames randomly with zeros and ones
    # for i in range(16, 32):
    #     output_subframes[i] = str(random.randint(0, 1)) * 4
    # Add random 4-bit subframes where there are no bits (0)
    for i in range(32):
        if output_subframes[i] == '0':
            output_subframes[i] = format(random.randint(0, 15), '04b')
            print('full',output_subframes)

    # Concatenate output sub-frames to get the final ciphertext
    final_ciphertext = ''.join(output_subframes)

    return final_ciphertext


# def round_17(input_64, key_80):
#     # Divide the 64-bit input into sixteen 4-bit sub-frames
#     input_subframes = [(input_64 >> i) & 0b1111 for i in range(60, -4, -4)]

#     # Initialize the 128-bit output cipher
#     cipher = 0

#     # Use each five bits of the 80-bit key to map one of the 4-bit input sub-frames to one 4-bit output sub-frame
#     for i in range(0, 80, 5):
#         key_subframe = (key_80 >> i) & 0b11111
#         input_index = key_subframe % 16
#         output_subframe = input_subframes[input_index]
#         cipher |= output_subframe << i

#     # Fill the remaining 16 sub-frames of the output with random zeros and ones
#     for i in range(80, 128, 4):
#         cipher |= random.randint(0, 15) << i

#     return cipher

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
print(remaining_80_bits)
print(len(remaining_80_bits))
print(hex2bin(cipher_text))
print(len(hex2bin(cipher_text)))
# key = "00101010101010101010101010101010101010101010101010101010101010101010101010"  # 80-bit key
# ciphertext = "1100110011001100110011001100110011001100110011001100110011001100"  # 64-bit ciphertext
cipher_text = hex2bin(cipher_text)
output_cipher = round_17(cipher_text, remaining_80_bits)
print("Output Cipher Text:", output_cipher)