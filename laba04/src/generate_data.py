"""
Модуль для генерации тестовых данных.
"""

import random
from typing import List, Dict


def generate_random_array(size: int) -> List[int]:
    """Генерация случайного массива."""
    return [random.randint(0, size * 10) for _ in range(size)]


def generate_sorted_array(size: int) -> List[int]:
    """Генерация отсортированного массива."""
    return list(range(size))


def generate_reversed_array(size: int) -> List[int]:
    """Генерация обратно отсортированного массива."""
    return list(range(size, 0, -1))


def generate_almost_sorted_array(size: int,
                                 swap_percent: float = 5) -> List[int]:
    """
    Генерация почти отсортированного массива.

    Args:
        size: Размер массива
        swap_percent: Процент перестановок (0-100)
    """
    arr = list(range(size))
    num_swaps = max(1, size * swap_percent // 100)

    for _ in range(num_swaps):
        i = random.randint(0, size - 1)
        j = random.randint(0, size - 1)
        arr[i], arr[j] = arr[j], arr[i]

    return arr


def generate_test_datasets(sizes: List[int] = None
                           ) -> Dict[str, Dict[int, List[int]]]:
    """
    Генерация всех тестовых наборов данных.

    Args:
        sizes: Список размеров массивов

    Returns:
        Словарь с тестовыми данными
    """
    if sizes is None:
        sizes = [100, 1000, 5000, 10000]

    datasets = {
        'random': {},
        'sorted': {},
        'reversed': {},
        'almost_sorted': {}
    }

    for size in sizes:
        datasets['random'][size] = generate_random_array(size)
        datasets['sorted'][size] = generate_sorted_array(size)
        datasets['reversed'][size] = generate_reversed_array(size)
        datasets['almost_sorted'][size] = generate_almost_sorted_array(size)

    return datasets


if __name__ == "__main__":
    test_sizes = [100, 500]
    datasets = generate_test_datasets(test_sizes)

    for data_type, size_data in datasets.items():
        print(f"\n{data_type}:")
        for size, arr in size_data.items():
            print(f"  Размер {size}: первые 10 элементов - {arr[:10]}")
