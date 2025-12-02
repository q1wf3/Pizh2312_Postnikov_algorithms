"""
Модуль реализации приоритетной очереди на основе кучи.
"""

from heap import MinHeap


class PriorityItem:
    """Элемент приоритетной очереди."""

    def __init__(self, item, priority):
        """
        Инициализация элемента.

        Args:
            item: Данные элемента
            priority: Приоритет (меньше = выше приоритет)
        """
        self.item = item
        self.priority = priority

    def __lt__(self, other):
        """Сравнение для min-heap."""
        return self.priority < other.priority

    def __eq__(self, other):
        """Проверка на равенство."""
        if not isinstance(other, PriorityItem):
            return False
        return self.priority == other.priority

    def __repr__(self):
        """Строковое представление."""
        return f"PriorityItem(item={self.item}, priority={self.priority})"


class PriorityQueue:
    """Приоритетная очередь на основе min-heap."""

    def __init__(self):
        """Инициализация пустой очереди."""
        self.heap = MinHeap()

    def enqueue(self, item, priority):
        """
        Добавление элемента в очередь.

        Args:
            item: Данные элемента
            priority: Приоритет (меньше = выше приоритет)

        Сложность: O(log n)
        """
        priority_item = PriorityItem(item, priority)
        self.heap.insert(priority_item)

    def dequeue(self):
        """
        Извлечение элемента с наивысшим приоритетом.

        Returns:
            Элемент с наивысшим приоритетом.

        Raises:
            IndexError: Если очередь пуста.

        Сложность: O(log n)
        """
        priority_item = self.heap.extract()
        return priority_item.item

    def peek(self):
        """
        Просмотр элемента с наивысшим приоритетом без извлечения.

        Returns:
            Элемент с наивысшим приоритетом.

        Raises:
            IndexError: Если очередь пуста.

        Сложность: O(1)
        """
        priority_item = self.heap.peek()
        return priority_item.item

    def is_empty(self):
        """
        Проверка на пустоту очереди.

        Returns:
            bool: True если очередь пуста.

        Сложность: O(1)
        """
        return len(self.heap) == 0

    def __len__(self):
        """
        Количество элементов в очереди.

        Returns:
            int: Количество элементов.

        Сложность: O(1)
        """
        return len(self.heap)

    def __str__(self):
        """Строковое представление."""
        return f"PriorityQueue(size={len(self)})"
