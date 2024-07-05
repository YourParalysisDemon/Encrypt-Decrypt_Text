chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' '1234567890"
chars = list(chars)
# add your key here
key = ""

# ENCRYPT
while True:
    plain_text = input("Enter a message to encrypt:")
    cipher_text = ""
    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]

    print(f"Original message : {plain_text}")
    print(f"Encrypted message: {cipher_text}")

    # DECRYPT
    cipher_text = input("Enter a message to decrypt:")
    plain_text = ""
    for letter in cipher_text:
        index = key.index(letter)
        plain_text += chars[index]

    print(f"Encrypted message: {cipher_text}")
    print(f"Original message : {plain_text}")
