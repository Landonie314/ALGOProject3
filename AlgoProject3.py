# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 11:56:17 2022

@author: Landon, Alvin, Aidan
"""

# graph 1
g = {
    'A': set(['B', 'E', 'F']),
    'B': set(['A', 'C', 'F']),
    'C': set(['B', 'D', 'G']),
    'D': set(['C', 'G']),
    'E': set(['A', 'F', 'I']),
    'F': set(['A', 'B', 'E', 'I']),
    'G': set(['C', 'D', 'J']),
    'H': set(['K', 'L']),
    'I': set(['E', 'F', 'J', 'M']),
    'J': set(['G', 'I']),
    'K': set(['H', 'L', 'O']),
    'L': set(['H', 'K', 'P']),
    'M': set(['I', 'N']),
    'N': set(['M']),
    'O': set(['K']),
    'P': set(['L'])
}

# BFS


def bfs(graph, start):
    visited, queue = set(), [start]
    p = []
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            p.append(vertex)
            queue.extend(graph[vertex] - visited)
    return p
# BFS paths


def bfs_path(graph, start, goal):
    if start == goal:
        return [start]
    visited = {start}
    queue = [(start, [])]
    while queue:
        current, path = queue.pop(0)
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor == goal:
                return path + [current, neighbor]
            if neighbor in visited:
                continue
            queue.append((neighbor, path + [current]))
            visited.add(neighbor)
    return None
# DFS


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited
# DFS paths


def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)
            for neighbor in graph[vertex]:
                stack.append((neighbor, path + [neighbor]))


# 1a
# Start at A, BFS
v = bfs(g, 'A')
print("BFS start at A")
print(v)
# Start at D, BFS
v = bfs(g, 'D')
print("BFS start at D")
print(v)

# DFS not working properly for me
# Start at A, DFS
#v = dfs(g, 'A')
#print("DFS start at A")
# print(v)
# Start at D, DFS
#v = dfs(g, 'D')
#print("DFS start at D")
# print(v)

# 1b
# BFS path from A to G
v = list(bfs_path(g, 'A', 'G'))
print("BFS path from A to G")
print(v)
# DFS path from A to G
v = list(dfs_path(g, 'A', 'G'))
print("DFS path from A to G")
print(v)

# 1c
# BFS path from A to B
v = list(bfs_path(g, 'A', 'B'))
print("BFS path from A to B")
print(v)
# DFS path from A to B
v = list(dfs_path(g, 'A', 'B'))
print("DFS path from A to B")
print(v)

# graph 2
g2 = {
    '1': set(['3']),
    '2': set(['1']),
    '3': set(['2', '5']),
    '4': set(['1', '2', '12']),
    '5': set(['6', '8']),
    '6': set(['7', '8', '10']),
    '7': set(['10']),
    '8': set(['9', '10']),
    '9': set(['5', '11']),
    '10': set(['9', '11']),
    '11': set(['12']),
    '12': set([]),
}

# graph 3
