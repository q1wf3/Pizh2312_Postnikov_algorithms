"""
Модуль с оптимизированными рекурсивными алгоритмами с мемоизацией.
"""

from functools import wraps
import time
import matplotlib.pyplot as plt  # Добавляем импорт для графика


def memoize(func):
    """Декоратор для мемоизации функций."""
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return wrapper


@memoize
def fibonacci_memoized(n):
    """
    Вычисление n-го числа Фибоначчи с мемоизацией.

    Args:
        n (int): Номер числа Фибоначчи.

    Returns:
        int: n-е число Фибоначчи.

    Временная сложность: O(n)
    Глубина рекурсии: O(n)
    """
    if n < 0:
        raise ValueError(
            "Номер числа Фибоначчи должен быть неотрицательным"
        )
    if n == 0:
        return 0
    if n == 1:
        return 1
    return (fibonacci_memoized(n - 1) +
            fibonacci_memoized(n - 2))


class FibonacciCounter:
    """Класс для подсчета вызовов рекурсивных функций."""

    def __init__(self):
        """Инициализация счетчика."""
        self.calls = 0

    def fibonacci_counted(self, n):
        """
        Числа Фибоначчи с подсчетом вызовов.

        Args:
            n (int): Номер числа Фибоначчи.

        Returns:
            int: n-е число Фибоначчи.
        """
        self.calls += 1
        if n < 0:
            raise ValueError(
                "Номер числа Фибоначчи должен быть неотрицательным"
            )
        if n == 0:
            return 0
        if n == 1:
            return 1
        return (self.fibonacci_counted(n - 1) +
                self.fibonacci_counted(n - 2))

    def reset_counter(self):
        """Сброс счетчика вызовов."""
        self.calls = 0


def compare_fibonacci_performance(n=35):
    """
    Сравнение производительности наивной и мемоизированной версий.

    Args:
        n (int): Номер числа Фибоначчи для теста.
    """
    counter = FibonacciCounter()

    print(f"Сравнение для n = {n}")
    print("-" * 50)

    # Наивная версия с подсчетом вызовов
    start_time = time.time()
    counter.reset_counter()
    result_naive = counter.fibonacci_counted(n)
    time_naive = time.time() - start_time
    calls_naive = counter.calls

    # Мемоизированная версия
    start_time = time.time()
    result_memo = fibonacci_memoized(n)
    time_memo = time.time() - start_time

    print(f"Результат: {result_naive}")
    print(f"Наивная версия: {time_naive:.6f} сек")
    print(f"Количество вызовов: {calls_naive}")
    print(f"Мемоизированная: {time_memo:.6f} сек")
    print(f"Ускорение: {time_naive / time_memo:.2f}x")

    # Проверяем, что результаты совпадают
    if result_naive == result_memo:
        print("Результаты совпадают ✓")
    else:
        print("Ошибка: результаты не совпадают ✗")


def plot_comparison():
    """
    Построение графика сравнения наивного и мемоизированного подхода.
    Требование из задания: Построить график сравнения.
    """
    from recursion import fibonacci

    n_values = list(range(1, 20))
    naive_times = []
    memo_times = []

    print("\nИзмерение для графика...")
    for n in n_values:
        # Наивная версия
        start = time.time()
        fibonacci(n)
        naive_times.append(time.time() - start)

        # Мемоизированная версия
        start = time.time()
        fibonacci_memoized(n)
        memo_times.append(time.time() - start)

    # Построение графика
    plt.figure(figsize=(10, 6))
    plt.plot(n_values, naive_times, 'ro-', label='Наивная рекурсия',
             linewidth=2)
    plt.plot(n_values, memo_times, 'go-', label='С мемоизацией',
             linewidth=2)
    plt.xlabel('n (номер числа Фибоначчи)')
    plt.ylabel('Время выполнения (секунды)')
    title = 'Сравнение производительности: наивная рекурсия vs мемоизация'
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.savefig('fibonacci_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("График сохранен как 'fibonacci_comparison.png'")


if __name__ == "__main__":
    compare_fibonacci_performance(35)
    plot_comparison()
