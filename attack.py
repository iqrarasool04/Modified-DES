from algorithm import bin2hex, encrypt
from key import rkb, rk

# Cipher text to be decrypted
cipher_text = "3DF950DD4DEB6776"
print(len(cipher_text))

# Generate all possible keys (simplified for demonstration)
# In a real scenario, you'd loop through all 2^120 possible keys
# all_possible_keys = ["00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
#                       "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000001",
#                       # Continue generating all 2^120 keys
#                       ]
# Generate a subset of keys for demonstration (e.g., first 10 keys)
all_possible_keys = [format(i, '0120b') for i in range(2**120)]
all_possible_keys_hex = [bin2hex(key) for key in all_possible_keys]

# Try each key to decrypt the cipher text
for possible_key in all_possible_keys:
    possible_key_hex = bin2hex(possible_key)
    print("Trying key:", possible_key_hex)
    decrypted_text = encrypt(cipher_text, rkb, rk)
    
    # Check if the decrypted text is the original plaintext
    if decrypted_text == cipher_text:
        print("Key found:", possible_key_hex)
        break
