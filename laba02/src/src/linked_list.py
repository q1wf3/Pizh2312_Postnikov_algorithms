# linked_list.py
class Node:
    def __init__(self, data):
        self.data = data  # O(1)
        self.next = None  # O(1)


class LinkedList:
    def __init__(self):
        self.head = None  # O(1)

    def insert_at_start(self, data):
        """Вставка в начало - O(1)"""
        new_node = Node(data)  # O(1)
        new_node.next = self.head  # O(1)
        self.head = new_node  # O(1)
        # Общая сложность: O(1)

    def insert_at_end(self, data):
        """Вставка в конец - O(n)"""
        new_node = Node(data)  # O(1)

        if self.head is None:  # O(1)
            self.head = new_node  # O(1)
            return

        current = self.head  # O(1)
        while current.next:  # O(n)
            current = current.next  # O(1)
        current.next = new_node  # O(1)
        # Общая сложность: O(n)

    def delete_from_start(self):
        """Удаление из начала - O(1)"""
        if self.head is None:  # O(1)
            return None
        data = self.head.data  # O(1)
        self.head = self.head.next  # O(1)
        return data  # O(1)
        # Общая сложность: O(1)

    def traversal(self):
        """Обход списка - O(n)"""
        elements = []  # O(1)
        current = self.head  # O(1)
        while current:  # O(n)
            elements.append(current.data)  # O(1)
            current = current.next  # O(1)
        return elements  # O(1)
        # Общая сложность: O(n)


if __name__ == "__main__":
    # Демонстрация работы LinkedList
    print("Демонстрация работы LinkedList:")
    ll = LinkedList()

    print("Вставка элементов в начало:")
    ll.insert_at_start(3)
    ll.insert_at_start(2)
    ll.insert_at_start(1)
    print(f"Элементы: {ll.traversal()}")

    print("Вставка элемента в конец:")
    ll.insert_at_end(4)
    print(f"Элементы: {ll.traversal()}")

    print("Удаление из начала:")
    deleted = ll.delete_from_start()
    print(f"Удален элемент: {deleted}")
    print(f"Элементы: {ll.traversal()}")
