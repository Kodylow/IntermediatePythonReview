# Process: a program in execution (e.g. the Python interpreter itself)

from multiprocessing import Process, Value, Array, Lock, Queue
import os
import time
from processing import Pool

def cube(num):
    return num*num*num

if __name__ == "__main__":

    numbers = range(10)
    pool = Pool()

    # map, apply, join, close
    res = pool.map(cube, numbers)
    
    # executes 1 process with this arg
    pool.apply(cube, numbers[0])
    pool.close()
    pool.join()

    print(res)
    




##### QUEUE

# def square(numbers, queue):
#     for i in numbers:
#         queue.put(i*i)

# def make_negative(numbers, queue):
#     for i in numbers:
#         queue.put(-i)

# if __name__ == "__main__":
#     numbers = range(1,6)
#     q = Queue()

#     p1 = Process(target=square, args=(numbers, q))
#     p2 = Process(target=make_negative, args=(numbers, q))

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     while not q.empty():
#         print(q.get())


### ARR

# def add_100(arr, lock):
#         for i in range(100):
#             time.sleep(0.01)
#             for i in range(len(arr)):
#                 with lock: 
#                     arr[i] += 1



# if __name__ == "__main__":

#     lock = Lock()
    
#     shared_array = Array('d', [0.0, 100.0, 200,0])
#     print('Number af beginning is', shared_array[:])

#     p1 = Process(target=add_100, args=(shared_array, lock))
#     p2 = Process(target=add_100, args=(shared_array, lock))

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     print('number at end is ', shared_number.value)