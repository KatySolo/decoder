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
        expected = {1:[{'I': ""},{'I':""}],2:[{'Hi':""},{'My':""},{'is':""},{'am':""}],
                    3:[{'old':""},{'are':""},{'not':""}],
                    4:[{'name':""},{'Kate':""}],5:[{'years':""}],8:[{'nineteen':""}]}
        self.assertEqual(actual,expected)

class TestTransformationBucketsToSequence(unittest.TestCase):

    def test_transform_buckets_to_sequence_less_than_hundred(self):
        expected = {1:[{'I': "0"},{'I':"0"}],2:[{'Hi':"01"},{'My':"01"},{'is':"01"},{'am':"01"}],
                    3:[{'old':"012"},{'are':"012"},{'not':"012"}],
                    4:[{'name':"0123"},{'Kate':"0123"}],5:[{'years':"01234"}],8:[{'nineteen':"01023220"}]}
        actual = decoder.extract_hundred_sequence_from_buckets({1:[{'I': ""},{'I':""}],2:[{'Hi':""},{'My':""},{'is':""},{'am':""}],
                                                                3:[{'old':""},{'are':""},{'not':""}],4:[{'name':""},{'Kate':""}],
                                                                5:[{'years':""}],8:[{'nineteen':""}]})
        self.assertEqual(actual,expected)

    def test_transform_buckets_to_sequence_more_than_hundred(self):
        # buckets = {}
        # sequence_buckets = {}
        # three_letters_words = ['aba' for i in range (200)]
        # three_letters_sequences = ['010' for i in range (100)]
        # buckets[3] = three_letters_words
        # sequence_buckets[3] = three_letters_sequences
        # actual = decoder.extract_hundred_sequence_from_buckets(buckets)
        # expected = sequence_buckets
        # self.assertEqual(actual, expected)
            pass

class TestImport(unittest.TestCase):

    def test_import_words(self):
        expected = ['a','abaca','abba','abbandon','back','buy','c','care','cat','cd','cry','dimmension']
        actual = decoder.import_basic_english_words('test_words')
        self.assertEqual(expected,actual)

    def test_import_text_falure(self):
        actual = decoder.import_input_text('bad_input_directory')
        self.assertEqual(None,actual)

    def test_import_text(self):
        expected = "P sprl dhajopun jhyavvuz huk kyhdpun wpjabylz mvy tf tvaoly. Aopz pz aol alza zlxblujl."
        actual = decoder.import_input_text('input')
        self.assertEqual(expected, actual)

class TestChainTranformation(unittest.TestCase):

    def test_from_import_to_hundred_buckets(self):
        expected = {1:[{'a':'0'},{'c':'0'}],2:[{'cd':'01'}],3:[{'buy':'012'},{'cat':'012'},{'cry':'012'}],
                    4:[{'abba':'0110'},{'back':'0123'},{'care':'0123'}],5:[{'abaca':'01020'}],
                    8:[{"abbandon":'01102342'}],10:[{"dimmension":'0122345164'}]}
        actual = decoder.import_basic_english_words('test_words')
        actual = decoder.separate_to_buckets(actual)
        actual = decoder.extract_hundred_sequence_from_buckets(actual)
        self.assertEqual(expected,actual)
        pass


if __name__ == '__main__':
    unittest.main()