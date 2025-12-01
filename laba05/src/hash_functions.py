"""
Модуль с реализацией различных хеш-функций для строковых ключей.
"""


def simple_hash(key: str, table_size: int) -> int:
    """
    Простая хеш-функция - сумма кодов символов.

    Args:
        key: Строковый ключ
        table_size: Размер хеш-таблицы

    Returns:
        Хеш-значение в диапазоне [0, table_size-1]
    """
    hash_value = 0
    for char in key:
        hash_value += ord(char)
    return hash_value % table_size


def polynomial_hash(key: str, table_size: int, base: int = 31) -> int:
    """
    Полиномиальная хеш-функция.

    Args:
        key: Строковый ключ
        table_size: Размер хеш-таблицы
        base: Основание полинома

    Returns:
        Хеш-значение в диапазоне [0, table_size-1]
    """
    hash_value = 0
    for char in key:
        hash_value = (hash_value * base + ord(char)) % table_size
    return hash_value


def djb2_hash(key: str, table_size: int) -> int:
    """
    Хеш-функция DJB2.

    Args:
        key: Строковый ключ
        table_size: Размер хеш-таблицы

    Returns:
        Хеш-значение в диапазоне [0, table_size-1]
    """
    hash_value = 5381
    for char in key:
        hash_value = ((hash_value << 5) + hash_value) + ord(char)
    return hash_value % table_size


def double_hash(key: str, table_size: int, attempt: int) -> int:
    """
    Вторая хеш-функция для двойного хеширования.

    Args:
        key: Строковый ключ
        table_size: Размер хеш-таблицы
        attempt: Номер попытки

    Returns:
        Хеш-значение для шага probing
    """
    hash1 = polynomial_hash(key, table_size)
    hash2 = 1 + (simple_hash(key, table_size - 2))
    return (hash1 + attempt * hash2) % table_size
