from algorithm import xor
import random
from algorithm import hex2bin
from algorithm import bin2hex
from key import remaining_80_bits
from main import cipher_text

import random

def round_17(ciphertext, key):
    # Divide ciphertext into 16 sub-frames of 4 bits each
    subframes = [ciphertext[i:i+4] for i in range(0, len(ciphertext), 4)]
    print(subframes)

    # Create output sub-frames list
    output_subframes = [['0']] * 32

    # Map each input sub-frame to an output sub-frame using the key
    for i in range(32):
        key_subframe = int(key[i*5:i*5+5], 2)
        print(key_subframe)

        # Check if there's already a value at this index
        if output_subframes[key_subframe] == ['0']:
            output_subframes[key_subframe] = [subframes[i]]
            print(output_subframes)
        else:
            output_subframes[key_subframe].append(subframes[i])
            print(output_subframes)

        if i == 15:
            break

    # Fill the remaining 16 sub-frames randomly with zeros and ones
    for i in range(32):
        if output_subframes[i] == ['0']:
            output_subframes[i] = [format(random.randint(0, 15), '04b')]

    # Concatenate output sub-frames to get the final ciphertext
    final_ciphertext = ''.join([''.join(item) for item in output_subframes])

    return final_ciphertext



# Example usage
# print(remaining_80_bits)
# print(len(remaining_80_bits))
# print(hex2bin(cipher_text))
# print(len(hex2bin(cipher_text)))
# key = "00101010101010101010101010101010101010101010101010101010101010101010101010"  # 80-bit key
# ciphertext = "1100110011001100110011001100110011001100110011001100110011001100"  # 64-bit ciphertext
cipher_text = hex2bin(cipher_text)
output_cipher = round_17(cipher_text, remaining_80_bits)
print("Output Cipher Text:", output_cipher)
print("Output Cipher Text (hex):", bin2hex(output_cipher))
print(len(output_cipher))
# original_text = hex2bin(original_text)
# original_text = inverse_round_17(hex2bin(cipher_text), remaining_80_bits)
# print("Original Text:", original_text)
# output_plain = inverse_round_17(hex2bin(output_cipher), remaining_80_bits)
# print("Output Plain Text after Round 17:", output_plain)
# print(len(output_plain))