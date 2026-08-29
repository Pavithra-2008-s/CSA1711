from collections import deque


n = int(input(
    "Enter number of vertices: "
))


graph = {}


for i in range(n):

    graph[i] = list(
        map(
            int,
            input(
                f"Enter neighbours of {i}: "
            ).split()
        )
    )


start = int(input(
    "Enter starting vertex: "
))


queue = deque([start])

visited = set([start])


print("BFS Traversal:")


while queue:

    node = queue.popleft()

    print(node, end=" ")


    for neighbour in graph[node]:

        if neighbour not in visited:

            visited.add(neighbour)

            queue.append(neighbour)
