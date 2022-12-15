# Given a sorted array of integers `arr` and an integer `target`, find the index of the first and last position of target in arr.
# If target can't be found in arr, return [-1, -1]

def first_and_last_pos(arr, target):
    # One line with index
    # return [arr.index(target), (len(arr) - arr[::-1].index(target)) - 1]
    

    # Multiple lines
    # O(n) time complexity, O(1) space complexity
    # sorted so can traverse start and end
    for i in range(len(arr)):
        if arr[i] == target:
            start = i
            while i+1 < len(arr) and arr[i+1] == target:
                i += 1
            return [start, i]
    return [-1, -1]

# Binary Search solution, orks because array is sorted
# O(logn) Time Complexity
# O(1) Space Complexity
def find_start(arr, target):
    if arr[0] == target:
        return 0
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target and arr[mid-1] < target:
            return mid
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return -1

def find_end(arr, target):
    if arr[-1] == target:
        return len(arr)-1
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target and arr[mid+1] > target:
            return mid
        elif arr[mid] > target:
            left = mid-1
        else:
            right = mid+1
    return -1

def first_and_last_bin_search(arr, target):
    if len(arr) == 0 or arr[0] > target or arr[-1] < target:
        return [-1,-1]
    start = find_start(arr, target)
    end = find_end(arr, target)
    return [start, end]