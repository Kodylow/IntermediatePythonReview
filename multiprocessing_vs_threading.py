# Process: a program in execution (e.g. the Python interpreter itself)

# Advantages
# - Takes advantage of multiple CPU cores
# - Separate memory space -> memory is not shared between processes
# - Great for CPU-bound processing
# - New process is stated independently from other processes
# - processes are interruptable/killable
# - one GIL for each process -> avoids GIL limitation

# Disadvantages
# - Heavyweight!
# - Starting a process is slower than starting a thread
# - More memory
# - IPC (inter-process comms) is more complicated



# Threads: an entity WITHIN a process that can be scheduled. A process can spawn multiple threads.

# Advantages
# - All threads within a process share the same memory.
# - Lightweight
# - Starting a thread is significantly faster than starting a process
# - Great for I/O bound tasks

# Disadvantages
# - Threading limited by GIL: Only one thread at a time
# - No effect for CPU-bound tasks
# - Not interruptable/killable
# - Careful with race conditions

# GIL: Global interpreter lock
# - A lock that allows only one thread at a time to execute in Python
# - Needed in CPython because memory management is not thread-safe
# - Avoid
#     - use multiprocessing
#     - use a different, free-threaded Python impl (Jython, IronPython)
#     - use Python as a wrapper for third-party libraries (C/C++) -> numpy, scipy