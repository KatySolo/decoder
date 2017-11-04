# -*- coding: utf-8 -*-
import unittest
import decoder


class TestTransformToNumberSequence (unittest.TestCase):

    def test_transform_to_number_sequence(self):
        input_string = 'abracadabra'
        number_sequence = "01203040120"
        self.assertEqual(decoder.transform_to_number_sequence(input_string),number_sequence)

class TestSplitTest (unittest.TestCase):

    def test_split_test(self):
        input_text = "Hi! My name is Kate? I am nineteen years old, are not I?"
        splitted_text = ["Hi","My","name","is","Kate","I","am","nineteen","years","old","are","not","I"]
        self.assertEqual(decoder.split_text(input_text),splitted_text)

if __name__ == '__main__':
    unittest.main()