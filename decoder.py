import re


def split_text(input_text):
    return re.findall(r"[\w']+", input_text)

def transform_to_number_sequence (input_string):
    letters = {}
    number_sequence = ""
    pointer = 0
    for letter in input_string.lower():
        if letter not in letters:
            letters[letter] = pointer
            number_sequence += str(pointer)
            pointer += 1
        else:
            number_sequence += str(letters[letter])
    return number_sequence
