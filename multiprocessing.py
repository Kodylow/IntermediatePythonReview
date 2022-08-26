# Process: a program in execution (e.g. the Python interpreter itself)

from multiprocessing import Process
import os
import time

def square_numbers():
    for i in range(100):
        i*i
        time.sleep(0.1)

processes = []
num_processes = os.cpu_count()

# create processes
for i in range(num_processes):
    p = Process(target=square_numbers)
    processes.append(p)

# start
for p in processes:
    p.start()

# join
for p in process:
    p.join()

print('end_main')