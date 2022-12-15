# Given an integer `n` representing the number of courses (courses are labelled from 0 to n-1), and an array `prerequisites` where `prerequisites[i] = [a,b]` means that you need to take the course b before taking the course a, determine it it's possible to finish all the courses.__doc__

# Prove there isn't a cycle!
# Build a directed graph, check for a cycle
# Depth first search doesn't work, gotta do a topological sort. Topo sort is impossible if there's a cycle, so if we find one then topo sort is impossible and course ordering is in turn impossible

# Topological Sort
# Path Stack and Order Stack, add to path stack, then push to order stack on backtrack

def dfs(graph, vertex, path_stack, order_stack, visited):
    path_stack.add(vertex)
    for neighbor in graph[vertex]:
        # Cycle
        if neighbor in path:
            return False
        if neighbor not in visited:
            visited.add(neighbor)
            # Cycle
            if not dfs(graph, neighbor, path_stack, order_stack, visited):
                return False
    path_stack.remove(vertex)
    order_stack.append(vertex)
    return True

def topo_sort(graph):
    visited = set()
    path_stack = []
    order_stack = []
    for vertex in graph:
        if vertex not in visited:
            visited.add(vertex)
            dfs(graph, vertex, path_
               stack, order_stack, visited)
    return order[::-1]

# O(|V|+|E|) = O(n + m) Time Complexity for depth first search
# O(4n+m) = O(n+m) Space Complexity
def course_schedule(n, prerequisites):
    graph = [[] for i in range(n)]
    for p in prerequisites:
        graph[p[1].append(p[0])]
    visited = set()
    path_set = set()
    order_stack = []
    for course in range(n):
        if course not in visited:
            visited.add(course)
            if not dfs(graph, course, path_set, order_stack):
                return False
    return True


# Breadth First Search
# Same space and time complexities
from collections import deque
def course_schedule(n, prerequisites):
    graph = [[] for i in range(n)]
    indegree = [0 for i in range(n)]
    for p in prerequisites:
        graph[p[1].append(p[0])]
        indegree[p[0]] += 1
    order_stack = []
    queue = deque([i for i in range(n) if indegree[i] == 0])
    while queue:
        vertex = queue.popLeft()
        order_stack.append(vertex)
        for neighbor in graph[vertex]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return len(order_stack) == n      