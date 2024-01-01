alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    encrypted_text = ""
    for char in plain_text.lower():
        index = alphabet.index(char)
        shifted_index = index + shift_amount
        encrypted_text += alphabet[shifted_index]
    print(f"Encrypted message:  {encrypted_text}")

def decrypt(encrypted_text, shift_amount):
    decrypted_text = ""
    for char in encrypted_text.lower():
        index = alphabet.index(char)
        deshifted_index = index - shift_amount
        decrypted_text += alphabet[deshifted_index]
    print(f"Decrypted message:  {decrypted_text}")

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)

