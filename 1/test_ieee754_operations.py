import unittest

from conversion import ieee754_to_float
from ieee754_operations import *


class TestIEEE754operations(unittest.TestCase):
    def test_float_to_ieee754(self):
        self.assertEqual(float_to_ieee754(2), '01000000000000000000000000000000')
        self.assertEqual(float_to_ieee754(-2), '11000000000000000000000000000000')
        self.assertEqual(float_to_ieee754(2.25), '01000000000100000000000000000000')
        self.assertEqual(float_to_ieee754(-2.527878356), '11000000001000011100100011000010')

    def test_summarize_ieee754(self):
        self.assertEqual(summarize_ieee754(1, 1), '01000000000000000000000000000000')
        self.assertEqual(summarize_ieee754(2, 3), '01000000101000000000000000000000')
        self.assertEqual(summarize_ieee754(0.125, 0.25), '00111110110000000000000000000000')
        self.assertEqual(summarize_ieee754(2, 0), '01000000000000000000000000000000')

    def test_ieee754_to_float(self):
        self.assertEqual(ieee754_to_float('01000000000000000000000000000000'), 2)
        self.assertEqual(ieee754_to_float('11000000000000000000000000000000'), -2)
        self.assertEqual(ieee754_to_float('01000000000100000000000000000000'), 2.25)
        self.assertEqual(ieee754_to_float('11000000001000011100100011000010'), -2.5278782844543457)
