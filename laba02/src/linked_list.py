"""Реализация односвязного списка для ЛР-02."""


class Node:
    """Узел списка."""

    def __init__(self, data):
        """Инициализация узла."""
        self.data = data
        self.next = None


class LinkedList:
    """Односвязный список с поддержкой head и tail."""

    def __init__(self):
        """Инициализация пустого списка."""
        self.head = None
        self.tail = None

    def insert_at_start(self, data) -> None:
        """Вставка в начало. Сложность O(1)."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data) -> None:
        """Вставка в конец. Сложность O(1) с tail."""
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def delete_from_start(self):
        """Удаление из начала. Сложность O(1)."""
        if self.head is None:
            return None
        value = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return value

    def traversal(self) -> list:
        """Обход списка. Сложность O(n)."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def is_empty(self) -> bool:
        """Проверка на пустоту. Сложность O(1)."""
        return self.head is None

    def size(self) -> int:
        """Размер списка. Сложность O(n)."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


if __name__ == "__main__":
    # Демонстрация работы связного списка
    ll = LinkedList()
    ll.insert_at_start(10)
    ll.insert_at_start(20)
    ll.insert_at_end(5)
    print("Список:", ll.traversal())
    print("Размер:", ll.size())
    print("Удалено:", ll.delete_from_start())
    print("После удаления:", ll.traversal())
