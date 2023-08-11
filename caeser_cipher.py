alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(any_text, shift, direction):
    final_text = ""
    for char in any_text:
        if char in alphabet:
            if direction == "encode":
                position = alphabet.index(char) + shift
            elif direction == "decode":
                position = alphabet.index(char) - shift
            final_text += alphabet[position]
        else:
            final_text += char
    return final_text

cipher_again = True
while cipher_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26 # in case the user enters very big number.

    result = caeser(any_text= text, shift = shift, direction = direction)
    print(f"The {direction}d text is: {result}")

    answer = input("Would you like to use the program again (YES/NO)\n").lower()
    if answer == "no":
        cipher_again = False
        print("GoodBye")


