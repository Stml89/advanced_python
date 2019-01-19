"""
Output numbers from 0..100 in order.
By synchronizing threads with Condition object.
First thread outputs even numbers. Second thread outputs odd numbers.
"""

import threading
import time

count = 0


def consumer(cv, name):
    global count
    while count < 100:
        with cv:
            cv.wait()
            print('{} {}'.format(name, count))
            count += 1
            cv.notify()


condition = threading.Condition()
cs1 = threading.Thread(name='consumer1', target=consumer,
                       args=(condition, "thread-1"))
cs2 = threading.Thread(name='consumer2', target=consumer,
                       args=(condition, "thread-2"))

cs1.start()
time.sleep(2)
cs2.start()

with condition:
    condition.notify()
