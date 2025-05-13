graph = [
    ('A', 'B', 3),
    ('A', 'C', 6),
    ('B', 'D', 1),
    ('D', 'C', 1),
    ('D', 'E', 3),
    ('E', 'F', 4),
    ('F', 'C', 8)]


def bellman_ford(graph, vertices, start):
    distance = {v: float('inf') for v in vertices}
    distance[start] = 0

    for _ in range(len(vertices) - 1):
        for u, v, w in graph:
            if distance[u] + w < distance[v]:
               distance[v] = distance[u] + w

    for u, v, w in graph:
        if distance[u] + w < distance[v]:
            return "Negative cicle "

    return distance

vertices = {'A', 'B', 'C', 'D', 'E', 'F'}

start_node = 'A'
result = bellman_ford(graph, vertices, start_node)

print("Shortest distance from", start_node, ":",  result)