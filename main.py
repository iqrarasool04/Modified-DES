from algorithm import bin2hex, hex2bin, encrypt
from key import rkb, rk, remaining_80_bits
from round17 import round_17
from inverseround17 import inverse_round_17

pt = "123456ABCD132539"
print("Encryption")
cipher_text = bin2hex(encrypt(pt, rkb, rk))
print("Cipher Text : ", cipher_text)
cipher_text = hex2bin(cipher_text)
output_cipher = round_17(cipher_text, remaining_80_bits)
print("Cipher Text (After Round 17)", bin2hex(output_cipher))
# print(output_cipher)

output = inverse_round_17(output_cipher, remaining_80_bits)
print('Cipher Text (Round 17 undone)',bin2hex(output))
# print(output)
cipherText = bin2hex(output)
print("Decryption")
rkb_rev = rkb[::-1]
rk_rev = rk[::-1]
text = bin2hex(encrypt(cipherText, rkb_rev, rk_rev))
print("Plain Text : ", text)
