import heapq

def (graph, start, end):
    d, p = {start: 0}, {}
    q = [(0, start)]
    while q:
        dist, node = heapq.heappop(q)
        if node == end: break
        if dist > d[node]: continue
        for neighbor, weight in graph[node].items():
            new_dist = dist + weight
            if new_dist < d.get(neighbor, float('inf')):
                d[neighbor], p[neighbor] = new_dist, node
                heapq.heappush(q, (new_dist, neighbor))
    path, node = [], end
    while node:
        path.insert(0, node)
        node = p.get(node)
    return path

def get_graph_from_user():
    graph = {}
    while True:
        node = input("Enter a node (or 'q' to quit): ")
        if node == 'q':
            break
        connections = {}
        while True:
            neighbor = input(f"Enter a neighbor for {node} (or 'q' to finish): ")
            if neighbor == 'q':
                break
            weight = int(input(f"Enter the weight between {node} and {neighbor}: "))
            connections[neighbor] = weight
        graph[node] = connections
    return graph

graph = get_graph_from_user()
start = input("Enter the start node: ")
end = input("Enter the end node: ")

route = dijkstra(graph, start, end)
print("Optimal Route:", route)
