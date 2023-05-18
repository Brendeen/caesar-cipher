
alphabet = 'abcdefghijklmnopqrstuvwxyz'
caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# numbers = '0123456789'


def encrypt(message, key):
    encrypted = ""
    for character in message:
        if character.isalpha():
            if character.isupper():
                mess_encryp = caps.find(character)
                shift = (mess_encryp + key) % len(caps)
                encrypted += caps[shift]
            else:
                mess_encryp = alphabet.find(character)
                shift = (mess_encryp + key) % len(alphabet)
                encrypted += alphabet[shift]
        # elif character.isdigit():
        #     mess_encryp = numbers.find(character)
        #     shift = (mess_encryp + key) % len(numbers)
        #     encrypted += numbers[shift]
        else:
            encrypted += character
    return encrypted


def decrypt(encrypted_message, key):
    return encrypt(encrypted_message, -key)


def crack(encrypted_message):
    for key in range(26):
        decrypted = encrypt(encrypted_message, -key)
        # Check if the decrypted phrase contains common English words
        if "the" in decrypted.lower() and "of" in decrypted.lower():
            return decrypted
    return ""


if __name__ == "__main__":
    secret_message = 'This message has numbers = 123!'
    encrypt_message = 'nBCM GyMMuAy BuM HOGvyLM = 123!'
    key_ = 10

    print(encrypt(secret_message, key_))
    print(decrypt(encrypt_message, key_))
