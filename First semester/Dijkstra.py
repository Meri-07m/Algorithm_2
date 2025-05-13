def dijkstra(graph, n, start):
    vis = [False] * n
    dist = [float('inf')] * n
    dist[start] = 0

    pq = [(start, 0)]
    print(pq)
    for _ in range(n):
        min_index = -1
        min_value = float('inf')

        for i in range(n):
            if not vis[i] and dist[i] < min_value:
                min_value = dist[i]
                min_index = i

        if min_index == -1:
            break

        vis[min_index] = True

        for to, cost in graph[min_index]:
            if not vis[to] and dist[min_index] + cost < dist[to]:
                dist[to] = dist[min_index] + cost

    return dist

graph = {
    0: [(1, 7), (2, 9), (5, 14)],
    1: [(3, 10), (2, 15)],
    2: [(3, 11), (5, 2)],
    3: [(4, 6)],
    4: [(5, 9)],
    5: []
}
n = 6
start = 0

print(dijkstra(graph, n, start))