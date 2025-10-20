# performance_analysis.py
import timeit


def compare_list_vs_linkedlist():
    """Сравнение list и LinkedList для вставки в начало."""
    print("Сравнение 1000 вставок в начало:")
    print("Структура      | Время (сек)")
    print("-" * 30)

    # List - O(n) на каждую операцию insert(0)
    list_time = timeit.timeit(
        'lst.insert(0, 1)',  # O(n) - вставка в начало list
        setup='lst = list(range(1000))',
        number=1000
    )

    # LinkedList - O(1) на каждую операцию insert_at_start
    linked_list_time = timeit.timeit(
        'll.insert_at_start(1)',  # O(1) - вставка в начало LinkedList
        setup='''
class Node:
    def __init__(self, data):  # O(1)
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):  # O(1)
        self.head = None

    def insert_at_start(self, data):  # O(1)
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

ll = LinkedList()
for i in range(1000):
    ll.insert_at_start(i)
        ''',
        number=1000
    )

    print(f"List          | {list_time:.6f}")
    print(f"LinkedList    | {linked_list_time:.6f}")


def compare_list_vs_deque():
    """Сравнение list и deque для удаления из начала."""
    print("\nСравнение 1000 удалений из начала:")
    print("Структура      | Время (сек)")
    print("-" * 30)

    # List - O(n) на каждую операцию pop(0)
    list_time = timeit.timeit(
        'lst.pop(0)',  # O(n) - удаление из начала list
        setup='lst = list(range(1000))',
        number=1000
    )

    # Deque - O(1) на каждую операцию popleft()
    deque_time = timeit.timeit(
        'dq.popleft()',  # O(1) - удаление из начала deque
        setup='from collections import deque; dq = deque(range(1000))',
        number=1000
    )

    print(f"List (pop(0))  | {list_time:.6f}")
    print(f"Deque (popleft)| {deque_time:.6f}")


if __name__ == "__main__":
    compare_list_vs_linkedlist()
    compare_list_vs_deque()
