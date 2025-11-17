"""Сравнительный анализ производительности структур данных."""
import timeit
from collections import deque
import matplotlib.pyplot as plt
from linked_list import LinkedList


def compare_insert_start(sizes: list[int]) -> tuple[list[float], list[float]]:
    """Сравнение вставки в начало: list vs LinkedList."""
    list_times = []
    linked_times = []

    for n in sizes:
        # Тестирование list
        lst = list(range(1000))  # Предварительное заполнение
        t_list = timeit.timeit(
            lambda: lst.insert(0, 1),
            number=n
        )
        list_times.append(t_list)

        # Тестирование LinkedList
        linked = LinkedList()
        for i in range(1000):  # Предварительное заполнение
            linked.insert_at_end(i)
        t_linked = timeit.timeit(
            lambda: linked.insert_at_start(1),
            number=n
        )
        linked_times.append(t_linked)

    return list_times, linked_times


def compare_queue(sizes: list[int]) -> tuple[list[float], list[float]]:
    """Сравнение очереди: deque.popleft() vs list.pop(0)."""
    deque_times = []
    list_pop_times = []

    for n in sizes:
        # Тестирование deque
        dq = deque(range(n * 2))  # Больше элементов
        t_deque = timeit.timeit(
            lambda: (dq.popleft() if dq else None),
            number=n
        )
        deque_times.append(t_deque)

        # Тестирование list
        lst = list(range(n * 2))
        t_list = timeit.timeit(
            lambda: (lst.pop(0) if lst else None),
            number=n
        )
        list_pop_times.append(t_list)

    return deque_times, list_pop_times


def plot_insert_graph(sizes: list[int], list_times: list[float],
                      linked_times: list[float]) -> None:
    """График сравнения вставки в начало."""
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, list_times, "r-o", label="list.insert(0)")
    plt.plot(sizes, linked_times, "b-o", label="LinkedList.insert_at_start")
    plt.xlabel("Количество операций (N)")
    plt.ylabel("Время выполнения (секунды)")
    plt.title("Вставка в начало: list vs LinkedList")
    plt.grid(True, linestyle="--", linewidth=0.5)
    plt.legend()
    plt.savefig("insert_comparison.png", dpi=300, bbox_inches="tight")
    plt.close()


def plot_queue_graph(sizes: list[int], deque_times: list[float],
                     list_pop_times: list[float]) -> None:
    """График сравнения очередей."""
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, list_pop_times, "r-o", label="list.pop(0)")
    plt.plot(sizes, deque_times, "b-o", label="deque.popleft()")
    plt.xlabel("Количество операций (N)")
    plt.ylabel("Время выполнения (секунды)")
    plt.title("Удаление из начала: list vs deque")
    plt.grid(True, linestyle="--", linewidth=0.5)
    plt.legend()
    plt.savefig("queue_comparison.png", dpi=300, bbox_inches="tight")
    plt.close()


def main() -> None:
    """Основной запуск: замеры и построение графиков."""
    sizes = [100, 500, 1000, 2000, 5000]

    print("Запуск сравнения вставки в начало...")
    list_times, linked_times = compare_insert_start(sizes)
    print("Запуск сравнения операций очереди...")
    deque_times, list_pop_times = compare_queue(sizes)

    print("Построение графиков...")
    plot_insert_graph(sizes, list_times, linked_times)
    plot_queue_graph(sizes, deque_times, list_pop_times)

    pc_info = """
Характеристики ПК для тестирования:
- Процессор: Intel(R) Xeon(R) CPU E3-1270 v3 @ 3.50GHz
- Оперативная память: 16 GB DDR4
- ОС: Windows 10
- Python: 3.13.2
"""
    print(pc_info)
    print("Графики сохранены:")
    print("- insert_comparison.png")
    print("- queue_comparison.png")


if __name__ == "__main__":
    main()
