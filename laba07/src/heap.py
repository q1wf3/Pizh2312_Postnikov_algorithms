"""
Модуль реализации структуры данных "Куча" (Heap).
Реализованы MinHeap, MaxHeap и универсальный Heap.
"""


class Heap:
    """Универсальная куча (min-heap или max-heap)."""

    def __init__(self, is_min=True):
        """
        Инициализация кучи.

        Args:
            is_min (bool): True для min-heap, False для max-heap.

        Сложность: O(1)
        """
        self.heap = []
        self.is_min = is_min

    def __len__(self):
        """Возвращает количество элементов в куче. O(1)"""
        return len(self.heap)

    def _compare(self, a, b):
        """
        Сравнивает два элемента в зависимости от типа кучи.

        Args:
            a: Первый элемент
            b: Второй элемент

        Returns:
            bool: True если a и b находятся в правильном порядке для кучи.

        Сложность: O(1)
        """
        if self.is_min:
            return a < b
        return a > b

    def _sift_up(self, index):
        """
        Всплытие элемента на нужную позицию (просеивание вверх).

        Args:
            index (int): Индекс элемента для всплытия.

        Сложность: O(log n)
        """
        parent = (index - 1) // 2
        while index > 0 and self._compare(self.heap[index], self.heap[parent]):
            self.heap[index], self.heap[parent] = (
                self.heap[parent], self.heap[index]
            )
            index = parent
            parent = (index - 1) // 2

    def _sift_down(self, index):
        """
        Погружение элемента на нужную позицию (просеивание вниз).

        Args:
            index (int): Индекс элемента для погружения.

        Сложность: O(log n)
        """
        size = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest_or_largest = index

            if left < size and self._compare(
                self.heap[left], self.heap[smallest_or_largest]
            ):
                smallest_or_largest = left

            if right < size and self._compare(
                self.heap[right], self.heap[smallest_or_largest]
            ):
                smallest_or_largest = right

            if smallest_or_largest != index:
                self.heap[index], self.heap[smallest_or_largest] = (
                    self.heap[smallest_or_largest], self.heap[index]
                )
                index = smallest_or_largest
            else:
                break

    def insert(self, value):
        """
        Вставка элемента в кучу.

        Args:
            value: Значение для вставки.

        Сложность: O(log n)
        """
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def extract(self):
        """
        Извлечение корневого элемента.

        Returns:
            Значение корневого элемента.

        Raises:
            IndexError: Если куча пуста.

        Сложность: O(log n)
        """
        if not self.heap:
            raise IndexError("Куча пуста")

        root = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            self._sift_down(0)

        return root

    def peek(self):
        """
        Просмотр корневого элемента без извлечения.

        Returns:
            Значение корневого элемента.

        Raises:
            IndexError: Если куча пуста.

        Сложность: O(1)
        """
        if not self.heap:
            raise IndexError("Куча пуста")
        return self.heap[0]

    def build_heap(self, array):
        """
        Построение кучи из произвольного массива за O(n).

        Args:
            array (list): Исходный массив.

        Сложность: O(n)
        """
        self.heap = array[:]
        n = len(self.heap)

        # Начинаем с последнего нелистового узла
        for i in range(n // 2 - 1, -1, -1):
            self._sift_down(i)

    def heapify(self):
        """Преобразование текущего массива в кучу. O(n)"""
        self.build_heap(self.heap)

    def is_valid(self):
        """
        Проверка свойства кучи.

        Returns:
            bool: True если свойство кучи выполняется.

        Сложность: O(n)
        """
        n = len(self.heap)
        for i in range(n):
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and not self._compare(self.heap[i], self.heap[left]):
                return False
            if right < n and not self._compare(self.heap[i], self.heap[right]):
                return False
        return True

    def __str__(self):
        """Строковое представление кучи."""
        return f"Heap({self.heap}, is_min={self.is_min})"


class MinHeap(Heap):
    """Минимальная куча (min-heap)."""

    def __init__(self):
        """Инициализация min-heap."""
        super().__init__(is_min=True)


class MaxHeap(Heap):
    """Максимальная куча (max-heap)."""

    def __init__(self):
        """Инициализация max-heap."""
        super().__init__(is_min=False)
