def floyd_warshall(graph):
    nodes = list(graph.keys())
    n = len(nodes)
    dist = {u:{v: float('inf') for v in nodes} for u in nodes}

    for u in nodes:
        dist[u][u] = 0
        for v in graph[u]:
            dist[u][v] = graph[u][v]

    for k in nodes:
        for i in nodes:
            for j in nodes:
                if(dist[i][j] > dist[i][k] + dist[k][j]):
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
distances = floyd_warshall(graph)
for u in distances:
    for  v in distances[u]:
        print(f"Shortest distance from {u} to {v}: {distances[u][v]}")