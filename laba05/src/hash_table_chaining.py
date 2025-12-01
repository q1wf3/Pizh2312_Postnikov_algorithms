"""
Реализация хеш-таблицы с методом цепочек для разрешения коллизий.
"""

from typing import Any, Optional, Tuple
from hash_functions import polynomial_hash


class HashTableChaining:
    """
    Хеш-таблица с методом цепочек.

    Особенности:
        - Коллизии разрешаются с помощью связных списков
        - Динамическое масштабирование
        - Средняя сложность операций: O(1 + α)
    """

    def __init__(self, initial_size: int = 16, load_factor: float = 0.75,
                 hash_func=polynomial_hash):
        """
        Инициализация хеш-таблицы.

        Args:
            initial_size: Начальный размер таблицы
            load_factor: Коэффициент заполнения
            hash_func: Используемая хеш-функция
        """
        self.size = initial_size
        self.load_factor = load_factor
        self.hash_func = hash_func
        self.table = [[] for _ in range(self.size)]
        self.count = 0

    def _hash(self, key: str) -> int:
        """Вычисляет хеш-значение для ключа."""
        return self.hash_func(key, self.size)

    def _resize(self, new_size: int) -> None:
        """Изменяет размер таблицы и перехеширует все элементы."""
        old_table = self.table
        self.size = new_size
        self.table = [[] for _ in range(self.size)]
        self.count = 0

        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)

    def insert(self, key: str, value: Any) -> None:
        """
        Вставляет пару ключ-значение в таблицу.

        Временная сложность:
            - В среднем: O(1)
            - В худшем случае: O(n)
        """
        if self.count / self.size > self.load_factor:
            self._resize(self.size * 2)

        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.count += 1

    def search(self, key: str) -> Optional[Any]:
        """
        Ищет значение по ключу.

        Временная сложность:
            - В среднем: O(1)
            - В худшем случае: O(n)
        """
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key: str) -> bool:
        """
        Удаляет пару ключ-значение.

        Returns:
            True если элемент был удален, False если не найден
        """
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.count -= 1
                return True
        return False

    def get_load_factor(self) -> float:
        """Возвращает текущий коэффициент заполнения."""
        return self.count / self.size

    def get_collision_stats(self) -> Tuple[int, float]:
        """
        Возвращает статистику коллизий.

        Returns:
            (total_collisions, average_collisions_per_bucket)
        """
        total_collisions = 0
        non_empty_buckets = 0

        for bucket in self.table:
            if len(bucket) > 0:
                total_collisions += len(bucket) - 1
                non_empty_buckets += 1

        if non_empty_buckets > 0:
            avg_collisions = total_collisions / non_empty_buckets
        else:
            avg_collisions = 0

        return total_collisions, avg_collisions
