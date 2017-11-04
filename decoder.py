import re


def split_text(input_text):
    return re.findall(r"[\w']+", input_text)


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



if __name__ == '__main__':
    print (separate_to_buckets(split_text("Hi! My name is Kate? I am nineteen years old, are not I?")))