# Given a sorted array of integers `arr` and an integer `target`, find the index of the first and last position of target in arr.
# If target can't be found in arr, return [-1, -1]

def first_and_last_pos(arr, target):
    # One line with index
    # return [arr.index(target), (len(arr) - arr[::-1].index(target)) - 1]

    # Multiple lines
    # sorted so can traverse start and end
    for i in range(len(arr)):
        if arr[i] == target:
            start = i
            while i+1 < len(arr) and arr[i+1] == target:
                i += 1
            return [start, i]
    return [-1, -1]
    