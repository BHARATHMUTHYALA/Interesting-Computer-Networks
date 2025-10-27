from collections import deque
def broadcast(graph, start_node, message):
    visited = set() 
    queue = deque([start_node])
    
    print(f" Broadcasting message: '{message}' from node: {start_node}")
    
    while queue:
        current = queue.popleft()
        
        if current not in visited:
            visited.add(current)
            print(f"Node {current} received the message")
            
            for neighbour in graph.get(current, []):
                if neighbour not in visited:
                    print(f"Node {current} sends message to Node {neighbour}")
                    queue.append(neighbour)
                    
network = {
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F'],
    'D':['B'],
    'E':['B','F'],
    'F':['C','E']
}

start = 'A'
message = "System update available!"
broadcast(network, start, message)