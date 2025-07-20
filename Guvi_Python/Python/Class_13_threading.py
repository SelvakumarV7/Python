# Thread:
# Multi-Tasking:
    # Threads
    # Processes

# Concurrent Programming: ability of a program to execute a program by using threads.
# GIL(Global Interpreter Lock) Mechanism is to prevent multiple threads from byte execution.
    # Race Conditions: Numpy and Pandas

import threading
import time
from time import sleep


def my_function(arg1, arg2):
    print('Running my function: ', arg1, arg2)

# To create a thread:
t = threading.Thread(target=my_function(1,2))   # create a thread

# to start a thread:
t.start()

# wait for a thread:
t.join()

print('Thread has completed')
print()

# Thread class methods:

def task1():
    print('Task 1 started')
    time.sleep(5)
    print('Task 1 completed')

def task2():
    print('Task 2 started')
    time.sleep(3)
    print('Task 2 completed')

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()

print("Both Task completed")