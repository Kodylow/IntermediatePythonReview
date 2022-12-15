# Given an array of integers and an integer k, find the kth largest element
import heapq

def kth_largest(arr, k):
    # Sorting Solution
    # O(nlogn) Time Complexity
    # Space Complexity depends on sorting function
    # return sorted(arr)[len(arr) - k]

# Priority Queue Solution, implemented with a heap
# O(n + klogn) Time Complexity
    # improvement if k much smaller than n
# O(n) Space Complexity
def kth_largest_heap(arr, k):
    arr = [-elem for elem in arr]
    heapq.heapify(arr)
    for i in range(k-1):
        heap.heappop(arr)
    return -heapq.heappop(arr)