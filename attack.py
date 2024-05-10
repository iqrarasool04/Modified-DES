from algorithm import bin2hex, encrypt
from key import rkb, rk

# Cipher text to be decrypted
cipher_text = "3DF950DD4DEB6776"

# Generator function to produce keys on-the-fly
def key_generator():
    for i in range(2**120):
        yield format(i, '0120b')

# Iterate over the key generator to try each key
for index, possible_key_binary in enumerate(key_generator(), start=1):
    possible_key_hex = bin2hex(possible_key_binary)
    print("Trying key:", possible_key_hex)
    
    # Decrypt the cipher text using the current key
    decrypted_text = encrypt(cipher_text, rkb, rk)
    
    # Check if the decrypted text matches the original plaintext
    if decrypted_text == cipher_text:
        print("Key found:", possible_key_hex)
        break  # Exit the loop if the key is found

    # Print progress every 10,000 keys
    if index % 10000 == 0:
        print("Tried {} keys...".format(index))

