"""
Output numbers from 0..100 in order.
By synchronizing threads with Semaphore object.
First thread outputs even numbers. Second thread outputs odd numbers.
"""

import threading
import time

count = 0


def even_numbers(es, os):
    global count
    while count < 100:
        es.acquire()
        count += 1 if not count == 0 else count
        print("Thread1 {}".format(count))
        os.release()
    os.release()


def odd_numbers(es, os):
    global count
    while count < 99:
        os.acquire()
        count += 1
        print("Thread2 {}".format(count))
        es.release()


even_sem = threading.Semaphore(1)
odd_sem = threading.Semaphore(0)

even = threading.Thread(name='even_numbers', target=even_numbers,
                        args=(even_sem, odd_sem))
odd = threading.Thread(name='odd_numbers', target=odd_numbers,
                       args=(even_sem, odd_sem))
even.start()
time.sleep(2)
odd.start()
