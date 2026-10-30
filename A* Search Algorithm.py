import heapq

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def misplaced(state):
    count = 0

    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1

    return count

def manhattan(state):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(goal.index(state[i]), 3)

            distance += abs(x1 - x2) + abs(y1 - y2)

    return distance

def get_moves(state):
    moves = []
    zero = state.index(0)
    row, col = divmod(zero, 3)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
        r, c = row + dr, col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            new_pos = r * 3 + c
            new_state = list(state)

            new_state[zero], new_state[new_pos] = (
                new_state[new_pos], new_state[zero]
            )

            moves.append(tuple(new_state))

    return moves

def astar(start, heuristic):
    queue = []
    heapq.heappush(queue, (heuristic(start), 0, start, [start]))

    visited = set()
    nodes = 0

    while queue:
        f, cost, state, path = heapq.heappop(queue)

        if state in visited:
            continue

        visited.add(state)
        nodes += 1

        if state == goal:
            return path, cost, nodes

        for next_state in get_moves(state):
            if next_state not in visited:
                new_cost = cost + 1
                new_f = new_cost + heuristic(next_state)

                heapq.heappush(
                    queue,
                    (new_f, new_cost, next_state, path + [next_state])
                )

    return None, -1, nodes

def display(path):
    for state in path:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()

print("Using Misplaced Tiles Heuristic")
path, cost, nodes = astar(start, misplaced)
display(path)
print("Path Cost:", cost)
print("Nodes Expanded:", nodes)

print("\nUsing Manhattan Distance Heuristic")
path, cost, nodes = astar(start, manhattan)
display(path)
print("Path Cost:", cost)
print("Nodes Expanded:", nodes)
