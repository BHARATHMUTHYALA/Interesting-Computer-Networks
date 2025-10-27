def bellman_ford(graph, V, E, src):
    dist =[ float('inf') ] * V
    dist[src] = 0 
    for i in range(V-1):
        for u, v , w in E:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    for u, v, w in E:
        if dist[u] + w < dist[v]:
            print('Negative cycle detected')
            return
    print("Shortest distances from node", src)
    for i in range(V):
        print(f"Node {i} -> Distance: {dist[i]}")

edges = [
    (0, 1, 4), (0, 2, 5),
    (1, 2, 3), (2, 3, 4)
]
bellman_ford(edges , 4, edges, 0)
