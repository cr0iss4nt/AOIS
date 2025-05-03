import unittest

from perfect_normal_form import build_perfect_disjunctive_normal_form, build_perfect_conjunctive_normal_form


class TestPerfectNormalForm(unittest.TestCase):
    def test_build_perfect_disjunctive_normal_form(self):
        self.assertEqual(build_perfect_disjunctive_normal_form("A"), "(A)")
        self.assertEqual(build_perfect_disjunctive_normal_form("A&B"), "(A & B)")
        self.assertEqual(build_perfect_disjunctive_normal_form("(A&B)|!C"),
                         "(!A & !B & !C) | (!A & B & !C) | (A & !B & !C) | (A & B & !C) | (A & B & C)")

    def test_build_perfect_conjunctive_normal_form(self):
        self.assertEqual(build_perfect_conjunctive_normal_form("A"), "(A)")
        self.assertEqual(build_perfect_conjunctive_normal_form("A&B"), "(A | B) & (A | !B) & (!A | B)")
        self.assertEqual(build_perfect_conjunctive_normal_form("(A&B)|!C"),
                         "(A | B | !C) & (A | !B | !C) & (!A | B | !C)")