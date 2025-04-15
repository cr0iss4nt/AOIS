import unittest

from conversion import *


class TestConversion(unittest.TestCase):
    def test_decimal_to_binary(self):
        self.assertEqual(decimal_to_binary(5), '00000101')
        self.assertEqual(decimal_to_binary(-5), '10000101')
        self.assertEqual(decimal_to_binary(0), '00000000')

    def test_decimal_to_binary_ones_complement(self):
        self.assertEqual(decimal_to_binary_ones_complement(5), '00000101')
        self.assertEqual(decimal_to_binary_ones_complement(-5), '11111010')
        self.assertEqual(decimal_to_binary(0), '00000000')

    def test_decimal_to_binary_twos_complement(self):
        self.assertEqual(decimal_to_binary_twos_complement(5), '00000101')
        self.assertEqual(decimal_to_binary_twos_complement(-5), '11111011')
        self.assertEqual(decimal_to_binary_twos_complement(-128), '10000000')
        self.assertEqual(decimal_to_binary(0), '00000000')

    def test_binary_to_decimal(self):
        self.assertEqual(binary_to_decimal('01111111'), 127)
        self.assertEqual(binary_to_decimal('11111111'), -127)
        self.assertEqual(binary_to_decimal('00000000'), 0)

    def test_binary_ones_complement_to_decimal(self):
        self.assertEqual(binary_ones_complement_to_decimal('01111111'), 127)
        self.assertEqual(binary_ones_complement_to_decimal('11111110'), -1)
        self.assertEqual(binary_ones_complement_to_decimal('11111111'), 0)
        self.assertEqual(binary_ones_complement_to_decimal('00000000'), 0)

    def test_binary_twos_complement_to_decimal(self):
        self.assertEqual(binary_twos_complement_to_decimal('01111111'), 127)
        self.assertEqual(binary_twos_complement_to_decimal('11111110'), -2)
        self.assertEqual(binary_twos_complement_to_decimal('11111111'), -1)
        self.assertEqual(binary_twos_complement_to_decimal('00000000'), 0)
