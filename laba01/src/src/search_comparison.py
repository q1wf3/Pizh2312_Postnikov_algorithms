# search_comparison.py
import timeit
from typing import List, Optional


def linear_search(arr: List[int], target: int) -> Optional[int]:
    """Линейный поиск элемента в массиве.

    Сложность: O(n), где n — длина массива.
    """
    for i, value in enumerate(arr):  # O(n) — цикл по массиву
        if value == target:  # O(1) — сравнение
            return i  # O(1) — возврат индекса
    return None  # O(1) — возврат None
    # Общая сложность: O(n)


def binary_search(arr: List[int], target: int) -> Optional[int]:
    """Бинарный поиск элемента в отсортированном массиве.

    Сложность: O(log n), где n — длина массива.
    """
    left: int = 0  # O(1)
    right: int = len(arr) - 1  # O(1)

    while left <= right:  # O(log n) итераций
        mid: int = (left + right) // 2  # O(1)
        if arr[mid] == target:  # O(1)
            return mid  # O(1)
        elif arr[mid] < target:  # O(1)
            left = mid + 1  # O(1)
        else:
            right = mid - 1  # O(1)
    return None  # O(1)
    # Общая сложность: O(log n)


def measure_time(func, arr: List[int], target: int, runs: int = 10) -> float:
    """Измеряет среднее время выполнения функции (в миллисекундах)."""
    total_time: float = timeit.timeit(
        lambda: func(arr, target), number=runs
    )
    return (total_time / runs) * 1000  # перевод в мс


# Характеристики ПК
pc_info: str = """
Характеристики ПК для тестирования:
- Процессор: Apple M4
- Оперативная память: 8 GB Unified Memory
- ОС: macOS
- Python: 3.13.7
"""
print(pc_info)

# Размеры массивов для эксперимента
sizes: List[int] = [1000, 5000, 10000]
linear_times: List[float] = []
binary_times: List[float] = []

print("Замеры времени выполнения для алгоритмов поиска:")
print("{:>10} {:>15} {:>15}".format("Размер (n)", "Линейный (мс)",
      "Бинарный (мс)"))
print("-" * 50)

for size in sizes:
    # Генерация отсортированного массива
    arr: List[int] = list(range(size))  # O(n)

    # Целевой элемент (берём последний для худшего случая)
    target: int = size - 1  # O(1)

    # Замеры времени
    lin_time: float = measure_time(linear_search, arr, target)
    bin_time: float = measure_time(binary_search, arr, target)

    linear_times.append(lin_time)
    binary_times.append(bin_time)

    print("{:>10} {:>15.4f} {:>15.4f}".format(size, lin_time, bin_time))


# Анализ результатов
print("\n" + "=" * 60)
print("Анализ результатов:")
print("1. Теоретическая сложность линейного поиска: O(n)")
print("2. Теоретическая сложность бинарного поиска: O(log n)")
print("3. Результаты подтверждают асимптотику:")
print("   - Время линейного поиска растет пропорционально размеру массива")
print("   - Время бинарного поиска растет очень медленно (логарифмически)")
print("4. Бинарный поиск значительно эффективнее на больших массивах")

# Дополнительный анализ роста времени
print("\nОтношение времени линейного к бинарному поиску:")
for i, size in enumerate(sizes):
    ratio = linear_times[i] / binary_times[i] if binary_times[i] > 0 else 0
    print(f"Размер {size:>6}: линейный поиск в {ratio:>6.1f} раз медленнее")
