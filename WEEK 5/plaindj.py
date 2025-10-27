import heapq
def dijsktra(graph, start):
    dist = {n: float('inf') for n in graph}
    prev = {n: None for n in graph} 
    pq = [(0, start)]
    visited = set()
    dist[start] = 0
    while pq:
        d, node = heapq.heappop(pq)
        if node in visited: continue
        visited.add(node)
        for neighbour ,  weight in graph[node].items():
            if(new_d := d +weight) < dist[neighbour]:
                dist[neighbour] = new_d
                prev[neighbour] = node
                heapq.heappush(pq, (new_d, neighbour))
    return dist, prev

def construct_path(prev, start, end):
    path, current = [], end
    while current is not None:
        path.append(current)
        current = prev[current]
    path.reverse()
    return  " --> ".join(path) if path[0] ==start else "No path found"

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

shortest_distances, previous_nodes =dijsktra(graph, 'A')

for node, distance in shortest_distances.items():
    print(f"Distance to {node}: {distance}")

print(f"Shortest path from A to D: {construct_path(previous_nodes, 'A', 'D')}")