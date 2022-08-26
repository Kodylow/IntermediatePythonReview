# Threads: an entity WITHIN a process that can be scheduled. A process can spawn multiple threads.

from threading import Thread, Lock, current_thread
import time

database_value = 0

def increase(lock):
    global database_value

    # context manager 'with', acquires and releases locks
    with lock:
        local_copy = database_value
    
        # processing
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy

if __name__ == "__main__":

    lock = Lock()
    print('start value', database_value)

    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()

    print('end value', database_value)
    print('end main')


# Queuing Threads

from queue import Queue
    # q = Queue()
    # q.put(1)
    # q.put(2)
    # q.put(3)
    # # 3,2,1 ->

    # first = q.get()

    # bool = q.empty()

    # q.task_done() # call when thread done processing

    # q.join() # wait for all elements in q to finish processing

def worker(q, lock):
    while True:
        value = q.get()

        # processing
        with lock: 
            print(f'in {current_thread().name} got {value}')
        q.task_done()

if __name == "__main__":

    q = Queue()
    lock = Lock()
    num_threads = 10

    for i in range(num_threads):
        t = Thread(target=worker, args=(q, lock))
        t.daemon = True
        t.start()

    for i in range(1,21):
        q.put(i)

    q.join()

    print("end main")