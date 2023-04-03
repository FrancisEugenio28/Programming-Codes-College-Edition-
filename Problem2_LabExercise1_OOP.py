#Francis Niño A. Eugenio
#BSCPE 1-5 | Object Oriented Programming
#Problem 2: Lab Exercise 1

# gagawa tayo ng input for user
encrypt_str = input('\33[35m' '\33[3m' "What is the text that you are trying to decrypt?: ")
# gagawa tayo ng list of substitutions which is magiging basis natin for decryption
def decrypted_str(encrypted_str):
    decrypted_dict = {'*' : 'a', '&' : 'e', '#' : 'i', '+' : 'o', '!' : 'u'}
# gagawa tayo ng empty list para doon papasok yung decrypted text
    decrypt_str = ""
# maguundergo tayo ng for loop para madecrypt yung input ng user
    for char in encrypt_str:
        if char in decrypted_dict:
            decrypt_str += decrypted_dict[char]
        else:
            decrypt_str += char
    return decrypt_str

import time
print('\33[34m' '\33[4m' "Decrypting your text, Please Wait...".center(150))
time.sleep(3)

# iprint yung output
print('\33[44m' "Decryption Complete. Your Plain Text is " + decrypted_str(encrypt_str))


