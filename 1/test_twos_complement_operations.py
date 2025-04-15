import unittest

from twos_complement_operations import *


class TestTwosComplementOperations(unittest.TestCase):
    def test_twos_complement_negation(self):
        self.assertEqual(twos_complement_negation('00000001'), '11111111')
        self.assertEqual(twos_complement_negation('00000101'), '11111011')
        self.assertEqual(twos_complement_negation('11111111'), '00000001')
        self.assertEqual(twos_complement_negation('11111011'), '00000101')
        self.assertEqual(twos_complement_negation('00000000'), '00000000')

    def test_summarize_in_twos_complement(self):
        self.assertEqual(summarize_in_twos_complement(2, 3), '00000101')
        self.assertEqual(summarize_in_twos_complement(5, 5), '00001010')
        self.assertEqual(summarize_in_twos_complement(5, -6), '11111111')

    def test_subtract_in_twos_complement(self):
        self.assertEqual(subtract_in_twos_complement(10, 7), '00000011')
        self.assertEqual(subtract_in_twos_complement(10, 10), '00000000')
        self.assertEqual(subtract_in_twos_complement(2, -2), '00000100')
