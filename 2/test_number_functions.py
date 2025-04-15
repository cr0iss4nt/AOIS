import unittest

from number_functions import index_form, number_perfect_conjunctive_normal_form, number_perfect_disjunctive_normal_form


class TestNumberFunctions(unittest.TestCase):
    def test_index_form(self):
        print('1')
        formula = "(A&B)|!C"
        self.assertEqual(index_form(formula), 171)

    def test_number_perfect_conjunctive_normal_form(self):
        print('2')
        formula = "(A&B)|!C"
        self.assertEqual(number_perfect_conjunctive_normal_form(formula), [1, 3, 5])

    def test_number_perfect_disjunctive_normal_form(self):
        print('3')
        formula = "(A&B)|!C"
        self.assertEqual(number_perfect_disjunctive_normal_form(formula), [0, 2, 4, 6, 7])
