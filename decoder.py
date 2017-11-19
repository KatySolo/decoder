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
    word_memo = {}
    for word in input_words_array:
        if len(buckets) == 0:
            word_memo[word] = ""
            buckets[len(word)] = [word_memo]
            word_memo={}
            continue
        for key in buckets.keys():
            if key != len(word):
                if len(word) in buckets.keys():
                    continue
                else:
                    word_memo[word] = ""
                    buckets[len(word)] = [word_memo]
                    word_memo = {}
                break
            else:
                word_memo[word]=""
                buckets[len(word)].append(word_memo)
                word_memo ={}
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
    sequence_buckets = buckets.copy()
    for i in sequence_buckets.keys():
        for n in range(min(len(buckets[i]),100)):
            for j in sequence_buckets[i][n].keys():
                sequence_buckets[i][n][j] = transform_to_number_sequence(j)
    return sequence_buckets

# [1:['a':'0','b':'0'],2:['ab':'01','aa':'00']]


def build_alphabet(english_word, coded_word):
    shift_alphabet = {i: '' for i in map(chr, range(97, 123))}
    print (english_word)
    print (coded_word)
    for i in range(len(english_word)):
        shift_alphabet[english_word[i]] = coded_word[i]
    return shift_alphabet


def start_programme(input_dir, input_basic_dir):
    pass

if __name__ == '__main__':
    text = import_input_text("input")
    if text is not None:
        print ('OK')
        print (text)
    words_array = split_text(text)
    print (words_array)
    buckets = separate_to_buckets(words_array)
    print (buckets)
    buckets_seq = extract_hundred_transform_dict_sequence_from_buckets(buckets)
    # all_buckets
    print (buckets_seq)
    eng_words = import_basic_english_words("test_words")
    eng_words = separate_to_buckets(eng_words)
    eng_words_seq = extract_hundred_transform_dict_sequence_from_buckets(eng_words)
    max_index = buckets_seq.keys().pop()
    print (max_index)
    i =-1
    j = -1
    shift_alphabet = {}
    # print (eng_words[max_index])
    for eng_word in eng_words_seq[max_index]:
        i += 1
        for word in buckets_seq[max_index]:
            j += 1
            if eng_word.find(word) != -1:
                print ("found matching at (" + str(i) + ',' + str(j)+')')
                print (word + ' in ' + eng_word)
                print ("trying convert " + eng_words[max_index][i] + ' to '+ buckets[max_index][j])
                shift_alphabet = build_alphabet(eng_words[max_index][i], buckets[max_index][j])
                replace_all_found_letters(shift_alphabet, all_buckets[max_index])

        j = -1