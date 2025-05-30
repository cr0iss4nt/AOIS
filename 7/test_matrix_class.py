import unittest
from copy import deepcopy

from matrix_class import Matrix


class TestMatrixClass(unittest.TestCase):
    def test_get_word(self):
        m = Matrix()

        try:
            word = m.get_word(-1)
        except ValueError:
            pass
        try:
            word = m.get_word(16)
        except ValueError:
            pass

        word = m.get_word(0)
        self.assertEqual(len(word),16)
        self.assertTrue(all(i in ['0','1'] for i in word))

    def test_get_diagonal(self):
        m = Matrix()

        try:
            diagonal = m.get_diagonal(-1)
        except ValueError:
            pass
        try:
            diagonal = m.get_diagonal(16)
        except ValueError:
            pass

        diagonal = m.get_diagonal(0)
        self.assertEqual(len(diagonal),16)
        self.assertTrue(all(i in ['0','1'] for i in diagonal))

    def test_replace_word(self):
        m = Matrix()

        try:
            m.replace_word(-1, "1111111111111111")
        except ValueError:
            pass
        try:
            m.replace_word(16, "1111111111111111")
        except ValueError:
            pass
        try:
            m.replace_word(15, "a111111111111111")
        except ValueError:
            pass
        try:
            m.replace_word(15, "111111111111111")
        except ValueError:
            pass

        m.replace_word(0, "1111111111111111")
        word = m.get_word(0)
        self.assertEqual(word, "1111111111111111")

    def test_replace_diagonal(self):
        m = Matrix()

        try:
            m.replace_diagonal(-1, "1111111111111111")
        except ValueError:
            pass
        try:
            m.replace_diagonal(16, "1111111111111111")
        except ValueError:
            pass
        try:
            m.replace_diagonal(15, "a111111111111111")
        except ValueError:
            pass
        try:
            m.replace_diagonal(15, "111111111111111")
        except ValueError:
            pass

        m.replace_diagonal(0, "1111111111111111")
        diagonal = m.get_diagonal(0)
        self.assertEqual(diagonal, "1111111111111111")

    def test_logic(self):
        m = Matrix()

        try:
            m.logic(-1, 1, 15, "0")
        except ValueError:
            pass
        try:
            m.logic(0, 16, 15, "0")
        except ValueError:
            pass
        try:
            m.logic(0, 15, 16, "0")
        except ValueError:
            pass
        try:
            m.logic(0, 1, 15, "1")
        except ValueError:
            pass

        m.logic(0, 1, 15, "0")
        diagonal = m.get_diagonal(15)
        self.assertEqual(diagonal, "0000000000000000")

        m.logic(0, 1, 14, "15")
        diagonal = m.get_diagonal(14)
        self.assertEqual(diagonal, "1111111111111111")

        diagonal1 = m.get_diagonal(13)
        m.logic(0, 13, 12, "5")
        diagonal2 = m.get_diagonal(12)
        self.assertEqual(diagonal1, diagonal2)

        diagonal1 = m.get_diagonal(11)
        m.logic(0, 11, 10, "10")
        diagonal2 = m.get_diagonal(10)
        inverted_diagonal2 = ''.join('1' if i == '0' else '0' for i in diagonal2)
        self.assertEqual(diagonal1, inverted_diagonal2)

    def test_summarize_words(self):
        m1 = Matrix()
        m2 = deepcopy(m1)

        try:
            m2.summarize_words("0001")
        except ValueError:
            pass
        try:
            m2.summarize_words("a01")
        except ValueError:
            pass

        m2.summarize_words("001")
        self.assertTrue(m1 != m2)

    def test_search_by_match(self):
        m = Matrix()

        try:
            best_candidate_index, max_matches = m.search_by_match("101010101010101a")
        except ValueError:
            pass
        try:
            best_candidate_index, max_matches = m.search_by_match("10101010101010101")
        except ValueError:
            pass

        best_candidate_index, max_matches = m.search_by_match("1010101010101010")
        self.assertIn(best_candidate_index, range(-1,16))
        self.assertIn(max_matches, range(-1, 16))