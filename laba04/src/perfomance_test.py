"""
Модуль для эмпирического анализа производительности алгоритмов сортировки.
Использует данные, сгенерированные в generate_data.py, и
сортировки из sorts.py.
"""

import time
import csv
from generate_data import generate_test_datasets
from sorts import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    is_sorted
)

# Список тестируемых алгоритмов
SORT_FUNCTIONS = {
    "bubble_sort": bubble_sort,
    "selection_sort": selection_sort,
    "insertion_sort": insertion_sort,
    "merge_sort": merge_sort,
    "quick_sort": quick_sort,
}


def measure_time(sort_func, data):
    """Измеряет время выполнения одной сортировки на копии массива."""
    data_copy = data.copy()
    start = time.perf_counter()
    sort_func(data_copy)
    end = time.perf_counter()
    return (end - start) * 1000  # Конвертируем в миллисекунды


def save_results_to_csv(results, filename="results.csv"):
    """Сохраняет результаты в CSV файл."""
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['algorithm', 'size', 'data_type', 'time_ms'])
        for result in results:
            writer.writerow([
                result['algorithm'],
                result['size'],
                result['data_type'],
                round(result['time_ms'], 6)
            ])


def run_performance_tests():
    """Проводит замеры времени для всех алгоритмов и наборов данных."""
    datasets = generate_test_datasets()
    results = []

    for data_type, size_dict in datasets.items():
        for size, arr in size_dict.items():
            print(f"Тест: {data_type}, размер {size}")
            for name, func in SORT_FUNCTIONS.items():
                elapsed = measure_time(func, arr)
                test_arr = arr.copy()
                func(test_arr)
                status = "OK" if is_sorted(test_arr) else "ERR"
                print(f"{name:15} | {elapsed:8.2f} ms {status}")
                results.append({
                    "algorithm": name,
                    "size": size,
                    "data_type": data_type,
                    "time_ms": elapsed
                })

    save_results_to_csv(results)
    print("Все результаты сохранены в results.csv")
    return results


def analyze_results(results):
    """Анализирует результаты тестирования."""
    print("=" * 50)
    print("АНАЛИЗ РЕЗУЛЬТАТОВ")
    print("=" * 50)

    # Самые быстрые алгоритмы для каждого размера
    print("Самые быстрые алгоритмы (случайные данные):")
    sizes = sorted(set(r['size'] for r in results))
    for size in sizes:
        size_results = [r for r in results
                        if r['size'] == size and r['data_type'] == 'random']
        if size_results:
            fastest = min(size_results, key=lambda x: x['time_ms'])
            algo = fastest['algorithm']
            time_val = fastest['time_ms']
            print(f"  Размер {size:5}: {algo:15} - {time_val:8.2f} ms")


def print_summary_statistics(results):
    """Выводит сводную статистику по результатам."""
    print("=" * 50)
    print("СВОДНАЯ СТАТИСТИКА")
    print("=" * 50)

    # Общая статистика
    print(f"Всего тестов: {len(results)}")
    print(f"Уникальных алгоритмов: {len(SORT_FUNCTIONS)}")
    sizes = sorted(set(r['size'] for r in results))
    print(f"Размеры массивов: {sizes}")

    # Статистика по времени
    times = [r['time_ms'] for r in results]
    print(f"Минимальное время: {min(times):.2f} ms")
    print(f"Максимальное время: {max(times):.2f} ms")
    avg_time = sum(times) / len(times)
    print(f"Среднее время: {avg_time:.2f} ms")

    # Лучший алгоритм в среднем
    algo_times = {}
    for algo in SORT_FUNCTIONS:
        algo_results = [r for r in results if r['algorithm'] == algo]
        if algo_results:
            total_time = sum(r['time_ms'] for r in algo_results)
            algo_times[algo] = total_time / len(algo_results)

    if algo_times:
        best_algo = min(algo_times, key=algo_times.get)
        best_time = algo_times[best_algo]
        print(f"Лучший алгоритм в среднем: {best_algo} ({best_time:.2f} ms)")


if __name__ == "__main__":
    print("Запуск тестов производительности алгоритмов сортировки...")
    results = run_performance_tests()

    print("=" * 50)
    print("ПРЕДВАРИТЕЛЬНЫЙ ПРОСМОТР ДАННЫХ")
    print("=" * 50)
    for i, result in enumerate(results[:10]):
        algo = result['algorithm']
        size = result['size']
        data_type = result['data_type']
        time_ms = result['time_ms']
        print(f"{i+1:2}. {algo:15} | {size:5} | {data_type:12} | "
              f"{time_ms:8.2f} ms")

    analyze_results(results)
    print_summary_statistics(results)

    print("Тестирование завершено! Результаты сохранены в results.csv")
