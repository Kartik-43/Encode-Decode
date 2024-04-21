from Alphabet_ED import *


def encode_decode(start_text, shift_amount, direction):
    end_text = ""
    if direction == "decode":
        shift_amount *= -1

    for i in start_text:

        if i in alphabet:
            position = alphabet.index(i)
            new_position = position + shift_amount
            end_text += alphabet[new_position]

        else:
            end_text += i

    print(f"Here's the {direction}d result: {end_text}")

