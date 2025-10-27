def floyd_warshall_with_path(graph):
    nodes = list(graph.keys())

    distance = {i: {j: float('inf') for j in nodes} for i in nodes}
    next_node = {i : {j: None for j in nodes} for i in nodes}

    for u in nodes:
        distance[u][u] = 0
        for v in graph[u]:
            distance[u][v] = graph[u][v]
            next_node[u][v] = v
    for k in nodes:
        for i in nodes:
            for j in nodes:
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    next_node[i][j] = next_node[i][k]
    return distance, next_node

def reconstruct_path(start, end, next_node):
    if next_node[start][end] is None:
        return []
    path = [start]
    while start != end:
        start = next_node[start][end]
        path.append(start)
    return path

graph = {
    'A' : {'B' : 2, 'C' : 6}, 
    'B' : {'A' : 2, 'C' : 3},
    'C' : {'A' : 6, 'B' : 3},
}
distances , next_node = floyd_warshall_with_path(graph)
start_node, end_node = 'A', 'C'
shortest_path = reconstruct_path(start_node, end_node, next_node)
print(f"Shortest path from {start_node} to {end_node} : {shortest_path}")