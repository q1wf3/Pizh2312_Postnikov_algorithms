"""
Unit-тесты для проверки корректности работы куч,
сортировки и приоритетной очереди.
"""

import unittest
import random
from heap import MinHeap, MaxHeap, Heap
from heapsort import heapsort, heapsort_inplace, heap_sort_min
from priority_queue import PriorityQueue, PriorityItem


class TestHeap(unittest.TestCase):
    """Тесты для класса Heap."""

    def test_min_heap_insert_extract(self):
        """Тест вставки и извлечения в min-heap."""
        heap = MinHeap()
        test_data = [5, 3, 8, 1, 2, 7]

        for item in test_data:
            heap.insert(item)

        # Проверяем свойство кучи
        self.assertTrue(heap.is_valid())

        # Извлекаем элементы в отсортированном порядке
        extracted = []
        while len(heap) > 0:
            extracted.append(heap.extract())

        # Для min-heap извлеченные элементы должны быть отсортированы
        self.assertEqual(extracted, sorted(test_data))

    def test_max_heap_insert_extract(self):
        """Тест вставки и извлечения в max-heap."""
        heap = MaxHeap()
        test_data = [5, 3, 8, 1, 2, 7]

        for item in test_data:
            heap.insert(item)

        # Проверяем свойство кучи
        self.assertTrue(heap.is_valid())

        # Извлекаем элементы
        extracted = []
        while len(heap) > 0:
            extracted.append(heap.extract())

        # Для max-heap извлеченные элементы должны быть отсортированы
        self.assertEqual(extracted, sorted(test_data, reverse=True))

    def test_build_heap_min(self):
        """Тест построения min-heap из массива."""
        test_data = [9, 5, 7, 1, 3, 8, 2, 6, 4]
        heap = MinHeap()
        heap.build_heap(test_data)

        # Проверяем свойство кучи
        self.assertTrue(heap.is_valid())

        # Проверяем, что корень - минимальный элемент
        self.assertEqual(heap.peek(), min(test_data))

    def test_build_heap_max(self):
        """Тест построения max-heap из массива."""
        test_data = [9, 5, 7, 1, 3, 8, 2, 6, 4]
        heap = MaxHeap()
        heap.build_heap(test_data)

        # Проверяем свойство кучи
        self.assertTrue(heap.is_valid())

        # Проверяем, что корень - максимальный элемент
        self.assertEqual(heap.peek(), max(test_data))

    def test_heap_operations_complexity_check(self):
        """Тест основных операций кучи."""
        heap = MinHeap()

        # Тест вставки
        heap.insert(10)
        self.assertEqual(heap.peek(), 10)

        heap.insert(5)
        self.assertEqual(heap.peek(), 5)

        heap.insert(15)
        self.assertEqual(heap.peek(), 5)

        # Тест извлечения
        self.assertEqual(heap.extract(), 5)
        self.assertEqual(heap.extract(), 10)
        self.assertEqual(heap.extract(), 15)

        # Тест исключения при извлечении из пустой кучи
        with self.assertRaises(IndexError):
            heap.extract()

    def test_large_heap(self):
        """Тест с большим количеством элементов."""
        heap = MinHeap()
        n = 1000
        random_data = [random.randint(1, 10000) for _ in range(n)]

        for item in random_data:
            heap.insert(item)

        self.assertTrue(heap.is_valid())

        extracted = []
        while len(heap) > 0:
            extracted.append(heap.extract())

        self.assertEqual(extracted, sorted(random_data))

    def test_universal_heap(self):
        """Тест универсальной кучи."""
        # Min-heap
        heap_min = Heap(is_min=True)
        heap_min.insert(5)
        heap_min.insert(3)
        heap_min.insert(7)
        self.assertEqual(heap_min.peek(), 3)

        # Max-heap
        heap_max = Heap(is_min=False)
        heap_max.insert(5)
        heap_max.insert(3)
        heap_max.insert(7)
        self.assertEqual(heap_max.peek(), 7)


class TestHeapsort(unittest.TestCase):
    """Тесты для сортировки кучей."""

    def test_heapsort_basic(self):
        """Базовый тест сортировки кучей."""
        test_data = [9, 5, 7, 1, 3, 8, 2, 6, 4]
        sorted_data = heapsort(test_data)
        self.assertEqual(sorted_data, sorted(test_data))

    def test_heapsort_inplace_basic(self):
        """Базовый тест in-place сортировки кучей."""
        test_data = [9, 5, 7, 1, 3, 8, 2, 6, 4]
        original = test_data[:]
        result = heapsort_inplace(test_data)

        self.assertEqual(result, sorted(original))
        # Проверяем, что сортировка была in-place
        self.assertEqual(test_data, sorted(original))

    def test_heapsort_min_heap(self):
        """Тест сортировки с использованием MinHeap."""
        test_data = [9, 5, 7, 1, 3, 8, 2, 6, 4]
        sorted_data = heap_sort_min(test_data)
        self.assertEqual(sorted_data, sorted(test_data))

    def test_heapsort_empty(self):
        """Тест сортировки пустого массива."""
        self.assertEqual(heapsort([]), [])
        self.assertEqual(heapsort_inplace([]), [])

    def test_heapsort_single(self):
        """Тест сортировки массива из одного элемента."""
        self.assertEqual(heapsort([5]), [5])
        self.assertEqual(heapsort_inplace([5]), [5])

    def test_heapsort_sorted(self):
        """Тест сортировки уже отсортированного массива."""
        test_data = [1, 2, 3, 4, 5]
        self.assertEqual(heapsort(test_data), test_data)
        self.assertEqual(heapsort_inplace(test_data), test_data)

    def test_heapsort_reverse_sorted(self):
        """Тест сортировки отсортированного в обратном порядке."""
        test_data = [5, 4, 3, 2, 1]
        self.assertEqual(heapsort(test_data), [1, 2, 3, 4, 5])
        self.assertEqual(heapsort_inplace(test_data), [1, 2, 3, 4, 5])

    def test_heapsort_duplicates(self):
        """Тест сортировки массива с дубликатами."""
        test_data = [5, 2, 5, 1, 2, 3, 5, 1]
        self.assertEqual(heapsort(test_data), sorted(test_data))
        self.assertEqual(heapsort_inplace(test_data), sorted(test_data))

    def test_heapsort_large_random(self):
        """Тест сортировки большого случайного массива."""
        n = 1000
        random_data = [random.randint(1, 10000) for _ in range(n)]

        # Тестируем все три реализации
        result1 = heapsort(random_data)
        self.assertEqual(result1, sorted(random_data))

        # Для in-place сортировки нужна копия
        random_data_copy = random_data[:]
        result2 = heapsort_inplace(random_data_copy)
        self.assertEqual(result2, sorted(random_data))

        result3 = heap_sort_min(random_data)
        self.assertEqual(result3, sorted(random_data))


class TestPriorityQueue(unittest.TestCase):
    """Тесты для приоритетной очереди."""

    def test_priority_queue_basic(self):
        """Базовый тест приоритетной очереди."""
        pq = PriorityQueue()

        # Добавляем элементы с разными приоритетами
        pq.enqueue("Task 1", 3)
        pq.enqueue("Task 2", 1)  # Самый высокий приоритет
        pq.enqueue("Task 3", 5)  # Самый низкий приоритет
        pq.enqueue("Task 4", 2)

        # Проверяем порядок извлечения
        self.assertEqual(pq.dequeue(), "Task 2")  # Приоритет 1
        self.assertEqual(pq.dequeue(), "Task 4")  # Приоритет 2
        self.assertEqual(pq.dequeue(), "Task 1")  # Приоритет 3
        self.assertEqual(pq.dequeue(), "Task 3")  # Приоритет 5

    def test_priority_queue_peek(self):
        """Тест просмотра без извлечения."""
        pq = PriorityQueue()

        pq.enqueue("Task A", 2)
        pq.enqueue("Task B", 1)

        # Peek должен показывать элемент с наивысшим приоритетом
        self.assertEqual(pq.peek(), "Task B")
        self.assertEqual(len(pq), 2)  # Размер не должен измениться

        # После извлечения - следующий элемент
        self.assertEqual(pq.dequeue(), "Task B")
        self.assertEqual(pq.peek(), "Task A")

    def test_priority_queue_empty(self):
        """Тест пустой очереди."""
        pq = PriorityQueue()

        self.assertTrue(pq.is_empty())
        self.assertEqual(len(pq), 0)

        with self.assertRaises(IndexError):
            pq.dequeue()

        with self.assertRaises(IndexError):
            pq.peek()

    def test_priority_queue_same_priority(self):
        """Тест с одинаковыми приоритетами."""
        pq = PriorityQueue()

        # При одинаковых приоритетах порядок может быть FIFO
        pq.enqueue("Task 1", 1)
        pq.enqueue("Task 2", 1)
        pq.enqueue("Task 3", 1)

        # Все три задачи должны быть извлечены
        tasks = set()
        while not pq.is_empty():
            tasks.add(pq.dequeue())

        self.assertEqual(tasks, {"Task 1", "Task 2", "Task 3"})

    def test_priority_queue_large(self):
        """Тест с большим количеством элементов."""
        pq = PriorityQueue()
        n = 100

        # Добавляем элементы в случайном порядке
        for i in range(n):
            priority = random.randint(1, 100)
            pq.enqueue(f"Task {i}", priority)

        # Извлекаем все элементы
        extracted_count = 0

        while not pq.is_empty():
            pq.dequeue()
            extracted_count += 1

        self.assertEqual(extracted_count, n)

    def test_priority_item_comparison(self):
        """Тест сравнения элементов приоритетной очереди."""
        item1 = PriorityItem("Task 1", 1)
        item2 = PriorityItem("Task 2", 2)
        item3 = PriorityItem("Task 3", 1)

        self.assertTrue(item1 < item2)  # 1 < 2
        self.assertFalse(item2 < item1)  # 2 < 1 - ложь
        self.assertEqual(item1, item3)  # Приоритеты равны


if __name__ == '__main__':
    unittest.main()
