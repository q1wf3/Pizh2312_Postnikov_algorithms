"""Решение практических задач с использованием структур данных."""
from collections import deque
from linked_list import LinkedList


def is_balanced_brackets(expression: str) -> bool:
    """
    Проверка сбалансированности скобок с использованием стека.

    Сложность: O(n), где n - длина выражения.
    """
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != brackets[char]:
                return False
            stack.pop()

    return len(stack) == 0


def is_palindrome_deque(sequence: str) -> bool:
    """
    Проверка палиндрома с использованием дека.

    Сложность: O(n), где n - длина последовательности.
    """
    dq = deque(sequence.lower().replace(" ", ""))

    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False

    return True


def print_queue_simulation(tasks: list[str]) -> None:
    """
    Симуляция обработки задач в очереди печати.

    Сложность: O(n), где n - количество задач.
    """
    queue = deque(tasks)
    time_elapsed = 0

    print("Начало симуляции очереди печати:")
    while queue:
        current_task = queue.popleft()
        time_elapsed += 1
        print(f"Время {time_elapsed}: обрабатывается '{current_task}'")

        # Имитация обработки
        if queue:
            print(f"        в очереди: {list(queue)}")
        else:
            print("        очередь пуста")

    print(f"Все задачи обработаны за {time_elapsed} единиц времени")


def demonstrate_linked_list() -> None:
    """Демонстрация работы связного списка."""
    print("\nДемонстрация связного списка:")
    ll = LinkedList()

    # Вставка в начало и конец
    ll.insert_at_start(10)
    ll.insert_at_start(20)
    ll.insert_at_end(30)
    ll.insert_at_end(40)

    print(f"Список после вставок: {ll.traversal()}")
    print(f"Размер списка: {ll.size()}")

    # Удаление из начала
    removed = ll.delete_from_start()
    print(f"Удален элемент: {removed}")
    print(f"Список после удаления: {ll.traversal()}")


def main() -> None:
    """Основная функция для демонстрации решений."""
    print("=== РЕШЕНИЕ ПРАКТИЧЕСКИХ ЗАДАЧ ===")

    # Задача 1: Проверка сбалансированности скобок
    test_expressions = [
        "({[]})",
        "({[}])",
        "((()))",
        "({[()]})",
        "({[(])})"
    ]

    print("1. Проверка сбалансированности скобок:")
    for expr in test_expressions:
        result = is_balanced_brackets(expr)
        status = "Сбалансировано" if result else "Не сбалансировано"
        print(f"   '{expr}' -> {status}")

    # Задача 2: Проверка палиндрома
    test_sequences = [
        "А роза упала на лапу Азора",
        "racecar",
        "hello",
        "Madam",
        "12321"
    ]

    print("\n2. Проверка палиндромов:")
    for seq in test_sequences:
        result = is_palindrome_deque(seq)
        status = "Палиндром" if result else "Не палиндром"
        print(f"   '{seq}' -> {status}")

    # Задача 3: Симуляция очереди печати
    tasks = ["Документ1", "Отчет", "Презентация", "Фото", "Чертеж"]
    print_queue_simulation(tasks)

    # Демонстрация связного списка
    demonstrate_linked_list()


if __name__ == "__main__":
    main()
