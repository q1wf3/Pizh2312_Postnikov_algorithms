import time
import random
import string

from hash_table_chaining import HashTableChaining
from hash_table_open_addressing import HashTableOpenAddressing


def generate_random_string(length: int = 10) -> str:
    """Генерирует случайную строку."""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))


def measure_performance(
    table_type,
    hash_func,
    probe_method=None,
    initial_size=100,
    load_factors=None,
    num_operations=1000
):
    """
    Измеряет производительность хеш-таблиц.
    """
    if load_factors is None:
        load_factors = [0.1, 0.5, 0.7, 0.9]

    results = {}

    for load_factor in load_factors:
        if table_type == 'chaining':
            table = HashTableChaining(
                initial_size=initial_size,
                load_factor=load_factor,
                hash_func=hash_func
            )
        else:
            table = HashTableOpenAddressing(
                initial_size=initial_size,
                load_factor=load_factor,
                probe_method=probe_method,
                hash_func=hash_func
            )

        num_elements = int(initial_size * load_factor)
        test_data = [
            (generate_random_string(), i)
            for i in range(num_elements)
        ]

        start = time.time()
        for key, value in test_data:
            table.insert(key, value)
        insert_time = time.time() - start

        start = time.time()
        for key, _ in test_data:
            table.search(key)
        search_time = time.time() - start

        start = time.time()
        for key, _ in test_data:
            table.delete(key)
        delete_time = time.time() - start

        if table_type == 'chaining':
            collisions, _ = table.get_collision_stats()
        else:
            probes, _ = table.get_probe_stats()
            collisions = probes

        results[load_factor] = {
            "insert_time": insert_time,
            "search_time": search_time,
            "delete_time": delete_time,
            "collisions": collisions,
            "load_factor": table.get_load_factor()
        }

    return results
