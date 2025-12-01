"""
Анализ производительности хеш-таблиц.
"""

import time
import random
import string
import matplotlib.pyplot as plt
from hash_functions import simple_hash, polynomial_hash, djb2_hash
from hash_table_chaining import HashTableChaining
from hash_table_open_addressing import HashTableOpenAddressing


def generate_random_string(length: int = 10) -> str:
    """Генерирует случайную строку."""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))


def measure_performance(
    table_type,
    hash_func,
    probe_method=None,
    initial_size=100,
    load_factors=None,
    num_operations=1000
):
    """
    Измеряет производительность хеш-таблиц.
    """
    if load_factors is None:
        load_factors = [0.1, 0.5, 0.7, 0.9]

    results = {}

    for load_factor in load_factors:
        if table_type == 'chaining':
            table = HashTableChaining(
                initial_size=initial_size,
                load_factor=load_factor,
                hash_func=hash_func
            )
        else:
            table = HashTableOpenAddressing(
                initial_size=initial_size,
                load_factor=load_factor,
                probe_method=probe_method,
                hash_func=hash_func
            )

        num_elements = int(initial_size * load_factor)
        test_data = [
            (generate_random_string(), i)
            for i in range(num_elements)
        ]

        start = time.time()
        for key, value in test_data:
            table.insert(key, value)
        insert_time = time.time() - start

        start = time.time()
        for key, _ in test_data:
            table.search(key)
        search_time = time.time() - start

        start = time.time()
        for key, _ in test_data:
            table.delete(key)
        delete_time = time.time() - start

        if table_type == 'chaining':
            collisions, _ = table.get_collision_stats()
        else:
            probes, _ = table.get_probe_stats()
            collisions = probes

        results[load_factor] = {
            "insert_time": insert_time,
            "search_time": search_time,
            "delete_time": delete_time,
            "collisions": collisions,
            "load_factor": table.get_load_factor()
        }

    return results


def compare_hash_functions():
    """Сравнивает распределение хеш-функций."""
    hash_funcs = {
        'Простая': simple_hash,
        'Полиномиальная': polynomial_hash,
        'DJB2': djb2_hash
    }

    table_size = 100
    num_keys = 1000
    test_keys = [generate_random_string(10) for _ in range(num_keys)]

    distribution_data = {}

    for name, hash_func in hash_funcs.items():
        buckets = [0] * table_size
        for key in test_keys:
            index = hash_func(key, table_size)
            buckets[index] += 1
        distribution_data[name] = buckets

    plt.figure(figsize=(15, 5))
    for i, (name, buckets) in enumerate(distribution_data.items(), 1):
        plt.subplot(1, 3, i)
        plt.hist(buckets, bins=20, alpha=0.7, edgecolor='black')
        plt.title(f'Распределение {name}')
        plt.xlabel('Элементов в корзине')
        plt.ylabel('Частота')
        plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('hash_distribution.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\nСтатистика распределения:")
    for name, buckets in distribution_data.items():
        avg = sum(buckets) / len(buckets)
        variance = sum((x - avg) ** 2 for x in buckets) / len(buckets)
        std_dev = variance ** 0.5
        print(f"{name}: среднее = {avg:.2f}, отклонение = {std_dev:.2f}")


def plot_performance_results(all_results):
    """Строит графики производительности."""
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))

    # Время вставки
    for label, results in all_results.items():
        loads = list(results.keys())
        times = [results[load]['insert_time'] for load in loads]
        axes[0, 0].plot(loads, times, marker='o', label=label)
    axes[0, 0].set_title('Время вставки')
    axes[0, 0].set_xlabel('Коэффициент заполнения')
    axes[0, 0].set_ylabel('Время (с)')
    axes[0, 0].legend()
    axes[0, 0].grid(True)

    # Время поиска
    for label, results in all_results.items():
        loads = list(results.keys())
        times = [results[load]['search_time'] for load in loads]
        axes[0, 1].plot(loads, times, marker='o', label=label)
    axes[0, 1].set_title('Время поиска')
    axes[0, 1].set_xlabel('Коэффициент заполнения')
    axes[0, 1].set_ylabel('Время (с)')
    axes[0, 1].legend()
    axes[0, 1].grid(True)

    # Время удаления
    for label, results in all_results.items():
        loads = list(results.keys())
        times = [results[load]['delete_time'] for load in loads]
        axes[1, 0].plot(loads, times, marker='o', label=label)
    axes[1, 0].set_title('Время удаления')
    axes[1, 0].set_xlabel('Коэффициент заполнения')
    axes[1, 0].set_ylabel('Время (с)')
    axes[1, 0].legend()
    axes[1, 0].grid(True)

    # Коллизии
    for label, results in all_results.items():
        loads = list(results.keys())
        collisions = [results[load]['collisions'] for load in loads]
        axes[1, 1].plot(loads, collisions, marker='o', label=label)
    axes[1, 1].set_title('Количество коллизий')
    axes[1, 1].set_xlabel('Коэффициент заполнения')
    axes[1, 1].set_ylabel('Коллизии')
    axes[1, 1].legend()
    axes[1, 1].grid(True)

    plt.tight_layout()
    plt.savefig('performance_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()


def run_performance_analysis():
    """Запускает полный анализ производительности."""
    configs = [
        ('chaining', 'polynomial', None, 'Цепочки'),
        ('open_addressing', 'polynomial', 'linear', 'Линейное'),
        ('open_addressing', 'polynomial', 'double', 'Двойное'),
    ]

    hash_funcs = {
        'simple': simple_hash,
        'polynomial': polynomial_hash,
        'djb2': djb2_hash
    }

    all_results = {}

    print("=== АНАЛИЗ ПРОИЗВОДИТЕЛЬНОСТИ ХЕШ-ТАБЛИЦ ===")

    print("\n1. Сравнение распределения хеш-функций...")
    compare_hash_functions()

    print("\n2. Сравнение методов разрешения коллизий...")
    for table_type, hash_name, probe_method, label in configs:
        print(f"   Тестирование: {label}")
        results = measure_performance(
            table_type=table_type,
            hash_func=hash_funcs[hash_name],
            probe_method=probe_method,
            initial_size=1000,
            num_operations=2000
        )
        all_results[label] = results

    print("\n3. Построение графиков...")
    plot_performance_results(all_results)

    print("\n=== АНАЛИЗ ЗАВЕРШЕН ===")
    print("Созданы файлы:")
    print("  - hash_distribution.png")
    print("  - performance_comparison.png")


if __name__ == '__main__':
    run_performance_analysis()
