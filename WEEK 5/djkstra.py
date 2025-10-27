import heapq 
def dijsktra(graph, start):
    pq , dist = [(0, start)], {node: float('inf') for node in graph}
    dist[start] = 0
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue
        for neighbour, weight in graph[node].items():
            if (new_d :=d + weight) < dist[neighbour]:
                dist[neighbour] = new_d
                heapq.heappush(pq, (new_d, neighbour))
    return dist

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
print(dijsktra(graph, 'A'))