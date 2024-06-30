# Importing necessary library
import random  # Library for generating random numbers

# Function to XOR two strings (secret and key)
def str_xor(secret, key):
    # Extend key to the length of the secret
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]  # Repeating characters of the key
        i = (i + 1) % len(key)  # Cycling through key characters

    # XOR each character of the secret with the corresponding character of the new key
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c, new_key_c) in zip(secret, new_key)])

# Encrypted flag (each character represented as its ASCII value)
flag_enc = chr(0x15) + chr(0x07) + chr(0x08) + chr(0x06) + chr(0x27) + chr(0x21) + chr(0x23) + chr(0x15) + chr(0x5f) + \
           chr(0x05) + chr(0x08) + chr(0x2a) + chr(0x1c) + chr(0x5e) + chr(0x1e) + chr(0x1b) + chr(0x3b) + chr(0x17) + \
           chr(0x51) + chr(0x5b) + chr(0x58) + chr(0x5c) + chr(0x3b) + chr(0x42) + chr(0x53) + chr(0x5c) + chr(0x0d) + \
           chr(0x5e) + chr(0x50) + chr(0x4d) + chr(0x00) + chr(0x13)

# Generate a random number between 10 and 100
num = random.choice(range(10, 101))

# Ask the user to convert the number to binary
print('If ' + str(num) + ' is in decimal base, what is it in binary base?')

# Take the user's input
ans = input('Answer: ')

# Try to convert the user's input from binary to decimal and check if it matches the generated number
try:
    ans_num = int(ans, base=2)  # Convert the binary input to a decimal number
    
    if ans_num == num:
        flag = str_xor(flag_enc, 'enkidu')  # Decrypt the flag using the correct password
        print('That is correct! Here\'s your flag: ' + flag)  # Print the decrypted flag
    else:
        print(str(ans_num) + ' and ' + str(num) + ' are not equal.')  # Print mismatch message

# Handle the case where the user's input is not a valid binary number
except ValueError:
    print('That isn\'t a binary number. Binary numbers contain only 1\'s and 0\'s')
