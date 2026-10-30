graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 2)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

def bfs(start, goal):
    queue = [[start]]
    visited = []

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.append(node)

            for neighbor, cost in graph[node]:
                queue.append(path + [neighbor])

    return None

def dfs(start, goal):
    stack = [[start]]
    visited = []

    while stack:
        path = stack.pop()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.append(node)

            for neighbor, cost in reversed(graph[node]):
                stack.append(path + [neighbor])

    return None

import heapq

def ucs(start, goal):
    queue = [(0, [start])]
    visited = set()

    while queue:
        cost, path = heapq.heappop(queue)
        node = path[-1]

        if node == goal:
            return path, cost

        if node not in visited:
            visited.add(node)

            for neighbor, weight in graph[node]:
                heapq.heappush(
                    queue,
                    (cost + weight, path + [neighbor])
                )

    return None, float('inf')

start = 'A'
goal = 'F'

print("BFS Path:", bfs(start, goal))
print("DFS Path:", dfs(start, goal))

path, cost = ucs(start, goal)

print("UCS Path:", path)
print("UCS Total Cost:", cost)
