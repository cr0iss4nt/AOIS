import unittest

from formula import normalize, is_atomic_formula, evaluate_formula


class TestFormula(unittest.TestCase):
    def test_normalize(self):
        formula1 = "!A"
        formula2 = "!!!A"
        formula3 = "!!!!A"
        self.assertEqual(normalize(formula1), "!A")
        self.assertEqual(normalize(formula2), "!A")
        self.assertEqual(normalize(formula3), "A")

    def test_is_atomic(self):
        self.assertTrue(is_atomic_formula("A"))
        self.assertFalse(is_atomic_formula("!A"))
        self.assertFalse(is_atomic_formula("A&B"))

    def test_evaluate(self):
        self.assertEqual(evaluate_formula("1&0"), '0')
        self.assertEqual(evaluate_formula("1|0"), '1')
        self.assertEqual(evaluate_formula("1&(1&(1&(1&(1&0))))"), '0')
        self.assertEqual(evaluate_formula("0"), '0')
