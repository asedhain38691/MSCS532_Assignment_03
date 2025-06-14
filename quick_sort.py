import random
import timeit


def random_pivot(arr, low, high):
    return random.randint(low, high)


def first_element_pivot(arr, low, high):
    return low


def quicksort(pivot_selector, arr):
    def _quicksort(low, high):
        if low < high:
            pivot_index = partition_with_custom_pivot(low, high)
            _quicksort(low, pivot_index - 1)
            _quicksort(pivot_index + 1, high)

    def partition_with_custom_pivot(low, high):
        pivot_index = pivot_selector(arr, low, high)
        arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
        return partition(low, high)

    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    if arr is None or len(arr) <= 1:
        return arr

    _quicksort(0, len(arr) - 1)
    return arr


def randomized_quicksort(arr):
    return quicksort(random_pivot, arr)


def deterministic_quicksort(arr):
    return quicksort(first_element_pivot, arr)


def generate_random_array(size):
    return [random.randint(0, 10000) for _ in range(size)]


def generate_sorted_array(size):
    return list(range(size))


def generate_reverse_sorted_array(size):
    return list(range(size, 0, -1))


def generate_repeated_array(size):
    return [42] * size


def benchmark(name, array_gen, sort_fn, num_runs=5, size=1000):
    setup_code = f"""
from __main__ import {sort_fn.__name__}, {array_gen.__name__}
import random
import sys
sys.setrecursionlimit(5000)

arr = {array_gen.__name__}({size})
"""
    stmt = f"{sort_fn.__name__}(arr.copy())"
    time = timeit.timeit(stmt=stmt, setup=setup_code, number=num_runs)
    print(f"{name:<35} | {sort_fn.__name__:<20} | {time:.6f} sec (avg over {num_runs})")


def run_all_benchmarks():
    sizes = [1000]
    input_types = [
        ("Random array", generate_random_array),
        ("Sorted array", generate_sorted_array),
        ("Reverse-sorted array", generate_reverse_sorted_array),
        ("Repeated elements", generate_repeated_array),
    ]
    sort_functions = [randomized_quicksort, deterministic_quicksort]

    for size in sizes:
        print(f"\nArray Size: {size}")
        print(f"{'Test Case':<20} | {'Pivot Strategy':<35} | Time")
        print("-" * 70)
        for name, gen_fn in input_types:
            for sort_fn in sort_functions:
                benchmark(name, gen_fn, sort_fn, num_runs=100, size=size)


if __name__ == "__main__":
    run_all_benchmarks()
