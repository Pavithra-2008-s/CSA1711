from collections import deque

M = int(input("Enter missionaries: "))
C = int(input("Enter cannibals: "))
B = int(input("Enter boat capacity: "))

start = (M, C, 1)
goal = (0, 0, 0)

def valid(m, c):
    if m < 0 or c < 0 or m > M or c > C:
        return False

    if m > 0 and m < c:
        return False

    if M - m > 0 and M - m < C - c:
        return False

    return True


queue = deque()
queue.append((start, []))
visited = set()

while queue:
    state, path = queue.popleft()

    if state in visited:
        continue

    visited.add(state)

    if state == goal:
        print("Solution:")
        for s in path + [state]:
            print(s)
        break

    m, c, boat = state

    for x in range(B + 1):
        for y in range(B + 1):

            if 1 <= x + y <= B:

                if boat == 1:
                    nm = m - x
                    nc = c - y
                    nb = 0
                else:
                    nm = m + x
                    nc = c + y
                    nb = 1

                new_state = (nm, nc, nb)

                if valid(nm, nc) and new_state not in visited:
                    queue.append((new_state, path + [state]))
else:
    print("No solution")
