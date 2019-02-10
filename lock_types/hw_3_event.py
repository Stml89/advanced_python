"""
Output numbers from 0..100 in order.
By synchronizing threads with Event object.
First thread outputs even numbers. Second thread outputs odd numbers.
"""

import threading
import time

count = 0


def even(event):
    global count
    event.set()
    while count <= 100:
        if not count % 2:
            event.wait(1)
            print('Thread 1 {}'.format(count))
            count += 1
        event.clear()


def odd(event):
    global count
    while count <= 100:
        if count % 2:
            event.wait(1)
            print('Thread 2 {}'.format(count))
            count += 1
        event.set()

def start_event():
    print_event = threading.Event()

    first = threading.Thread(name='even', target=even, args=(print_event,))
    second = threading.Thread(name='odd', target=odd, args=(print_event,))

    first.start()
    time.sleep(1)
    second.start()
