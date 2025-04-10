INF = float('inf')

def floyd_warshall_with_paths_and_cycle_check(graph):
    n = len(graph)
    dist = [row[:] for row in graph]
    next_node = [[None] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] != INF:
                next_node[i][j] = j

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    for i in range(n):
        if dist[i][i] < 0:
            print(f"Negative Cicle from {i}")
            return dist, next_node, True

    return dist, next_node, False


def reconstruct_path(i, j, next_node):
    if next_node[i][j] is None:
        return []

    path = [i]
    while i != j:
        i = next_node[i][j]
        path.append(i)

    return path


graph = [
    [0,     1,    INF],
    [INF,   0,   1],
    [2,   INF,   0]
]

dist, next_node, has_negative_cycle = floyd_warshall_with_paths_and_cycle_check(graph)

if not has_negative_cycle:
    print("There are no negative cycles ։")
    print("Adj matrix՝")
    for row in dist:
        print(row)

    # path example 0 → 2
    path = reconstruct_path(0, 2, next_node)
    print("Shortest path from  0 to  2՝", path)

else:
    print("There are negative cycle։")