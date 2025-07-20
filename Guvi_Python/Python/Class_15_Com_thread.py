# Thread Communication:

import threading

# condition variable.

condition = threading.Condition()

def my_thread():
    with condition:
        print('Thread Waiting for Signal')
        condition.wait()
        print('Thread received Signal')

t = threading.Thread(target=my_thread)
t.start()

with condition:
    print('Sending Signal')
    condition.notify()


t.join()


import threading

def print_cube(num):
    print("Cube: {}" .format(num * num * num))

def print_square(num):
    print("Square: {}" .format(num * num))

if __name__ =="__main__":
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

t1.start()
t2.start()

t1.join()
t2.join()

import threading
import queue

def producer(q):
    for i in range(3):
        q.put(i)

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print("Processed item:", item)

q = queue.Queue()
t1 = threading.Thread(target=producer, args=(q,))
t2 = threading.Thread(target=consumer, args=(q,))
t1.start()
t2.start()
q.put(None)
t1.join()
t2.join()