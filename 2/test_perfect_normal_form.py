import unittest

from perfect_normal_form import build_perfect_conjunctive_normal_form, build_perfect_disjunctive_normal_form


class TestPerfectNormalForm(unittest.TestCase):
    def test_perfect_conjunctive_normal_form(self):
        formula = "(A&B)|!C"
        self.assertEqual(build_perfect_conjunctive_normal_form(formula), "(A | B | !C) & (A | !B | !C) & (!A | B | !C)")

    def test_perfect_disjunctive_normal_form(self):
        formula = "(A&B)|!C"
        self.assertEqual(build_perfect_disjunctive_normal_form(formula),
                         "(!A & !B & !C) | (!A & B & !C) | (A & !B & !C) | (A & B & !C) | (A & B & C)")
