"""
Модуль для визуализации результатов тестирования.
"""

import matplotlib.pyplot as plt
import numpy as np
import time
import copy
from typing import List, Dict

from sorts import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    is_sorted
)
from generate_data import generate_test_datasets


def measure_time(algorithm, arr: List[int]) -> float:
    """
    Измерение времени выполнения алгоритма.

    Args:
        algorithm: Функция сортировки
        arr: Массив для сортировки

    Returns:
        Время выполнения в секундах
    """
    arr_copy = copy.deepcopy(arr)

    start_time = time.time()
    algorithm(arr_copy)
    end_time = time.time()

    return end_time - start_time


def run_performance_tests() -> Dict[str, Dict[str, Dict[int, float]]]:
    """
    Запуск тестов производительности.

    Returns:
        Словарь с результатами тестов
    """
    sizes = [100, 1000, 5000]
    datasets = generate_test_datasets(sizes)

    algorithms = {
        'bubble_sort': bubble_sort,
        'selection_sort': selection_sort,
        'insertion_sort': insertion_sort,
        'merge_sort': merge_sort,
        'quick_sort': quick_sort
    }

    results = {algo_name: {} for algo_name in algorithms.keys()}

    print("Запуск тестов производительности...")

    for data_type, size_data in datasets.items():
        print(f"\nТип данных: {data_type}")

        for algo_name, algorithm in algorithms.items():
            results[algo_name][data_type] = {}
            print(f"{algo_name:15}", end=" ")

            for size, arr in size_data.items():
                time_taken = measure_time(algorithm, arr)
                results[algo_name][data_type][size] = time_taken
                test_arr = arr.copy()
                algorithm(test_arr)
                correct = is_sorted(test_arr)
                status = "OK" if correct else "ERR"
                print(f"{size}: {time_taken:.4f}s {status}", end=" ")

            print()

    return results


def plot_comprehensive_comparison(results: dict):
    """
    Построение всеобъемлющих графиков сравнения.

    Args:
        results: Результаты тестирования
    """
    data_types = ['random', 'sorted', 'reversed', 'almost_sorted']
    algorithms = list(results.keys())
    sizes = [100, 1000, 5000, 10000]

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    axes = axes.flatten()

    for idx, data_type in enumerate(data_types):
        ax = axes[idx]
        for algo in algorithms:
            if data_type in results[algo]:
                times = []
                for size in sizes:
                    time_val = results[algo][data_type].get(size, 0)
                    times.append(time_val)
                ax.plot(sizes, times, marker='o', linewidth=2,
                        label=algo, markersize=6)

        ax.set_title(f'Производительность на {data_type} данных',
                     fontsize=14)
        ax.set_xlabel('Размер массива', fontsize=12)
        ax.set_ylabel('Время (секунды)', fontsize=12)
        ax.legend(fontsize=10)
        ax.grid(True, alpha=0.3)
        ax.set_xscale('log')
        ax.set_yscale('log')

    plt.tight_layout()
    plt.savefig('comprehensive_performance.png', dpi=300,
                bbox_inches='tight')
    plt.show()


def plot_comparison_histogram(results: dict, size: int = 5000):
    """
    Гистограмма сравнения алгоритмов для фиксированного размера.

    Args:
        results: Результаты тестирования
        size: Размер массива
    """
    data_types = ['random', 'sorted', 'reversed', 'almost_sorted']
    algorithms = list(results.keys())

    fig, axes = plt.subplots(2, 2, figsize=(16, 10))
    axes = axes.flatten()

    for idx, data_type in enumerate(data_types):
        ax = axes[idx]
        times = []
        labels = []

        for algo in algorithms:
            if (data_type in results[algo] and
                    size in results[algo][data_type]):
                times.append(results[algo][data_type][size])
                labels.append(algo)

        if times:
            sorted_indices = np.argsort(times)
            sorted_times = [times[i] for i in sorted_indices]
            sorted_labels = [labels[i] for i in sorted_indices]

            colors = plt.cm.viridis(np.linspace(0, 1, len(times)))
            bars = ax.barh(sorted_labels, sorted_times, color=colors)
            ax.set_title(f'{data_type} данные (n={size})', fontsize=12)
            ax.set_xlabel('Время (секунды)')

            for bar in bars:
                width = bar.get_width()
                ax.text(width + max(sorted_times) * 0.01,
                        bar.get_y() + bar.get_height()/2,
                        f'{width:.4f}s', ha='left', va='center', fontsize=9)

    plt.tight_layout()
    plt.savefig('algorithm_comparison_histogram.png', dpi=300,
                bbox_inches='tight')
    plt.show()


def plot_performance_heatmap(results: dict):
    """
    Тепловая карта производительности.

    Args:
        results: Результаты тестирования
    """
    data_types = ['random', 'sorted', 'reversed', 'almost_sorted']
    algorithms = list(results.keys())
    sizes = [100, 1000, 5000, 10000]

    fig, ax = plt.subplots(figsize=(16, 8))

    heatmap_data = []
    row_labels = []

    for algo in algorithms:
        row_data = []
        for data_type in data_types:
            for size in sizes:
                time_val = results[algo].get(data_type, {}).get(size, 0)
                row_data.append(time_val)
        heatmap_data.append(row_data)
        row_labels.append(algo)

    heatmap_data = np.array(heatmap_data)

    im = ax.imshow(heatmap_data, cmap='YlOrRd', aspect='auto')

    ax.set_xticks(np.arange(len(data_types) * len(sizes)))
    ax.set_yticks(np.arange(len(algorithms)))
    ax.set_yticklabels(row_labels)

    x_labels = []
    for data_type in data_types:
        for size in sizes:
            x_labels.append(f"{data_type[0]}{size}")
    ax.set_xticklabels(x_labels, rotation=45)

    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.set_ylabel('Время (секунды)', rotation=-90, va="bottom")

    ax.set_title("Тепловая карта производительности алгоритмов сортировки",
                 fontsize=14, pad=20)

    plt.tight_layout()
    plt.savefig('performance_heatmap.png', dpi=300, bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    print("Запуск тестов для комплексной визуализации...")
    results = run_performance_tests()

    print("\nПостроение комплексных графиков...")
    plot_comprehensive_comparison(results)
    plot_comparison_histogram(results, 5000)
    plot_performance_heatmap(results)
