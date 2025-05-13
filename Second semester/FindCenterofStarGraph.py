from collections import Counter

def findCenter(edges):
    if len(edges) < 2:
        return "Error"

    node_count = Counter()
    for edge in edges:
        node_count[edge[0]] += 1
        node_count[edge[1]] += 1

    for node, count in node_count.items():
        if count == len(edges):
            return node

    return "The graph is not a star graph"

edges1 = [[1, 2], [2, 3], [4, 2]]
edges2 = [[1, 2], [6, 5], [1, 2], [2, 4]]
edges3 = [[1, 2], [2, 3]]
edges4 = [[1, 2], [2, 3], [4, 2], [2, 5], [2, 6]]
edges5 = [[1, 2], [3, 4]]
edges6 = [[1, 2], [2, 3]]

print(findCenter(edges1))
print(findCenter(edges2))
print(findCenter(edges3))
print(findCenter(edges4))
print(findCenter(edges5))
print(findCenter(edges6))