import unittest

from minimization_gluing import minimize_implicant_check, minimize_chart
from perfect_normal_form import build_perfect_disjunctive_normal_form, build_perfect_conjunctive_normal_form


class TestMinimizationGluing(unittest.TestCase):
    def test_minimize_pnf_implicant_check(self):
        sdnf = build_perfect_disjunctive_normal_form("(A&B)|!C")
        sknf = build_perfect_conjunctive_normal_form("(A&B)|!C")
        minimized_dnf = minimize_implicant_check(sdnf, is_conjunction=False)
        minimized_knf = minimize_implicant_check(sknf, is_conjunction=True)
        self.assertEqual(sorted(minimized_dnf.split(' | ')), ["(!C)", "(A & B)"])
        self.assertEqual(sorted(minimized_knf.split(' & ')), ["(A | !C)", "(B | !C)"])

    def test_minimize_pnf_chart(self):
        sdnf = build_perfect_disjunctive_normal_form("(A&B)|!C")
        sknf = build_perfect_conjunctive_normal_form("(A&B)|!C")
        minimized_dnf = minimize_chart(sdnf, is_conjunction=False)
        minimized_knf = minimize_chart(sknf, is_conjunction=True)
        self.assertEqual(sorted(minimized_dnf.split(' | ')),["(!C)","(A & B)"])
        self.assertEqual(sorted(minimized_knf.split(' & ')), ["(A | !C)","(B | !C)"])
