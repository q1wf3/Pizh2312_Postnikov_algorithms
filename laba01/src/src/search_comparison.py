import time  # O(1)
import matplotlib.pyplot as plt  # O(1)


def linear_search(arr: list[int], target: int) -> int:
    """
    Линейный поиск элемента в массиве.
    Сложность: O(n)
    """
    for i in range(len(arr)):  # O(n)
        if arr[i] == target:  # O(1)
            return i  # O(1)
    return -1  # O(1)
# Общая сложность: O(n)


def binary_search(arr: list[int], target: int) -> int:
    """
    Бинарный поиск элемента в отсортированном массиве.
    Сложность: O(log n)
    """
    left = 0  # O(1)
    right = len(arr) - 1  # O(1)

    while left <= right:  # цикл — O(log n)
        mid = (left + right) // 2  # O(1)

        if arr[mid] == target:  # O(1)
            return mid  # O(1)
        elif arr[mid] < target:  # O(1)
            left = mid + 1  # O(1)
        else:
            right = mid - 1  # O(1)

    return -1  # O(1)
# Общая сложность: O(log n)


def generate_array(size: int) -> list[int]:
    """
    Генерация отсортированного массива [0, size-1].
    Сложность: O(n)
    """
    return list(range(size))  # O(n)


def measure_time(func, arr: list[int], target: int,
                 repeats: int = 5) -> float:
    """
    Замер среднего времени выполнения алгоритма.
    """
    total = 0.0  # O(1)

    for _ in range(repeats):  # O(repeats)
        start = time.perf_counter()  # O(1)
        func(arr, target)  # O(n) или O(log n)
        end = time.perf_counter()  # O(1)

        total += end - start  # O(1)

    return total / repeats  # O(1)


def run_experiments() -> dict:
    """
    Проведение экспериментов для линейного и бинарного поиска
    в четырёх сценариях: first, middle, last, absent.
    """
    sizes = [
        1000, 2000, 5000, 10_000, 50_000,
        100_000, 500_000, 1_000_000
    ]

    results = {
        'linear': {'first': [], 'middle': [], 'last': [], 'absent': []},
        'binary': {'first': [], 'middle': [], 'last': [], 'absent': []},
    }

    for size in sizes:  # O(k)
        arr = generate_array(size)  # O(n)

        # Линейный поиск
        results['linear']['first'].append(
            measure_time(linear_search, arr, arr[0])
        )
        results['linear']['middle'].append(
            measure_time(linear_search, arr, arr[size // 2])
        )
        results['linear']['last'].append(
            measure_time(linear_search, arr, arr[-1])
        )
        results['linear']['absent'].append(
            measure_time(linear_search, arr, -1)
        )

        # Бинарный поиск
        results['binary']['first'].append(
            measure_time(binary_search, arr, arr[0])
        )
        results['binary']['middle'].append(
            measure_time(binary_search, arr, arr[size // 2])
        )
        results['binary']['last'].append(
            measure_time(binary_search, arr, arr[-1])
        )
        results['binary']['absent'].append(
            measure_time(binary_search, arr, -1)
        )

    return {'sizes': sizes, 'results': results}


def plot_results(data: dict) -> None:
    """
    График в линейном масштабе.
    """
    sizes = data['sizes']
    results = data['results']

    plt.figure(figsize=(12, 6))  # O(1)

    for case, times in results['linear'].items():  # O(c)
        plt.plot(sizes, times, marker='o', label=f'Linear - {case}')  # O(k)

    for case, times in results['binary'].items():  # O(c)
        plt.plot(
            sizes,
            times,
            marker='x',
            linestyle='--',
            label=f'Binary - {case}'
        )  # O(k)

    plt.xlabel('Размер массива (N)')
    plt.ylabel('Время (сек)')
    plt.title('Сравнение линейного и бинарного поиска')
    plt.grid(True)
    plt.legend()
    plt.show()  # O(1)


def plot_results_log(data: dict) -> None:
    """
    График в логарифмическом масштабе по оси Y.
    """
    sizes = data['sizes']
    results = data['results']

    plt.figure(figsize=(12, 6))  # O(1)

    for case, times in results['linear'].items():
        plt.plot(sizes, times, marker='o', label=f'Linear - {case}')

    for case, times in results['binary'].items():
        plt.plot(
            sizes,
            times,
            marker='x',
            linestyle='--',
            label=f'Binary - {case}'
        )

    plt.xlabel('Размер массива (N)')
    plt.ylabel('Время (лог scale)')
    plt.title('Сравнение O(n) и O(log n)')
    plt.yscale('log')
    plt.grid(True, which='both')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    data = run_experiments()

    print('Размеры массивов:', data['sizes'])
    print()

    for algo in ['linear', 'binary']:
        print(f'Алгоритм: {algo}')
        for case in ['first', 'middle', 'last', 'absent']:
            print(f'  {case:7}: {data["results"][algo][case]}')
        print()

    plot_results(data)
    plot_results_log(data)
