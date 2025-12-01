"""
Unit-тесты для проверки корректности работы хеш-таблиц.
"""

import unittest
import sys
import os
from hash_functions import simple_hash, polynomial_hash, djb2_hash
from hash_table_chaining import HashTableChaining
from hash_table_open_addressing import HashTableOpenAddressing

# Добавляем путь для импорта модулей
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)


class TestHashFunctions(unittest.TestCase):
    """Тесты хеш-функций."""

    def test_simple_hash(self):
        """Тест простой хеш-функции."""
        self.assertEqual(simple_hash("test", 100),
                         simple_hash("test", 100))
        self.assertNotEqual(simple_hash("test", 100),
                            simple_hash("test2", 100))

    def test_polynomial_hash(self):
        """Тест полиномиальной хеш-функции."""
        h1 = polynomial_hash("hello", 100)
        h2 = polynomial_hash("hello", 100)
        self.assertEqual(h1, h2)
        h3 = polynomial_hash("world", 100)
        self.assertNotEqual(h1, h3)

    def test_djb2_hash(self):
        """Тест хеш-функции DJB2."""
        self.assertEqual(djb2_hash("test", 100),
                         djb2_hash("test", 100))
        self.assertNotEqual(djb2_hash("test", 100),
                            djb2_hash("test2", 100))


class TestHashTableChaining(unittest.TestCase):
    """Тесты таблицы цепочек."""

    def setUp(self):
        self.table = HashTableChaining(initial_size=10)

    def test_insert_search(self):
        """Тест вставки и поиска."""
        self.table.insert("k1", "v1")
        self.table.insert("k2", "v2")
        self.assertEqual(self.table.search("k1"), "v1")
        self.assertEqual(self.table.search("k2"), "v2")
        self.assertIsNone(self.table.search("unknown"))

    def test_update(self):
        """Тест обновления значения."""
        self.table.insert("k", "v")
        self.table.insert("k", "new")
        self.assertEqual(self.table.search("k"), "new")

    def test_delete(self):
        """Тест удаления."""
        self.table.insert("k", "v")
        self.assertTrue(self.table.delete("k"))
        self.assertIsNone(self.table.search("k"))
        self.assertFalse(self.table.delete("k"))

    def test_collisions(self):
        """Тест обработки коллизий."""
        t = HashTableChaining(initial_size=2)
        t.insert("a", 1)
        t.insert("b", 2)
        t.insert("c", 3)
        self.assertEqual(t.search("a"), 1)
        self.assertEqual(t.search("b"), 2)
        self.assertEqual(t.search("c"), 3)


class TestHashTableOpenAddressing(unittest.TestCase):
    """Тесты открытой адресации."""

    def test_linear(self):
        """Тест линейного пробирования."""
        t = HashTableOpenAddressing(initial_size=5, probe_method='linear')
        t.insert("a", 1)
        t.insert("b", 2)
        t.insert("c", 3)
        self.assertEqual(t.search("a"), 1)

    def test_double(self):
        """Тест двойного хеширования."""
        t = HashTableOpenAddressing(initial_size=5, probe_method='double')
        t.insert("a", 1)
        t.insert("b", 2)
        t.insert("c", 3)
        self.assertEqual(t.search("b"), 2)

    def test_delete(self):
        """Тест удаления."""
        t = HashTableOpenAddressing(initial_size=5)
        t.insert("a", 1)
        t.insert("b", 2)
        t.delete("a")
        self.assertIsNone(t.search("a"))
        self.assertEqual(t.search("b"), 2)
        t.insert("c", 3)
        self.assertEqual(t.search("c"), 3)


class TestPerformance(unittest.TestCase):
    """Тесты масштабирования."""

    def test_resize(self):
        """Тест операции масштабирования."""
        t = HashTableChaining(initial_size=5, load_factor=0.5)

        for i in range(3):
            t.insert(f"k{i}", f"v{i}")

        old_size = t.size
        t.insert("trigger", "resize")

        self.assertGreater(t.size, old_size)

        for i in range(3):
            self.assertEqual(t.search(f"k{i}"), f"v{i}")
        self.assertEqual(t.search("trigger"), "resize")


if __name__ == '__main__':
    unittest.main()
