from collections import deque, defaultdict

def build_broadcast_tree(graph, source):
    visited = set()
    tree_edges = []
    queue = deque([source])
    visited.add(source)
    while queue:
        node = queue.popleft()
        for neighbour in graph[node]:
            if neighbour not in visited :
                visited.add(neighbour)
                tree_edges.append((node, neighbour))
                queue.append(neighbour)
    return tree_edges
def main():
    graph = defaultdict(list)
    n = int(input("Enter the number of nodes: "))
    e = int(input("Enter number of edges: "))
    for i in range(e):
        u, v = input().split()
        graph[u].append(v)
        graph[v].append(u)
    source = input("Enter source node: ")
    tree = build_broadcast_tree(graph, source)
    print("Broadcast Tree Edges: ")
    for u, v in tree:
        print(f"{u} --> {v}")
if __name__ == "__main__":
    main()