# -*- coding: utf-8 -*-
import unittest
import decoder


class TestTransformToNumberSequence (unittest.TestCase):

    def test_transform_to_number_sequence(self):
        input_string = 'abracadabra'
        number_sequence = "01203040120"
        self.assertEqual(decoder.transform_to_number_sequence(input_string),number_sequence)


class TestSplitText (unittest.TestCase):

    def test_split_test(self):
        input_text = "Hi! My name is Kate? I am nineteen years old, are not I?"
        splitted_text = ["Hi","My","name","is","Kate","I","am","nineteen","years","old","are","not","I"]
        actual = decoder.split_text(input_text)
        self.assertEqual(actual,splitted_text)


class TestSeparationToBuckets(unittest.TestCase):

    def separate_to_buckets_test(self):
        input_words_array = ["Hi","My","name","is","Kate","I","am","nineteen","years","old","are","not","I"]
        expected = {'1':{'I','I'},'2':{'Hi','My','is','am'},'3':{'old','are','not'},'4':{'name','Kate'},'5':{'years'},'8':{'nineteen'}}
        self.assertEqual(decoder.separate_to_buckets(input_words_array),expected)


if __name__ == '__main__':
    unittest.main()