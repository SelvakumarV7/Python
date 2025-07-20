# Thread Synchronisation: process to ensure communication between threads.
# Lock: synchronization mechanism which helps to one thread to allow for synchronize(modify)
# Semaphore: it allows to shared resources but limit the number of threads.

import threading
import time

# lock:

lock = threading.Lock()

def task1():
    # acquire a lock
    lock.acquire()
    print('Task 1 Started')
    time.sleep(5)
    print('Task 1 Completed')
    # release lock
    lock.release()

def task2():
    lock.acquire()
    print('Task 2 Started')
    time.sleep(2)
    lock.release()

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()

print('Lock tasks completed')

# semaphore:

semaphore = threading.Semaphore()

def task3():
    semaphore.acquire()
    print('Task 3 Started')
    time.sleep(5)
    print('Task 3 Completed')
    semaphore.release()

def task4():
    semaphore.acquire()
    print('Task 4 started')
    time.sleep(2)
    print('Task 4 completed')
    semaphore.release()

t3 = threading.Thread(target=task3)
t4 = threading.Thread(target=task4)

t3.start()
t4.start()

t3.join()
t4.join()

print('Semaphore Tasks completed')