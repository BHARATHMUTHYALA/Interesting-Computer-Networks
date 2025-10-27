import heapq 
from collections import defaultdict

class BroadcastTree:
    def __init__(self, network):
        self.network = network

    def construct_tree(self, source):
        tree = defaultdict(dict)
        visited = set([source])
        edges = [(cost, source, neighbour)
        for neighbour , cost in self.network[source].items()]
        heapq.heapify(edges)

        while edges and len(visited) < len(self.network):
            cost, u, v = heapq.heappop(edges)
            if v not in visited:
                visited.add(v)
                tree[u][v] = cost
                for neighbour , c in self.network[v].items():
                    if neighbour not in visited:
                        heapq.heappush(edges, (c, v, neighbour))
        return dict(tree)
    
    def propogate(self,tree, source, message):
        delivery_log = []
        queue  = [(source, message)]
        while queue:
            node, msg = queue.pop(0)
            delivery_log.append(f"Node {node} received:'{msg}'")
            for neighbour in tree.get(node, {}): 
                queue.append((neighbour, msg))
        return delivery_log

    def dynamic_update(self, tree, failed_node):
        new_network = {}
        for node, neighbours in self.network.items():
            if node != failed_node:
                new_network[node] = {}
                for neighbour, cost in neighbours.items():
                    if neighbour != failed_node:
                        new_network[node][neighbour] = cost 
        return BroadcastTree(new_network)
if __name__ == "__main__":
    print("=============== WEEK 7 BROADCAST TREE ===============")
    network = {
        'A' : {'B': 2, 'C': 3},
        'B' : {'A': 2, 'C': 1, 'D': 1},
        'C' : {'A': 3, 'B': 1, 'D': 4},
        'D' : {'B': 1, 'C': 4}
    }
    bt = BroadcastTree(network)

    tree = bt.construct_tree('A')
    print("\n7.2 Broadcast tree structure: ")
    for node , neighbours in tree.items():
        print(f"{node} --> {neighbours}")

    print("\n7.3 Message propagation: ")
    for log in bt.propogate(tree, 'A' , "Network Update"):
        print(log)


    print("\n7.4 Dynamic Update (Node B failed): ")
    new_bt = bt.dynamic_update(tree, 'B')
    new_tree = new_bt.construct_tree('A')
    for node , neighbours in new_tree.items():
        print(f"{node} --> {neighbours}")
