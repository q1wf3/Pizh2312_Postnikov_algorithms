# task_solutions.py
from collections import deque


def check_brackets(expression):
    """Проверка сбалансированности скобок с использованием стека - O(n)."""
    stack = []  # O(1)
    brackets = {')': '(', '}': '{', ']': '['}  # O(1)

    for char in expression:  # O(n)
        if char in '({[':  # O(1)
            stack.append(char)  # O(1)
        elif char in ')}]':  # O(1)
            if not stack:  # O(1)
                return False
            if stack.pop() != brackets[char]:  # O(1)
                return False

    return len(stack) == 0  # O(1)
    # Общая сложность: O(n)


def simulate_print_queue():
    """Симуляция очереди печати с использованием deque - O(n)."""
    print_queue = deque()  # O(1)

    # Добавление задач в очередь
    tasks = ["doc1.pdf", "doc2.docx", "image.png", "report.pdf"]  # O(1)
    for task in tasks:  # O(n)
        print_queue.append(task)  # O(1)
        print(f"Добавлена задача: {task}")

    print("\nОбработка задач:")
    while print_queue:  # O(n)
        current_task = print_queue.popleft()  # O(1)
        print(f"Печатается: {current_task}")
    # Общая сложность: O(n)


def is_palindrome(sequence):
    """Проверка палиндрома с использованием дека - O(n)."""
    dq = deque(sequence)  # O(n)

    while len(dq) > 1:  # O(n)
        if dq.popleft() != dq.pop():  # O(1)
            return False

    return True  # O(1)
    # Общая сложность: O(n)


if __name__ == "__main__":
    print("1. Проверка сбалансированности скобок:")
    tests = ["({[]})", "({[}])", "((()))", "()}"]
    for test in tests:
        result = check_brackets(test)
        status = 'Сбалансировано' if result else 'Не сбалансировано'
        print(f"'{test}': {status}")

    print("\n2. Симуляция очереди печати:")
    simulate_print_queue()

    print("\n3. Проверка палиндромов:")
    words = ["радар", "level", "hello", "a", "12321" "радар"]
    for word in words:
        result = is_palindrome(word)
        status = 'Палиндром' if result else 'Не палиндром'
        print(f"'{word}': {status}")
