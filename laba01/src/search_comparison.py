"""
Сравнение линейного и бинарного поиска.
"""

import timeit
from typing import Callable, List

import matplotlib.pyplot as plt


def linear_search(arr: List[int], target: int) -> int | None:
    """
    Линейный поиск.

    Сложность: O(n)
    """
    for index, value in enumerate(arr):  # O(n)
        if value == target:  # O(1)
            return index  # O(1)
    return None  # O(1)
    # Общая сложность: O(n)


def binary_search(arr: List[int], target: int) -> int | None:
    """
    Бинарный поиск.

    Сложность: O(log n)
    """
    left = 0  # O(1)
    right = len(arr) - 1  # O(1)

    while left <= right:  # O(log n)
        mid = (left + right) // 2  # O(1)
        value = arr[mid]  # O(1)

        if value == target:  # O(1)
            return mid  # O(1)

        if value < target:  # O(1)
            left = mid + 1  # O(1)
        else:
            right = mid - 1  # O(1)

    return None  # O(1)
    # Общая сложность: O(log n)


def measure_average_time(
    func: Callable,
    arr: List[int],
    target: int,
    runs: int = 10,
) -> float:
    """
    Измеряет среднее время выполнения функции в миллисекундах.
    """
    total = timeit.timeit(lambda: func(arr, target), number=runs)  # O(runs)
    return (total / runs) * 1000  # O(1)


def generate_sorted_array(size: int) -> List[int]:
    """
    Создаёт отсортированный массив.

    Сложность: O(n)
    """
    return list(range(size))  # O(n)


def plot_results(
    sizes: List[int],
    lin_t: List[float],
    bin_t: List[float]
) -> None:
    """
    Строит графики сравнения алгоритмов.
    """
    plt.figure(figsize=(10, 6))  # O(1)
    plt.plot(sizes, lin_t, "o-b", label="Линейный поиск O(n)")  # O(n)
    plt.plot(sizes, bin_t, "o-r", label="Бинарный поиск O(log n)")  # O(n)
    plt.xlabel("Размер массива (n)")  # O(1)
    plt.ylabel("Время (мс)")  # O(1)
    plt.grid(True, linestyle="--", alpha=0.6)  # O(1)
    plt.title("Сравнение алгоритмов поиска")  # O(1)
    plt.legend()  # O(1)
    plt.savefig("comparison.png", dpi=300, bbox_inches="tight")  # O(1)
    plt.show()  # O(1)

    plt.figure(figsize=(10, 6))  # O(1)
    plt.plot(sizes, lin_t, "o-b", label="Линейный поиск O(n)")  # O(n)
    plt.plot(sizes, bin_t, "o-r", label="Бинарный поиск O(log n)")  # O(n)
    plt.yscale("log")  # O(1)
    plt.xlabel("Размер массива (n)")  # O(1)
    plt.ylabel("Время (мс), лог шкала")  # O(1)
    plt.grid(True, linestyle="--", alpha=0.6)  # O(1)
    plt.title("Поиск в логарифмической шкале")  # O(1)
    plt.legend()  # O(1)
    plt.savefig("comparison_log.png", dpi=300, bbox_inches="tight")  # O(1)
    plt.show()  # O(1)


def run_experiment() -> None:
    """
    Запуск эксперимента по замеру времени.
    """
    pc_info = (
        "Характеристики системы:\n"
        "- CPU: Intel(R) Xeon(R) CPU E3-1270 v3 @ 3.50GHz\n"
        "- RAM: 16 GB\n"
        "- OS: Windows 10\n"
        "- Python: 3.13\n"
    )  # O(1)
    print(pc_info)  # O(1)

    sizes = [1000, 5000, 10000, 50000, 100000, 500000]  # O(1)
    linear_times: List[float] = []  # O(1)
    binary_times: List[float] = []  # O(1)

    # Заголовок таблицы
    print(
        f"{'Размер n':>10} | "
        f"{'Линейный (мс)':>15} | "
        f"{'Бинарный (мс)':>15}"
    )
    print("-" * 45)  # O(1)

    for size in sizes:  # O(k)
        arr = generate_sorted_array(size)  # O(size)
        target = size - 1  # O(1)
        t_lin = measure_average_time(
            linear_search, arr, target
        )  # O(runs * n)
        t_bin = measure_average_time(
            binary_search, arr, target
        )  # O(runs * log n)
        linear_times.append(t_lin)  # O(1)
        binary_times.append(t_bin)  # O(1)

        # Вывод результатов
        print(
            f"{size:>10} | "
            f"{t_lin:>15.4f} | "
            f"{t_bin:>15.4f}"
        )

    plot_results(sizes, linear_times, binary_times)  # O(n)


if __name__ == "__main__":
    run_experiment()
