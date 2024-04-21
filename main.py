from Alphabet_ED import *
from Logo_ED import *
from Function_ED import *

print(logo)

should_end = False
while not should_end:
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    shift = shift % 26

    if direction == 'encode' or 'decode':
        encode_decode(start_text=text, shift_amount=shift, direction=direction)

        with open("Encoded_Texts.txt", 'a') as file:
            if direction == 'encode':
                file.write("Text - " + text + f", Shift - {shift}\n")

        with open("Decoded_Texts.txt", 'a') as file2:
            if direction == 'decode':
                file2.write("Text - " + text + f", Shift - {shift}\n")


    else:
        should_end = True
        print("Write a correct input !")

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    if restart == "no":
        should_end = True
        print("\n\nOK\nGoodbye")

    else:
        print('\n\n')

file.close()
file2.close()
