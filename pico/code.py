# Importing necessary libraries
import random  # Library for generating random numbers (not used in this script)
import sys  # Library for system-specific parameters and functions (not used in this script)

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
flag_enc = chr(0x13) + chr(0x01) + chr(0x17) + chr(0x07) + chr(0x2c) + chr(0x3a) + chr(0x2f) + chr(0x1a) + chr(0x0d) + \
           chr(0x53) + chr(0x0c) + chr(0x47) + chr(0x0a) + chr(0x5f) + chr(0x5e) + chr(0x02) + chr(0x3e) + chr(0x5a) + \
           chr(0x56) + chr(0x5d) + chr(0x45) + chr(0x5d) + chr(0x58) + chr(0x31) + chr(0x58) + chr(0x58) + chr(0x59) + \
           chr(0x02) + chr(0x51) + chr(0x4c) + chr(0x5a) + chr(0x0c) + chr(0x13)

# Function to print the decrypted flag
def print_flag():
    try:
        # Reading the codebook file
        codebook = open('codebook.txt', 'r').read()
        
        # Constructing the password from specific characters of the codebook
        password = codebook[4] + codebook[14] + codebook[13] + codebook[14] + \
                   codebook[23] + codebook[25] + codebook[16] + codebook[0] + \
                   codebook[25]
        
        # Decrypting the flag using XOR function
        flag = str_xor(flag_enc, password)
        print(flag)  # Printing the decrypted flag
    except FileNotFoundError:
        print('Couldn\'t find codebook.txt. Did you download that file into the same directory as this script?')

# Main function to execute the script
def main():
    print_flag()  # Calling the function to print the flag

# Checking if the script is run directly
if __name__ == "__main__":
    main()  # Running the main function
