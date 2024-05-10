from algorithm import bin2hex
from algorithm import encrypt
from key import rkb
from key import rk
from key import remaining_80_bits
# from algorithm import hex2bin
# from round17 import round_17
# from round17 import inverse_round_17

# pt = "123456ABCD132536"
pt = "123456ABCD132539"
print("Encryption")
cipher_text = bin2hex(encrypt(pt, rkb, rk))
print("Cipher Text : ", cipher_text)
# output_cipher = round_17(hex2bin(cipher_text), remaining_80_bits)
# print("Output Cipher Text after Round 17:", output_cipher)
# print("Output Cipher Text after Round 17(hex):", bin2hex(output_cipher))

print("Decryption")
rkb_rev = rkb[::-1]
rk_rev = rk[::-1]
# output_plain = inverse_round_17(hex2bin(output_cipher), remaining_80_bits)
# print("Output Plain Text after Round 17:", output_plain)
# print(len(output_plain))
# print("Output Plain Text after Round 17(hex):", bin2hex(output_plain))
text = bin2hex(encrypt(cipher_text, rkb_rev, rk_rev))
print("Plain Text : ", text)