import argparse
import decoder

parser = argparse.ArgumentParser()
parser.add_argument("--input_text_dir", help = "Directory for 'input.txt' file", type=str)
parser.add_argument("--input_basic_words_dir", help = "Directory for basic words's files", type=str)
args = parser.parse_args()

# print (args)

decoder.start_programme(args.input_text_dir, args.input_basic_words_dir)