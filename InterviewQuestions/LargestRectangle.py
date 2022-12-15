# Given an array *heights* that contains the height of each bar in the histogram, return the area of the largest rectangle in the histogram.
# Each bar has a width of 1.

# Brute Force: try expanding left and right from each bar
# O(n) Time Complexity
# O(1) Space Complexity
def largest_rectangle_brute_force(heights):
    max_area = 0
    for i in range(len(heights)):
        left = i
        while left-1 >= 0 and heights[left-1] >= heights[i]:
            left -= 1
        right = i
        while right+1 < len(heights) and heights[right+1] >= heights[i]:
            right += 1
        max_area = max(max_area, heights[i]*(right-left+1))
    return max_area

# Divide and Conquer Solution: biggest rectangle cannot pass through the smallest height (unless the biggest is just the smallest height one). Divide left and right then recurse.
def rec(heights, low, high):
    if low > high:
        return 0
    elif low == high:
        return heights[low]
    else:
        minh = min(heights[low:high+1])
        pos_min = heights.index(minh, low, high+1)
        from_left = rec(heights, low, pos_min-1)
        from_right = rec(heights, pos_min+1, high)
        return max(from_left, from_right, minh*(high-low+1))

# O(nlogn) using a segment tree to optimize finding min
def largest_rectangle(heights):
    return rec(heights, 0, len(heights)-1)

# Optimization: Pass from left, pass from right, find max area comparing passes
def largest_rectangle_three_passes(heights):
    # set left and rights at negative 1 so always max_area within heights
    heights = [-1]+heights+[-1]

    # First pass from left
    from_left = [0]*len(heights)
    stack = [0]
    for i in range(1, len(heights)-1):
        while heights[stack[-1]] >= heights[i]:
            stack.pop()
        from_left[i] = stack[-1]
        stack.append(i)

    # Second pass from right
    from_right = [0]*len(heights)
    stack = [len(heights-1)]
    for i in range(1, len(heights)-1)[::-1]:
        while heights[stack[-1]] >= heights[i]:
            stack.pop()
        from_right[i] = stack[-1]
        stack.append(i)
    # Third pass
    max_area = 0
    for i in range(1, len(heights)-1):
        max_area = max(max_area, heights[i]*(from_right[i]-from_left[i]-1))
    return max_area

# Single Pass Solution
def largest_rectangle_single_pass(heights):
    heights = [-1]+heights+[-1]
    max_area = 0
    stack=[(0,-1)]
    for i in range(1, len(heights)):
        start = i
        while stack[-1][1] > heights[i]:
            top_index, top_height = stack.pop()
            max_area = max(max_area, top_height*(i-top_index))
            start = top_index
        stack.append((start, heights[i]))
    return max_area