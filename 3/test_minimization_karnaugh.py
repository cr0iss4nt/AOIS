import unittest

from minimization_karnaugh import minimize_karnaugh
from perfect_normal_form import build_perfect_disjunctive_normal_form, build_perfect_conjunctive_normal_form


class TestKarnaugh(unittest.TestCase):
    def test_minimize_karnaugh(self):
        sdnf = build_perfect_disjunctive_normal_form("(A&B)|!C")
        sknf = build_perfect_conjunctive_normal_form("(A&B)|!C")
        minimized_dnf = minimize_karnaugh(sdnf, is_conjunction=False)
        minimized_knf = minimize_karnaugh(sknf, is_conjunction=True)
        self.assertTrue(minimized_dnf == "(!C) | (A & B)" or minimized_dnf == "(A & B) | (!C)")
        self.assertTrue(minimized_knf == "(A | !C) & (B | !C)" or minimized_knf == "(B | !C) & (A | !C)")

    def test_minimize_karnaugh_for_five(self):
        sdnf = build_perfect_disjunctive_normal_form("(A|B)&(C|D)&E")
        sknf = build_perfect_conjunctive_normal_form("(A|B)&(C|D)&E")
        minimized_dnf = minimize_karnaugh(sdnf, is_conjunction=False)
        minimized_knf = minimize_karnaugh(sknf, is_conjunction=True)
        self.assertEqual(minimized_dnf, "(B & C & E) | (B & D & E) | (A & D & E) | (A & C & E)")
        self.assertEqual(minimized_knf, "(A | B) & (E) & (C | D)")