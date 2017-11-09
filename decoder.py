import re
import os


def split_text(input_text):
    return re.findall(r"[\w']+", input_text)

def import_basic_english_words(directory):
    basic_english_words = []
    for file in os.listdir(directory + "/"):
        if file.endswith(".txt"):
            with open(directory + "/" + file, 'r') as f:
                for line in f:
                    basic_english_words.append(line)
    basic_english_words = [line.rstrip('\n') for line in basic_english_words]
    basic_english_words.sort()
    return basic_english_words

def import_input_text(directory):
    text=""
    inputDirectory = (directory + '/input.txt', 'input.txt')[directory == '.']
    try:
        with open(inputDirectory,'r') as f:
            for char in f.read():
                text += char
        return text
    except IOError:
        print ("File not found")
        return None



def separate_to_buckets(input_words_array):
    buckets = {}
    for word in input_words_array:
        if len(buckets) == 0:
            buckets[len(word)] = [word]
            continue
        for key in buckets.keys():
            if key != len(word):
                if len(word) in buckets.keys():
                    continue
                else:
                    buckets[len(word)] = [word]
                break
            else:
                buckets[len(word)].append(word)
                break
    return buckets

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


def extract_hundred_sequence_from_buckets(buckets):
    sequence_buckets = {}
    for i in buckets.keys():
        sequence_buckets[i] = []
        for n in range(min(len(buckets[i]),100)):
            sequence_buckets[i].append(transform_to_number_sequence(buckets[i][n]))
    return sequence_buckets


if __name__ == '__main__':
    text = import_input_text()
    if text is not None:
        print ('OK')
        print (text)
