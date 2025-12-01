"""
Модуль с классическими рекурсивными алгоритмами.
"""


def factorial(n):
    """
    Вычисление факториала числа n рекурсивным способом.

    Args:
        n (int): Неотрицательное целое число.

    Returns:
        int: Факториал числа n.

    Raises:
        ValueError: Если n < 0.

    Временная сложность: O(n)
    Глубина рекурсии: O(n)
    """
    if n < 0:
        raise ValueError(
            "Факториал определен только для неотрицательных чисел"
        )
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """
    Вычисление n-го числа Фибоначчи наивным рекурсивным способом.

    Args:
        n (int): Номер числа Фибоначчи (n >= 0).

    Returns:
        int: n-е число Фибоначчи.

    Raises:
        ValueError: Если n < 0.

    Временная сложность: O(2^n)
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
    return fibonacci(n - 1) + fibonacci(n - 2)


def fast_power(a, n):
    """
    Быстрое возведение числа a в степень n через степень двойки.

    Args:
        a (float): Основание.
        n (int): Показатель степени (неотрицательное целое).

    Returns:
        float: a в степени n.

    Raises:
        ValueError: Если n < 0.

    Временная сложность: O(log n)
    Глубина рекурсии: O(log n)
    """
    if n < 0:
        raise ValueError(
            "Показатель степени должен быть неотрицательным"
        )
    if n == 0:
        return 1
    if n == 1:
        return a

    # Если степень четная
    if n % 2 == 0:
        half_power = fast_power(a, n // 2)
        return half_power * half_power
    # Если степень нечетная
    else:
        return a * fast_power(a, n - 1)


if __name__ == "__main__":
    # Тестирование функций
    print("Факториал 5:", factorial(5))
    print("Число Фибоначчи F(6):", fibonacci(6))
    print("2^10:", fast_power(2, 10))
