"""
Output numbers from 0..100 in order.
By synchronizing threads with Timer object.
First thread outputs even numbers. Second thread outputs odd numbers.
"""

from threading import Timer
from time import sleep

count = 0
LIMIT = 100


def print_numbers(number, limit):
    global count
    while count < limit:
        count += 1
        print("{0} {1}".format(number, count))
        sleep(1)


def start_timer():
    t = Timer(1, print_numbers, args=["Thread-1", LIMIT])
    t2 = Timer(2, print_numbers, args=['Thread-2', LIMIT])

    t.start()
    t2.start()
