# Mono-alphabetic Cipher
def monoalphabetic_cipher(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                ciphertext += key[ord(char) - 65].upper()
            else:
                ciphertext += key[ord(char) - 97].lower()
        else:
            ciphertext += char
    return ciphertext

def monoalphabetic_decipher(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                plaintext += chr(key.index(char.upper()) + 65)
            else:
                plaintext += chr(key.index(char.lower()) + 97)
        else:
            plaintext += char
    return plaintext


# Vigenere Cipher
def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key_length = len(key)
    key_as_int = [ord(i.upper()) - 65 for i in key]
    plaintext_as_int = [ord(i.upper()) - 65 for i in plaintext]
    
    for i in range(len(plaintext_as_int)):
        value = (plaintext_as_int[i] + key_as_int[i % key_length]) % 26
        ciphertext += chr(value + 65)
    
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key_length = len(key)
    key_as_int = [ord(i.upper()) - 65 for i in key]
    ciphertext_as_int = [ord(i.upper()) - 65 for i in ciphertext]
    
    for i in range(len(ciphertext_as_int)):
        value = (ciphertext_as_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 65)
    
    return plaintext


# Vernam Cipher
def vernam_cipher(plaintext, key):
    ciphertext = ""
    for i in range(len(plaintext)):
        # convert each character to its corresponding numerical value
        plaintext_num = ord(plaintext[i].lower()) - ord('a')
        key_num = ord(key[i % len(key)].lower()) - ord('a')
        # calculate the ciphertext numerical value using modular addition
        ciphertext_num = (plaintext_num + key_num) % 26
        # convert the ciphertext numerical value back to a character
        ciphertext_char = chr(ciphertext_num + ord('a'))
        ciphertext += ciphertext_char
    return ciphertext

def vernam_decipher(ciphertext, key):
    plaintext = ""
    for i in range(len(ciphertext)):
        # convert each character to its corresponding numerical value
        ciphertext_num = ord(ciphertext[i].lower()) - ord('a')
        key_num = ord(key[i % len(key)].lower()) - ord('a')
        # calculate the plaintext numerical value using modular subtraction
        plaintext_num = (ciphertext_num - key_num) % 26
        # convert the plaintext numerical value back to a character
        plaintext_char = chr(plaintext_num + ord('a'))
        plaintext += plaintext_char
    return plaintext


# One-Time Pad
def OTPencrypt(message, key):
    # One Time Pad Encrypt the message using the key
    encrypted_message = ""
    for i in range(len(message)):
        encrypted_message += chr((ord(message[i]) + ord(key[i])) % 256)
    return encrypted_message

def OTPdecrypt(encrypted_message, key):
    # One Time Pad Decrypt the encrypted message using the key
    decrypted_message = ""
    for i in range(len(encrypted_message)):
        decrypted_message += chr((ord(encrypted_message[i]) - ord(key[i])) % 256)
    return decrypted_message


## Hybrid
# MonoAlphabetic Cipher with Vigenere Cipher (Encryption and Decryption)
def combine_encrypt(plaintext, key1, key2):
    monoalphabetic_cipher_text = monoalphabetic_cipher(plaintext, key1)
    vigenere_cipher_text = vigenere_encrypt(monoalphabetic_cipher_text, key2)
    return vigenere_cipher_text

def combine_decrypt(ciphertext, key1, key2):
    monoalphabetic_decipher_text = monoalphabetic_decipher(vigenere_decrypt(ciphertext, key2), key1)
    return monoalphabetic_decipher_text


# Vernam Cipher with Vigenere Cipher (Encryption and Decryption)
def encrypt_combine(message, key):
    # Use Vernam cipher to encrypt the message
    vernam_ciphertext = vernam_cipher(message, key)
    # Use Vigenere cipher to further encrypt the Vernam ciphertext
    vigenere_ciphertext = vigenere_encrypt(vernam_ciphertext, key)
    return vigenere_ciphertext

def decrypt_combine(ciphertext, key):
    # Use Vigenere cipher to decrypt the ciphertext
    vernam_ciphertext = vigenere_decrypt(ciphertext, key)
    # Use Vernam cipher to further decrypt the Vigenere ciphertext
    plaintext = vernam_decipher(vernam_ciphertext, key)
    return plaintext


# Mono-alphabetic with Vernam Cipher (Encryption and Decryption)
def mono_vernEncrypt(plaintext, key, key2):
    ciphertext = vernam_cipher(plaintext, key)
    ciphertext1 = (monoalphabetic_cipher(ciphertext,key2)).upper()
    
    return ciphertext1

def mono_vernDecrypt(ciphertext,monokey,key) :
    plaintext = monoalphabetic_decipher(ciphertext, monokey)
    decrypted_plaintext = vernam_decipher(plaintext, key)
    
    return decrypted_plaintext


# Function acts as a Bridge between the Front-End and the back-End of the Web Page
def returnOutput(message, algorithm, hybrid_algorithm, option, key, key2):
    if algorithm == 'Mono-alphabetic Cipher':
        if option == 'Encrypt':
            return monoalphabetic_cipher(message, key)
        elif option == 'Decrypt':
            return monoalphabetic_decipher(message, key)
    
    elif algorithm == 'Vigenere Cipher':
        if option == 'Encrypt':
            return vigenere_encrypt(message, key)
        elif option == 'Decrypt':
            return vigenere_decrypt(message, key)
    
    elif algorithm == 'Vernam Cipher':
        if option == 'Encrypt':
            return vernam_cipher(message, key)
        elif option == 'Decrypt':
            return vernam_decipher(message, key)

    elif algorithm == 'One-Time Pad':
        if option == 'Encrypt':
            return OTPencrypt(message, key)
        elif option == 'Decrypt':
            return OTPdecrypt(message, key)

    elif algorithm == 'Hybrid':
        if hybrid_algorithm == 'Mono-alphabetic with Vigenere':
            if option == 'Encrypt':
                return combine_encrypt(message, key, key2)
            else:
                return combine_decrypt(message, key, key2)

        elif hybrid_algorithm == 'Vernam with Vigenere':
            if option == 'Encrypt':
                return encrypt_combine(message, key)
            else:
                return decrypt_combine(message, key)

        elif hybrid_algorithm == 'Mono-alphabetic with Vernam':
            if option == 'Encrypt':
                return mono_vernEncrypt(message, key, key2)
            else:
                return mono_vernDecrypt(message, key, key2)
