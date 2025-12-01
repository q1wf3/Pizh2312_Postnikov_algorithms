"""
Модуль тестирования BST.
Unit-тесты для проверки корректности работы всех операций.
"""
import unittest
from binary_search_tree import BinarySearchTree, TreeNode
from tree_traversal import TreeTraversal


class TestBST(unittest.TestCase):
    """Тесты для бинарного дерева поиска."""

    def setUp(self):
        """Настройка тестового окружения."""
        self.bst = BinarySearchTree()

    def test_insert_and_search(self):
        """Тест вставки и поиска."""
        # Вставка элементов
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(70)
        self.bst.insert(20)
        self.bst.insert(40)
        self.bst.insert(60)
        self.bst.insert(80)

        # Проверка поиска существующих элементов
        self.assertTrue(self.bst.search(50))
        self.assertTrue(self.bst.search(30))
        self.assertTrue(self.bst.search(70))
        self.assertTrue(self.bst.search(20))
        self.assertTrue(self.bst.search(40))
        self.assertTrue(self.bst.search(60))
        self.assertTrue(self.bst.search(80))

        # Проверка поиска несуществующих элементов
        self.assertFalse(self.bst.search(10))
        self.assertFalse(self.bst.search(90))
        self.assertFalse(self.bst.search(55))

    def test_inorder_traversal(self):
        """Тест in-order обхода."""
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(70)
        self.bst.insert(20)
        self.bst.insert(40)
        self.bst.insert(60)
        self.bst.insert(80)

        result = self.bst.to_list_inorder()
        self.assertEqual(result, [20, 30, 40, 50, 60, 70, 80])

    def test_delete(self):
        """Тест удаления элементов."""
        # Создаем дерево
        values = [50, 30, 70, 20, 40, 60, 80]
        for value in values:
            self.bst.insert(value)

        # Удаление листа
        self.bst.delete(20)
        self.assertFalse(self.bst.search(20))
        self.assertEqual(self.bst.to_list_inorder(),
                         [30, 40, 50, 60, 70, 80])

        # Удаление узла с одним потомком
        self.bst.delete(30)
        self.assertFalse(self.bst.search(30))
        self.assertEqual(self.bst.to_list_inorder(),
                         [40, 50, 60, 70, 80])

        # Удаление узла с двумя потомками
        self.bst.delete(50)
        self.assertFalse(self.bst.search(50))
        result = self.bst.to_list_inorder()
        # Минимальный в правом поддереве 60 станет корнем
        self.assertEqual(result, [40, 60, 70, 80])

    def test_find_min_max(self):
        """Тест поиска минимума и максимума."""
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(70)
        self.bst.insert(20)
        self.bst.insert(40)
        self.bst.insert(60)
        self.bst.insert(80)

        min_node = self.bst.find_min()
        self.assertIsNotNone(min_node)
        self.assertEqual(min_node.value, 20)

        max_node = self.bst.find_max()
        self.assertIsNotNone(max_node)
        self.assertEqual(max_node.value, 80)

    def test_is_valid_bst(self):
        """Тест проверки корректности BST."""
        # Корректное BST
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(70)
        self.assertTrue(self.bst.is_valid_bst())

        # Создаем некорректное BST вручную
        invalid_bst = BinarySearchTree()
        invalid_bst.root = TreeNode(50)
        invalid_bst.root.left = TreeNode(60)  # Нарушает свойство BST
        invalid_bst.root.right = TreeNode(70)

        self.assertFalse(invalid_bst.is_valid_bst())

    def test_height(self):
        """Тест вычисления высоты."""
        # Пустое дерево
        self.assertEqual(self.bst.height(), 0)

        # Дерево с одним элементом
        self.bst.insert(50)
        self.assertEqual(self.bst.height(), 0)

        # Дерево с несколькими элементами
        self.bst.insert(30)
        self.bst.insert(70)
        self.assertEqual(self.bst.height(), 1)

        self.bst.insert(20)
        self.bst.insert(40)
        self.assertEqual(self.bst.height(), 2)

    def test_size(self):
        """Тест подсчета количества элементов."""
        self.assertEqual(self.bst.size(), 0)

        self.bst.insert(50)
        self.assertEqual(self.bst.size(), 1)

        self.bst.insert(30)
        self.bst.insert(70)
        self.assertEqual(self.bst.size(), 3)

        self.bst.insert(20)
        self.bst.insert(40)
        self.bst.insert(60)
        self.bst.insert(80)
        self.assertEqual(self.bst.size(), 7)

    def test_traversal_methods(self):
        """Тест различных методов обхода."""
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(70)
        self.bst.insert(20)
        self.bst.insert(40)
        self.bst.insert(60)
        self.bst.insert(80)

        # In-order
        inorder_result = TreeTraversal.inorder_recursive(self.bst.root)
        self.assertEqual(inorder_result, [20, 30, 40, 50, 60, 70, 80])

        # Pre-order
        preorder_result = TreeTraversal.preorder_recursive(self.bst.root)
        self.assertEqual(preorder_result, [50, 30, 20, 40, 70, 60, 80])

        # Post-order
        postorder_result = TreeTraversal.postorder_recursive(self.bst.root)
        self.assertEqual(postorder_result, [20, 40, 30, 60, 80, 70, 50])

        # Итеративный in-order
        iterative_result = TreeTraversal.inorder_iterative(self.bst.root)
        self.assertEqual(iterative_result, [20, 30, 40, 50, 60, 70, 80])

        # Level-order (BFS)
        level_order_result = TreeTraversal.level_order_traversal(self.bst.root)
        self.assertEqual(level_order_result, [50, 30, 70, 20, 40, 60, 80])


class TestEdgeCases(unittest.TestCase):
    """Тесты граничных случаев."""

    def test_empty_tree(self):
        """Тест пустого дерева."""
        bst = BinarySearchTree()
        self.assertFalse(bst.search(10))
        self.assertEqual(bst.height(), 0)
        self.assertEqual(bst.size(), 0)
        self.assertEqual(bst.to_list_inorder(), [])
        self.assertIsNone(bst.find_min())
        self.assertIsNone(bst.find_max())
        # Пустое дерево - валидное BST
        self.assertTrue(bst.is_valid_bst())

    def test_single_element(self):
        """Тест дерева с одним элементом."""
        bst = BinarySearchTree()
        bst.insert(42)

        self.assertTrue(bst.search(42))
        self.assertFalse(bst.search(10))
        self.assertEqual(bst.height(), 0)
        self.assertEqual(bst.size(), 1)
        self.assertEqual(bst.find_min().value, 42)
        self.assertEqual(bst.find_max().value, 42)
        self.assertTrue(bst.is_valid_bst())

    def test_duplicate_values(self):
        """Тест дублирующихся значений."""
        bst = BinarySearchTree()
        bst.insert(50)
        bst.insert(50)  # Дубликат
        bst.insert(30)
        bst.insert(30)  # Дубликат

        # BST не должен содержать дубликатов
        self.assertEqual(bst.size(), 2)  # Только 50 и 30
        self.assertEqual(bst.to_list_inorder(), [30, 50])

    def test_delete_nonexistent(self):
        """Тест удаления несуществующего элемента."""
        bst = BinarySearchTree()
        bst.insert(50)
        bst.insert(30)
        bst.insert(70)

        # Удаление несуществующего элемента не должно вызывать ошибку
        bst.delete(100)
        self.assertEqual(bst.size(), 3)
        self.assertEqual(bst.to_list_inorder(), [30, 50, 70])


if __name__ == "__main__":
    unittest.main(verbosity=2)
