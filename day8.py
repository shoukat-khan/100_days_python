 #ceasor cypher

def caesar_cipher(text, shift, direction):
    new_text = ""
    if direction == "decode":
        shift *= -1
    for char in text:
        if char.isalpha():
            new_text += chr((ord(char.upper()) - 65 + shift) % 26 + 65).lower()
            
        else:
            new_text += char
    print(f"The {direction}d text is: {new_text}")

bool =True
while bool:
    TEXT = input("Enter the text: ").upper()
    SHIFT = int(input("Enter the shift number: "))
    DIRECTION = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    caesar_cipher(TEXT, SHIFT, DIRECTION)
    result = input("Do you want to continue? Type 'yes' or 'no': ").lower()
    if result == "no":
        bool = False
        print("Goodbye") 
    else:
        bool = True
        print("Welcome back")
