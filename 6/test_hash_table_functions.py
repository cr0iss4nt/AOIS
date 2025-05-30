import unittest

from hash_table_class import HashTable
from hash_table_functions import normalize_term_name, table_term


class TestHashTableFunctions(unittest.TestCase):
    def test_normalize_term_name(self):
        self.assertEqual(normalize_term_name("кЛЕтКА"), "Клетка")
        self.assertEqual(normalize_term_name("ДНК"), "Днк")

    def test_table_term(self):
        table = HashTable()
        table.set("A", "B")
        self.assertEqual(table_term(table, "A"), "A - B.")
        self.assertEqual(table_term(table, "C"), "C - None.")
