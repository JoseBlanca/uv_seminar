# primes_threads.py
import math
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def count_primes(start: int, end: int) -> int:
    return sum(is_prime(n) for n in range(start, end))


def threaded_count_primes(ranges, n_threads=4):
    with ThreadPoolExecutor(max_workers=n_threads) as ex:
        futures = (ex.submit(count_primes, a, b) for (a, b) in ranges)
        return sum(f.result() for f in as_completed(futures))


if __name__ == "__main__":
    N = 10_000_000
    ranges = [(i, i + N // 4) for i in range(2, N, N // 4)]

    for threads in [1, 4]:
        t0 = time.perf_counter()
        result = threaded_count_primes(ranges, n_threads=threads)
        t1 = time.perf_counter()
        print(f"{threads} threads → {result} primes in {t1 - t0:.2f}s")
