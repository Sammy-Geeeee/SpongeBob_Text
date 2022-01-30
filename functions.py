# This will be all the functions needed to run this program

import random


def spongeBobify(input_text):
    characters = []
    for letter in input_text:
        if random.randint(1, 2) == 1:  # To randomly choose whether it is upper or lower
            letter = letter.lower()
        else:
            letter = letter.upper()
        characters.append(letter)

    # This part will make it less random, but it will appear more random, is nicer to look at
    i = 0
    while i < len(characters) - 2:
        if characters[i].isupper() and characters[i+1].isupper():  # To check if there is multiple consecutive uppercase characters
            characters[i+2] = characters[i+2].lower()
        elif characters[i].islower() and characters[i+1].islower():  # To check for too many lower characters
            characters[i+2] = characters[i+2].upper()
        i += 1

    text_converted = ''.join(characters)
    return text_converted
