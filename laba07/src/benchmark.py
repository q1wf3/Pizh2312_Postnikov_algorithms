"""
Бенчмарки и измерения производительности для куч и сортировок.
"""

import time
import random
import sys
import platform
import matplotlib.pyplot as plt
from heap import MinHeap
from heapsort import heapsort, heapsort_inplace


def get_system_info():
    """Получение информации о системе."""
    info = {
        "Python version": sys.version,
        "Platform": platform.platform(),
        "Processor": platform.processor(),
        "System": platform.system(),
        "Machine": platform.machine(),
    }
    return info


def benchmark_heap_construction():
    """Сравнение времени построения кучи."""
    print("Бенчмарк: Построение кучи")
    print("-" * 50)

    sizes = [100, 500, 1000, 5000, 10000, 20000]
    times_insert = []
    times_build = []

    for size in sizes:
        print(f"Размер массива: {size}")

        data = [random.randint(1, 100000) for _ in range(size)]

        # Метод 1: Последовательная вставка
        start = time.perf_counter()
        heap = MinHeap()
        for item in data:
            heap.insert(item)
        end = time.perf_counter()
        time_insert = end - start
        times_insert.append(time_insert)
        print(f"  Последовательная вставка: {time_insert:.6f} сек")

        if not heap.is_valid():
            print("  Внимание: Свойство кучи нарушено!")

        # Метод 2: Алгоритм build_heap
        start = time.perf_counter()
        heap = MinHeap()
        heap.build_heap(data)
        end = time.perf_counter()
        time_build = end - start
        times_build.append(time_build)
        print(f"  Алгоритм build_heap: {time_build:.6f} сек")

        if not heap.is_valid():
            print("  Внимание: Свойство кучи нарушено!")

        if time_build > 0:
            ratio = time_insert / time_build
            print(f"  Отношение (вставка/build_heap): {ratio:.2f}")

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times_insert, 'o-',
             label='Последовательная вставка', linewidth=2)
    plt.plot(sizes, times_build, 's-',
             label='Алгоритм build_heap', linewidth=2)
    plt.xlabel('Размер массива (n)', fontsize=12)
    plt.ylabel('Время (секунды)', fontsize=12)
    title = 'Сравнение времени построения кучи'
    plt.title(title, fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=11)
    plt.yscale('log')
    plt.xscale('log')
    plt.tight_layout()
    plt.savefig('heap_construction_benchmark.png', dpi=300)
    print("График сохранен как 'heap_construction_benchmark.png'")

    return sizes, times_insert, times_build


def benchmark_heapsort():
    """Бенчмарк сортировки кучей."""
    print("Бенчмарк: Сортировка кучей (Heapsort)")
    print("-" * 50)

    sizes = [100, 500, 1000, 5000, 10000, 20000]
    times_standard = []
    times_inplace = []

    for size in sizes:
        print(f"Размер массива: {size}")

        data = [random.randint(1, 100000) for _ in range(size)]

        # Метод 1: Стандартная сортировка кучей
        start = time.perf_counter()
        sorted_data = heapsort(data)
        end = time.perf_counter()
        time_standard = end - start
        times_standard.append(time_standard)
        print(f"  Heapsort (с доп. памятью): {time_standard:.6f} сек")

        if sorted_data != sorted(data):
            print("  Внимание: Неправильная сортировка!")

        # Метод 2: In-place сортировка кучей
        data_copy = data[:]
        start = time.perf_counter()
        heapsort_inplace(data_copy)
        end = time.perf_counter()
        time_inplace = end - start
        times_inplace.append(time_inplace)
        print(f"  Heapsort (in-place): {time_inplace:.6f} сек")

        if data_copy != sorted(data):
            print("  Внимание: Неправильная сортировка!")

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times_standard, 'o-',
             label='Heapsort (с доп. памятью)', linewidth=2)
    plt.plot(sizes, times_inplace, 's-',
             label='Heapsort (in-place)', linewidth=2)
    plt.xlabel('Размер массива (n)', fontsize=12)
    plt.ylabel('Время (секунды)', fontsize=12)
    title = 'Сравнение времени сортировки Heapsort'
    plt.title(title, fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=11)
    plt.yscale('log')
    plt.xscale('log')
    plt.tight_layout()
    plt.savefig('heapsort_benchmark.png', dpi=300)
    print("График сохранен как 'heapsort_benchmark.png'")

    return sizes, times_standard, times_inplace


def benchmark_sorting_algorithms():
    """Сравнение Heapsort с другими алгоритмами сортировки."""
    print("Бенчмарк: Сравнение алгоритмов сортировки")
    print("-" * 50)

    sizes = [100, 500, 1000, 5000, 10000]

    def quicksort(arr):
        """Быстрая сортировка."""
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

    def mergesort(arr):
        """Сортировка слиянием."""
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = mergesort(arr[:mid])
        right = mergesort(arr[mid:])
        return merge(left, right)

    def merge(left, right):
        """Слияние для MergeSort."""
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    times_heapsort = []
    times_quicksort = []
    times_mergesort = []
    times_timsort = []

    for size in sizes:
        print(f"Размер массива: {size}")

        data = [random.randint(1, 100000) for _ in range(size)]

        # Heapsort (in-place)
        data_copy = data[:]
        start = time.perf_counter()
        heapsort_inplace(data_copy)
        end = time.perf_counter()
        time_heap = end - start
        times_heapsort.append(time_heap)
        print(f"  Heapsort: {time_heap:.6f} сек")

        # QuickSort
        start = time.perf_counter()
        quicksort(data)
        end = time.perf_counter()
        time_quick = end - start
        times_quicksort.append(time_quick)
        print(f"  QuickSort: {time_quick:.6f} сек")

        # MergeSort
        start = time.perf_counter()
        mergesort(data)
        end = time.perf_counter()
        time_merge = end - start
        times_mergesort.append(time_merge)
        print(f"  MergeSort: {time_merge:.6f} сек")

        # Timsort (встроенная сортировка Python)
        data_copy = data[:]
        start = time.perf_counter()
        sorted(data_copy)
        end = time.perf_counter()
        time_tim = end - start
        times_timsort.append(time_tim)
        print(f"  Timsort (sorted()): {time_tim:.6f} сек")

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times_heapsort, 'o-',
             label='Heapsort', linewidth=2)
    plt.plot(sizes, times_quicksort, 's-',
             label='QuickSort', linewidth=2)
    plt.plot(sizes, times_mergesort, '^-',
             label='MergeSort', linewidth=2)
    plt.plot(sizes, times_timsort, 'D-',
             label='Timsort (sorted())', linewidth=2)
    plt.xlabel('Размер массива (n)', fontsize=12)
    plt.ylabel('Время (секунды)', fontsize=12)
    title = 'Сравнение алгоритмов сортировки'
    plt.title(title, fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=11)
    plt.yscale('log')
    plt.xscale('log')
    plt.tight_layout()
    plt.savefig('sorting_algorithms_benchmark.png', dpi=300)
    print("График сохранен как 'sorting_algorithms_benchmark.png'")

    return (sizes, times_heapsort, times_quicksort,
            times_mergesort, times_timsort)


def benchmark_heap_operations():
    """Бенчмарк основных операций кучи."""
    print("Бенчмарк: Основные операции кучи")
    print("-" * 50)

    sizes = [100, 500, 1000, 5000, 10000, 20000]
    times_insert = []
    times_extract = []

    for size in sizes:
        print(f"Размер кучи: {size}")

        heap = MinHeap()
        data = [random.randint(1, 100000) for _ in range(size)]
        heap.build_heap(data)

        # Бенчмарк вставки
        start = time.perf_counter()
        for _ in range(100):
            heap.insert(random.randint(1, 100000))
        end = time.perf_counter()
        time_insert = (end - start) / 100
        times_insert.append(time_insert)
        msg = f"  Среднее время вставки: {time_insert*1e6:.2f} микросекунд"
        print(msg)

        heap.build_heap(data)

        # Бенчмарк извлечения
        start = time.perf_counter()
        for _ in range(min(100, size)):
            heap.extract()
        end = time.perf_counter()
        time_extract = (end - start) / min(100, size)
        times_extract.append(time_extract)
        msg = f"  Среднее время извлечения: {time_extract*1e6:.2f} микросекунд"
        print(msg)

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, [t * 1e6 for t in times_insert], 'o-',
             label='Вставка (insert)', linewidth=2)
    plt.plot(sizes, [t * 1e6 for t in times_extract], 's-',
             label='Извлечение (extract)', linewidth=2)
    plt.xlabel('Размер кучи (n)', fontsize=12)
    plt.ylabel('Время (микросекунды)', fontsize=12)
    title = 'Время основных операций кучи'
    plt.title(title, fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=11)
    plt.xscale('log')
    plt.tight_layout()
    plt.savefig('heap_operations_benchmark.png', dpi=300)
    print("График сохранен как 'heap_operations_benchmark.png'")

    return sizes, times_insert, times_extract


def run_all_benchmarks():
    """Запуск всех бенчмарков."""
    print("Начало бенчмарк-тестов")

    print("Информация о системе:")
    for key, value in get_system_info().items():
        print(f"  {key}: {value}")

    benchmark_heap_construction()
    benchmark_heapsort()
    benchmark_sorting_algorithms()
    benchmark_heap_operations()

    print("Бенчмарк-тесты завершены")


if __name__ == "__main__":
    run_all_benchmarks()
