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


def crack_the_code(english_word, coded_word):
    shift_alphabet = {i: '' for i in map(chr, range(97, 123))}
    print (english_word)
    print (coded_word)
    for i in range(len(english_word)):
        shift_alphabet[english_word[i]] = coded_word[i]

if __name__ == '__main__':
    text = import_input_text("input")
    if text is not None:
        print ('OK')
        print (text)
    words_array = split_text(text)
    print (words_array)
    buckets = separate_to_buckets(words_array)
    print (buckets)
    buckets_seq = extract_hundred_sequence_from_buckets(buckets)
    print (buckets_seq)
    eng_words = import_basic_english_words("words")
    eng_words = separate_to_buckets(eng_words)
    eng_words_seq = extract_hundred_sequence_from_buckets(eng_words)
    max_index = buckets_seq.keys().pop()
    print (max_index)
    i =0
    j = 0
    # print (eng_words[max_index])
    for eng_word in eng_words_seq[max_index]:
        i += 1
        for word in buckets_seq[max_index]:
            j += 1
            if eng_word.find(word) != -1:
                print ("found matching at (" + str(i) + ',' + str(j)+')')
                print (word + ' in ' + eng_word)
                print ("trying convert " + eng_words[max_index][i] + ' to '+ buckets[max_index][j])
                crack_the_code(eng_words[max_index][i],buckets[max_index][j])
        j = 0