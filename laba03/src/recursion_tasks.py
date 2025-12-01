"""
Модуль с практическими задачами на рекурсию.
"""


def binary_search_recursive(arr, target, left=0, right=None):
    """
    Рекурсивный бинарный поиск в отсортированном массиве.

    Args:
        arr (list): Отсортированный массив.
        target: Искомый элемент.
        left (int): Левая граница поиска.
        right (int): Правая граница поиска.

    Returns:
        int: Индекс элемента или -1 если не найден.

    Временная сложность: O(log n)
    Глубина рекурсии: O(log n)
    """
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def hanoi_towers(n, source="A", auxiliary="B", target="C"):
    """
    Решение задачи о Ханойских башнях.

    Args:
        n (int): Количество дисков.
        source (str): Стержень-источник.
        auxiliary (str): Вспомогательный стержень.
        target (str): Стержень-цель.

    Returns:
        list: Список ходов для решения.

    Временная сложность: O(2^n)
    Глубина рекурсии: O(n)
    """
    if n == 0:
        return []

    moves = []

    def hanoi_recursive(num, src, aux, dst):
        if num == 1:
            moves.append(f"Переместить диск 1 с {src} на {dst}")
        else:
            # Переместить n-1 дисков с src на aux
            hanoi_recursive(num - 1, src, dst, aux)
            # Переместить самый большой диск с src на dst
            moves.append(f"Переместить диск {num} с {src} на {dst}")
            # Переместить n-1 дисков с aux на dst
            hanoi_recursive(num - 1, aux, src, dst)

    hanoi_recursive(n, source, auxiliary, target)
    return moves


if __name__ == "__main__":
    # Тестирование бинарного поиска
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 7
    print(f"Бинарный поиск {target} в {arr}:")
    print(f"Индекс: {binary_search_recursive(arr, target)}")

    # Тестирование Ханойских башен
    print("\nХанойские башни для 3 дисков:")
    moves = hanoi_towers(3)
    for i, move in enumerate(moves, 1):
        print(f"{i}. {move}")
