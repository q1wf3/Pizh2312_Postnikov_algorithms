"""
Модуль для визуализации куч в виде деревьев.
"""

from heap import MinHeap


def heap_to_tree_str(heap, index=0, prefix="", is_left=True):
    """
    Рекурсивное преобразование кучи в строковое представление дерева.

    Args:
        heap: Объект кучи
        index: Текущий индекс в куче
        prefix: Префикс для отступов
        is_left: Является ли узел левым потомком

    Returns:
        str: Строковое представление дерева
    """
    if index >= len(heap.heap):
        return ""

    result = ""
    # Добавляем правого потомка
    right_idx = 2 * index + 2
    if right_idx < len(heap.heap):
        result += heap_to_tree_str(
            heap, right_idx,
            prefix + ("│   " if is_left else "    "),
            False
        )

    # Добавляем текущий узел
    node_str = prefix + ("└── " if is_left else "┌── ")
    result += node_str + str(heap.heap[index]) + "\n"

    # Добавляем левого потомка
    left_idx = 2 * index + 1
    if left_idx < len(heap.heap):
        result += heap_to_tree_str(
            heap, left_idx,
            prefix + ("    " if is_left else "│   "),
            True
        )

    return result


def print_heap_tree(heap):
    """
    Вывод кучи в виде дерева.

    Args:
        heap: Объект кучи
    """
    if not heap.heap:
        print("(пустая куча)")
        return

    print("Структура кучи:")
    print(heap_to_tree_str(heap))


def visualize_heap_operations():
    """Демонстрация операций с кучей с визуализацией."""
    print("Демонстрация операций с кучей")
    print("-" * 50)

    heap = MinHeap()

    print("1. Начальное состояние:")
    print_heap_tree(heap)

    print("2. Вставка элемента 10:")
    heap.insert(10)
    print_heap_tree(heap)

    print("3. Вставка элемента 5:")
    heap.insert(5)
    print_heap_tree(heap)

    print("4. Вставка элемента 15:")
    heap.insert(15)
    print_heap_tree(heap)

    print("5. Вставка элемента 3:")
    heap.insert(3)
    print_heap_tree(heap)

    print("6. Вставка элемента 7:")
    heap.insert(7)
    print_heap_tree(heap)

    print("7. Извлечение корня (должен быть 3):")
    root = heap.extract()
    print(f"Извлеченный элемент: {root}")
    print_heap_tree(heap)

    print("8. Извлечение корня (должен быть 5):")
    root = heap.extract()
    print(f"Извлеченный элемент: {root}")
    print_heap_tree(heap)

    print("9. Построение кучи из массива [9, 5, 7, 1, 3, 8]:")
    heap.build_heap([9, 5, 7, 1, 3, 8])
    print_heap_tree(heap)

    print("10. Проверка свойства кучи:")
    print(f"Куча корректна: {heap.is_valid()}")


def print_array_as_heap(arr):
    """
    Вывод массива как кучи в виде дерева.

    Args:
        arr: Массив для представления в виде кучи
    """
    class TempHeap:
        def __init__(self, arr):
            self.heap = arr

    temp_heap = TempHeap(arr)
    print_heap_tree(temp_heap)


if __name__ == "__main__":
    visualize_heap_operations()
