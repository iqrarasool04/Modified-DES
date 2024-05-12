from algorithm import bin2hex, encrypt
from key import rkb, rk
from main import output_cipher
import time

# Generate a subset of keys for demonstration (e.g., first 10 keys)
all_possible_keys = [format(i, '0120b') for i in range(10000)]

start_time = time.time()
# Try each key to decrypt the cipher text
for possible_key in all_possible_keys:
    possible_key_hex = bin2hex(possible_key)
    print("Trying key:", possible_key_hex)
    decrypted_text = encrypt(output_cipher, rkb, rk)
    
    # Check if the decrypted text is the original plaintext
    if decrypted_text == output_cipher:
        print("Key found:", possible_key_hex)
        break
end_time = time.time()
print("Time taken:", end_time - start_time, "seconds")
