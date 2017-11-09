# -*- coding: utf-8 -*-
import unittest
import decoder


class TestTransformToNumberSequence (unittest.TestCase):

    def test_transform_to_number_sequence(self):
        input_string = 'abracadabra'
        actual = decoder.transform_to_number_sequence(input_string)
        expected = "01203040120"
        self.assertEqual(actual,expected)


class TestSplitText(unittest.TestCase):

    def test_split_test(self):
        input_text = "Hi! My name is Kate? I am nineteen years old, are not I?"
        actual = decoder.split_text(input_text)
        expected = ["Hi","My","name","is","Kate","I","am","nineteen","years","old","are","not","I"]
        self.assertEqual(actual,expected)


class TestSeparationToBuckets(unittest.TestCase):

    def test_separate_to_buckets(self):
        input_words_array = ["Hi","My","name","is","Kate","I","am","nineteen","years","old","are","not","I"]
        actual =  decoder.separate_to_buckets(input_words_array)
        expected = {1:['I','I'],2:['Hi','My','is','am'],3:['old','are','not'],4:['name','Kate'],5:['years'],8:['nineteen']}
        self.assertEqual(actual,expected)


class TestTransformationBucketsToSequence(unittest.TestCase):

    def test_transform_buckets_to_sequence_less_than_hundred(self):
        expected = {1:['0','0'],2:['01','01','01','01'], 3:['012','012','012'],4:['0123','0123'],5:['01234'],8:['01023220']}
        actual = decoder.extract_hundred_sequence_from_buckets({1:['I','I'],2:['Hi','My','is','am'],3:['old','are','not'],4:['name','Kate'],5:['years'],8:['nineteen']})
        self.assertEqual(actual,expected)

    def test_transform_buckets_to_sequence_more_than_hundred(self):
        buckets = {}
        sequence_buckets = {}
        three_letters_words = ['aba' for i in range (200)]
        three_letters_sequences = ['010' for i in range (100)]
        buckets[3] = three_letters_words
        sequence_buckets[3] = three_letters_sequences
        actual = decoder.extract_hundred_sequence_from_buckets(buckets)
        expected = sequence_buckets
        self.assertEqual(actual, expected)

class TestImportBasicEnglishWords(unittest.TestCase):

    def test_import_words(self):
        expected = ['a','ab','abc','b','bc','bcd','c','cd','cde']
        actual = decoder.import_basic_english_words('test_words')
        self.assertEqual(expected,actual)

if __name__ == '__main__':
    unittest.main()