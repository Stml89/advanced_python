"""
Output numbers from 0..100 in order.
By synchronizing threads with Lock object.
First thread outputs even numbers. Second thread outputs odd numbers.
"""

import threading
import time

count = 0
lock = threading.Lock()


def print_numbers(thread_name, delay):
    global count
    with lock:
        time.sleep(delay)
        print("{} {}".format(thread_name, count))
        count += 1


def print_even_numbers(name, sleep_time):
    while count <= 100:
        if not count % 2:
            print_numbers(name, sleep_time)


def print_odd_numbers(name, sleep_time):
    while count <= 100:
        if count % 2:
            print_numbers(name, sleep_time)


def start_lock():
    t1 = threading.Thread(target=print_even_numbers, args=("Thread-1", 1))
    t2 = threading.Thread(target=print_odd_numbers, args=("Thread-2", 1))

    t1.start()
    t2.start()
