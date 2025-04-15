import unittest

from formula_evaluation import evaluate


class TestFormulaEvaluation(unittest.TestCase):
    def test_evaluate(self):
        self.assertEqual(evaluate('1&1'), '1')
        self.assertEqual(evaluate('1&0'), '0')
        self.assertEqual(evaluate('0|0'), '0')
        self.assertEqual(evaluate('1|0'), '1')
        self.assertEqual(evaluate('1>1'), '1')
        self.assertEqual(evaluate('1>0'), '0')
        self.assertEqual(evaluate('0~0'), '1')
        self.assertEqual(evaluate('1~0'), '0')
