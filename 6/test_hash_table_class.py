import unittest

from hash_table_class import HashTable, hash_table_from_terms


class TestHashTableClass(unittest.TestCase):
    def test_resize(self):
        table = HashTable()
        self.assertEqual(table.size, 8)
        table.set("A", "B")
        table.set("C", "D")
        table.set("E", "F")
        table.set("G", "H")
        table.set("I", "J")
        table.set("K", "L")
        self.assertEqual(table.size, 16)

    def test_set(self):
        table = HashTable()
        self.assertEqual(str(table), "")
        table.set("A", "B")
        self.assertEqual(str(table), "A - B.")
        table.set("C", "D")
        self.assertEqual(str(table), "A - B.\nC - D.")
        table.set("C", "E")
        self.assertEqual(str(table), "A - B.\nC - D.")

    def test_get(self):
        table = HashTable()
        table.set("A", "B")
        self.assertEqual(table.get("A"), "B")
        self.assertIsNone(table.get("C"))

    def test_delete(self):
        table = HashTable()
        table.set("A", "B")
        table.set("C", "D")
        table.delete("A")
        self.assertEqual(str(table), "C - D.")
        table.delete("E")
        self.assertEqual(str(table), "C - D.")

    def test_hash_table_from_terms(self):
        terms = {
            "A": "B",
            "C": "D",
            "E": "F"
        }
        table = hash_table_from_terms(terms)
        self.assertEqual(str(table), "A - B.\nC - D.\nE - F.")
