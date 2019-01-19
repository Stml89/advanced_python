"""
Output numbers from 0..100 in order.
First thread outputs even numbers. Second thread outputs odd numbers.

By synchronizing processes with
Lock object and shared counter with Value object.
"""

import multiprocessing
import time


def print_numbers(thread_name, delay, counter):
    with lock:
        time.sleep(delay)
        print("{} {}".format(thread_name, counter.value))
        counter.value += 1


def print_even_numbers(name, sleep_time, counter):
    while counter.value <= 100:
        if not counter.value % 2:
            print_numbers(name, sleep_time, counter)


def print_odd_numbers(name, sleep_time, counter):
    while counter.value <= 100:
        if counter.value % 2:
            print_numbers(name, sleep_time, counter)


if __name__ == '__main__':
    count = multiprocessing.Value('i', 0)
    lock = multiprocessing.Lock()

    process_1 = multiprocessing.Process(target=print_even_numbers,
                                        args=("Process-1", 1, count))
    process_2 = multiprocessing.Process(target=print_odd_numbers,
                                        args=("Process-2", 1, count))

    process_1.start()
    process_2.start()
