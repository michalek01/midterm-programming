import time
import random
import matplotlib.pyplot as plt

# =======================================================
# DO NOT MODIFY THE ALGORITHM IMPLEMENTATIONS
# =======================================================

def find_duplicates_slow(data):
    """An O(n^2) algorithm to find duplicates."""
    n = len(data)
    for i in range(n):
        for j in range(i + 1, n):
            if data[i] == data[j]:
                return True
    return False

def find_duplicates_fast(data):
    """An O(n) algorithm to find duplicates."""
    seen = set()
    for item in data:
        if item in seen:
            return True
        seen.add(item)
    return False


# =======================================================
# YOUR TASK: FIX THE BENCHMARKING SCRIPT BELOW
# =======================================================

def benchmark():
    """
    Properly benchmark the two algorithms across multiple input sizes.
    """
    print("Running benchmark...")

    sizes = [1000, 2000, 4000, 8000]

    for n in sizes:
        data = [random.randint(0, 10000) for _ in range(n)]

        start_time = time.perf_counter()
        find_duplicates_slow(data)
        end_time = time.perf_counter()
        slow_time = end_time - start_time

        start_time = time.perf_counter()
        find_duplicates_fast(data)
        end_time = time.perf_counter()
        fast_time = end_time - start_time

        print(f"n = {n}")
        print(f"Slow algorithm: {slow_time:.6f} seconds")
        print()  # Add a blank line for better readability between different input sizes
        print(f"Fast algorithm: {fast_time:.6f} seconds")

if __name__ == "__main__":
    benchmark()

#plot benchmark results

    sizes = [1000, 2000, 4000, 8000]
    slow_times = []
    fast_times = []

    for n in sizes:
        data = [random.randint(0, 10000) for _ in range(n)]

        start_time = time.perf_counter()
        find_duplicates_slow(data)
        end_time = time.perf_counter()
        slow_times.append(end_time - start_time)

        start_time = time.perf_counter()
        find_duplicates_fast(data)
        end_time = time.perf_counter()
        fast_times.append(end_time - start_time)

    plt.plot(sizes, slow_times, label="Slow Algorithm")
    plt.plot(sizes, fast_times, label="Fast Algorithm")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Time (seconds)")
    plt.title("Benchmark Results")
    plt.legend()
    plt.show()