#Francis Niño A. Eugenio
#BSCPE 1-5 | Object Oriented Programing
#Program 3

import colorama
import pyfiglet

colorama.init()

# input para sa mga user (message, key)
message = input(colorama.Fore.LIGHTMAGENTA_EX + "Please enter your Message: ")
key = input(colorama.Fore.LIGHTMAGENTA_EX + "Please enter your key: ")

def vigenere_cipher(message,key):
    # irerepeat natin yung key base sa length nung message
    key_index = key * (len(message)// len(key) + 1)
    key_index = key_index[:len(message)]

    # Gagawa tayo ng empty cipher text variable wherein dun natin ilalagay yung output 
    cipher_text = ''

    # iiscan natin each character sa message (gagamit tayo ng for loop para dito)
    for i in range(len(message)):
    # kukunin natin yung ASCII code ng both message and key 
        message_code = ord(message[i])
        key_code = ord(key_index[i])
    # isusubtract natin ito sa 65 para maging A=0, B=1,...
        message_code -= 65
        key_code -= 65
    # Peperform na natin yung formula para sa Vigenere Cipher
        cipher_code = (message_code + key_code) % 26
    # magaadd tayo ng 65 para maconvert at makuha yung ASCII code nung cipher text
        cipher_code += 65
        cipher_code += chr(cipher_code)

    return cipher_text

# import tayo ng time like loading effect 
import time
print("Decoding...".center(150))
time.sleep(3)

# print na natin yung output
cipher_text = vigenere_cipher(message,key)
print(cipher_text)