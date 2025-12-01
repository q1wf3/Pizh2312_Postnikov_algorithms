"""
Реализация хеш-таблицы с открытой адресацией.
"""

from typing import Any, Optional, Tuple
from hash_functions import polynomial_hash, double_hash


class HashTableOpenAddressing:
    """
    Хеш-таблица с открытой адресацией.

    Особенности:
        - Все элементы хранятся в массиве
        - Разрешение коллизий через probing sequence
        - Поддерживает линейное пробирование и двойное хеширование
    """

    def __init__(self, initial_size: int = 16, load_factor: float = 0.75,
                 probe_method: str = 'linear', hash_func=polynomial_hash):
        """
        Инициализация хеш-таблицы.

        Args:
            initial_size: Начальный размер таблицы
            load_factor: Коэффициент заполнения
            probe_method: Метод пробирования
            hash_func: Основная хеш-функция
        """
        self.size = initial_size
        self.load_factor = load_factor
        self.probe_method = probe_method
        self.hash_func = hash_func
        self.table = [None] * self.size
        self.count = 0
        self.DELETED = object()

    def _hash(self, key: str, attempt: int) -> int:
        """Вычисляет хеш-значение с учетом номера попытки."""
        if self.probe_method == 'linear':
            return (self.hash_func(key, self.size) + attempt) % self.size
        elif self.probe_method == 'double':
            return double_hash(key, self.size, attempt)
        else:
            raise ValueError("Неизвестный метод пробирования")

    def _resize(self, new_size: int) -> None:
        """Изменяет размер таблицы и перехеширует все элементы."""
        old_table = self.table
        self.size = new_size
        self.table = [None] * self.size
        self.count = 0

        for item in old_table:
            if item is not None and item != self.DELETED:
                key, value = item
                self.insert(key, value)

    def insert(self, key: str, value: Any) -> None:
        """
        Вставляет пару ключ-значение в таблицу.

        Временная сложность:
            - В среднем: O(1/(1-α))
            - В худшем случае: O(n)
        """
        if self.count / self.size > self.load_factor:
            self._resize(self.size * 2)

        attempt = 0
        while attempt < self.size:
            index = self._hash(key, attempt)

            if (self.table[index] is None or
                    self.table[index] == self.DELETED or
                    (self.table[index] is not None and
                     self.table[index][0] == key)):

                self.table[index] = (key, value)
                if (self.table[index] is None or
                        self.table[index] == self.DELETED):
                    self.count += 1
                return

            attempt += 1

        self._resize(self.size * 2)
        self.insert(key, value)

    def search(self, key: str) -> Optional[Any]:
        """
        Ищет значение по ключу.

        Временная сложность:
            - В среднем: O(1/(1-α))
            - В худшем случае: O(n)
        """
        attempt = 0
        while attempt < self.size:
            index = self._hash(key, attempt)

            if self.table[index] is None:
                return None
            elif (self.table[index] != self.DELETED and
                  self.table[index][0] == key):
                return self.table[index][1]

            attempt += 1

        return None

    def delete(self, key: str) -> bool:
        """
        Удаляет пару ключ-значение.

        Returns:
            True если элемент был удален, False если не найден
        """
        attempt = 0
        while attempt < self.size:
            index = self._hash(key, attempt)

            if self.table[index] is None:
                return False
            elif (self.table[index] != self.DELETED and
                  self.table[index][0] == key):
                self.table[index] = self.DELETED
                self.count -= 1
                return True

            attempt += 1

        return False

    def get_load_factor(self) -> float:
        """Возвращает текущий коэффициент заполнения."""
        return self.count / self.size

    def get_probe_stats(self) -> Tuple[int, float]:
        """
        Возвращает статистику пробирования.

        Returns:
            (total_probes, average_probes_per_operation)
        """
        total_probes = 0
        operations = 0

        for item in self.table:
            if item is not None and item != self.DELETED:
                key, _ = item
                attempt = 0
                while attempt < self.size:
                    index = self._hash(key, attempt)
                    total_probes += 1
                    if (self.table[index] is not None and
                            self.table[index] != self.DELETED and
                            self.table[index][0] == key):
                        break
                    attempt += 1
                operations += 1

        if operations > 0:
            avg_probes = total_probes / operations
        else:
            avg_probes = 0

        return total_probes, avg_probes
