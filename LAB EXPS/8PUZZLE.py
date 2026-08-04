from collections import deque

# Goal State
goal_state = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)

# Find the position of the blank tile (0)
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate all possible moves
def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)

    # Up, Down, Left, Right
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]

            # Swap blank with adjacent tile
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]

            neighbors.append(tuple(tuple(row) for row in new_state))

    return neighbors

# Breadth First Search
def bfs(initial_state):
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()

        if current_state == goal_state:
            return path + [current_state]

        if current_state in visited:
            continue

        visited.add(current_state)

        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                queue.append((neighbor, path + [current_state]))

    return None

# Initial State
initial_state = (
    (5, 4, 0),
    (6, 1, 8),
    (7, 3, 2)
)

solution = bfs(initial_state)

if solution:
    print("Solution Found!\n")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No Solution Found!")
