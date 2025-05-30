import unittest

from matrix_functions import summarize_binary


class MatrixFunctions(unittest.TestCase):
    def test_summarize_binary(self):
        self.assertEqual(summarize_binary("11","1"),"100")
        self.assertEqual(summarize_binary("10", "1"), "11")