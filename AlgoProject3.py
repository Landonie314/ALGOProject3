# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 11:56:17 2022

@author: Landon, Alvin, Aidan
"""
import collections

visited = set()
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


def dfs(visited, graph, node):  # function for dfs
    if node not in visited:
        print("'"+node + "', ", end="")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

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
print("1a")
print("BFS start at A")
print(v)
# Start at D, BFS
v = bfs(g, 'D')
print("BFS start at D")
print(v)
# Start at A, DFS
print("DFS start at A")
print("{", end="")
v = dfs(visited, g, 'A')
print("}")
# Start at D, DFS
visited = set()
print("DFS start at D")
print("{", end="")
d = dfs(visited, g, 'D')
print("}")

# 1b
# BFS path from A to G
print("\n1b")
v = list(bfs_path(g, 'A', 'G'))
print("BFS path from A to G")
print(v)
# DFS path from A to G
v = list(dfs_path(g, 'A', 'G'))
print("DFS path from A to G")
print(v)

# 1c
# BFS path from A to B
print("\n1c")
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


class DijkstraGraph:
    def __init__(self):
        self.nodes = set()
        self.edges = collections.defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance


def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distance[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path


graph = DijkstraGraph()

graph.nodes = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'}

graph.edges = {'A': ['B', 'C', 'D'], 'B': ['A', 'C', 'F', 'H'],
               'C': ['A', 'B', 'D', 'E', 'F'], 'D': ['A', 'C', 'E', 'I'],
               'E': ['C', 'D', 'F', 'G'], 'F': ['B', 'C', 'E', 'G', 'H'],
               'G': ['E', 'F', 'H', 'I'], 'H': ['B', 'F', 'G', 'I'],
               'I': ['D', 'G', 'H']}

graph.distance = {('A', 'B'): 22, ('A', 'C'): 9, ('A', 'D'): 12,
                  ('B', 'A'): 22, ('B', 'C'): 35, ('B', 'F'): 36, ('B', 'H'): 34,
                  ('C', 'A'): 9,  ('C', 'B'): 35, ('C', 'D'): 4, ('C', 'E'): 65, ('C', 'F'): 42,
                  ('D', 'A'): 12, ('D', 'C'): 4, ('D', 'E'): 33, ('D', 'I'): 30,
                  ('E', 'C'): 65, ('E', 'D'): 33, ('E', 'F'): 18, ('E', 'G'): 23,
                  ('F', 'B'): 36, ('F', 'C'): 42, ('F', 'E'): 18, ('F', 'G'): 39, ('F', 'H'): 24,
                  ('G', 'E'): 23, ('G', 'F'): 39, ('G', 'H'): 25, ('G', 'I'): 21,
                  ('H', 'B'): 34, ('H', 'F'): 24, ('H', 'G'): 25, ('H', 'I'): 19,
                  ('I', 'D'): 30, ('I', 'G'): 21, ('I', 'H'): 19,
                  }

# 3a
v, path = dijkstra(graph, 'A')
print("\n3a")
print('Visited: ', v)
print('Path :', path)

# 3b
