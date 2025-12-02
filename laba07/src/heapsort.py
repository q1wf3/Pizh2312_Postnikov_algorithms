"""
Модуль реализации сортировки кучей (Heapsort).
Реализованы обычная и in-place версии.
"""


def heapsort(array):
    """
    Сортировка кучей с использованием дополнительной памяти.

    Args:
        array (list): Массив для сортировки.

    Returns:
        list: Отсортированный массив.

    Сложность: O(n log n)
    """
    # Создаем min-heap
    heap = []

    # Вставляем все элементы в кучу: O(n log n)
    for item in array:
        heap.append(item)
        # Просеиваем вверх
        i = len(heap) - 1
        while i > 0:
            parent = (i - 1) // 2
            if heap[i] < heap[parent]:
                heap[i], heap[parent] = heap[parent], heap[i]
                i = parent
            else:
                break

    # Извлекаем элементы из кучи: O(n log n)
    result = []
    while heap:
        # Извлекаем корень
        root = heap[0]
        last = heap.pop()
        if heap:
            heap[0] = last
            # Просеиваем вниз
            i = 0
            n = len(heap)
            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                smallest = i

                if left < n and heap[left] < heap[smallest]:
                    smallest = left
                if right < n and heap[right] < heap[smallest]:
                    smallest = right

                if smallest != i:
                    heap[i], heap[smallest] = heap[smallest], heap[i]
                    i = smallest
                else:
                    break
        result.append(root)

    return result


def heapsort_inplace(array):
    """
    In-place сортировка кучей (пирамидальная сортировка).

    Args:
        array (list): Массив для сортировки (изменяется на месте).

    Returns:
        list: Отсортированный массив.

    Сложность: O(n log n)
    Память: O(1)
    """
    def sift_down(arr, start, end):
        """
        Просеивание элемента вниз.

        Args:
            arr: Массив
            start: Индекс корня поддерева
            end: Конечный индекс
        """
        root = start
        while True:
            child = 2 * root + 1  # Левый потомок
            if child > end:
                break

            # Выбираем большего потомка
            if child + 1 <= end and arr[child] < arr[child + 1]:
                child += 1

            # Если корень меньше потомка, меняем местами
            if arr[root] < arr[child]:
                arr[root], arr[child] = arr[child], arr[root]
                root = child
            else:
                break

    n = len(array)

    # Шаг 1: Построение max-heap из массива (heapify)
    # Начинаем с последнего нелистового узла
    for i in range(n // 2 - 1, -1, -1):
        sift_down(array, i, n - 1)

    # Шаг 2: Извлечение элементов из кучи
    for i in range(n - 1, 0, -1):
        # Меняем корень (максимальный элемент) с последним элементом
        array[0], array[i] = array[i], array[0]
        # Восстанавливаем свойство кучи для уменьшенной кучи
        sift_down(array, 0, i - 1)

    return array


def heap_sort_min(array):
    """
    Сортировка кучей с использованием класса MinHeap.

    Args:
        array (list): Массив для сортировки.

    Returns:
        list: Отсортированный по возрастанию массив.

    Сложность: O(n log n)
    """
    from heap import MinHeap

    heap = MinHeap()
    heap.build_heap(array)

    result = []
    while len(heap) > 0:
        result.append(heap.extract())

    return result
