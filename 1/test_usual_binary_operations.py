import unittest

from usual_binary_operations import *


class TestUsualBinaryOperations(unittest.TestCase):
    def test_subtract_in_usual_binary(self):
        self.assertEqual(subtract_in_usual_binary('00000011', '00000010'), '1')

    def test_binary_multiply(self):
        self.assertEqual(binary_multiply(7, 5), '0000000000100011')
        self.assertEqual(binary_multiply(-7, 5), '1000000000100011')
        self.assertEqual(binary_multiply(-7, -5), '0000000000100011')
        self.assertEqual(binary_multiply(127, -127), '1011111100000001')

    def test_binary_greater_equal(self):
        self.assertTrue(binary_greater_equal('10000', '100'))
        self.assertFalse(binary_greater_equal('11', '111'))
        self.assertTrue(binary_greater_equal('1111', '1101'))
        self.assertTrue(binary_greater_equal('1111', '1111'))

    def test_binary_divide(self):
        self.assertEqual(binary_divide(8, 4), '00000010')
        self.assertEqual(binary_divide(80, 55), '00000001.01110')
