from sys import maxsize
from itertools import permutations

def tsp(graph, s):
    V = len(graph)
    vertex = [i for i in range(V) if i != s]

    min_cost = maxsize
    for perm in permutations(vertex):
        current_cost, k = 0, s
        selected_vertices = [s]

        for j in perm:
            current_cost += graph[k][j]
            k = j
            selected_vertices.append(k)

        current_cost += graph[k][s]
        selected_vertices.append(s)  
        min_cost = min(min_cost, current_cost)

        if current_cost == min_cost:
            print("Selected Vertices:", selected_vertices)

    return min_cost

V = int(input("Enter the number of vertices: "))
graph = [[0] * V for _ in range(V)]

for i in range(V):
    graph[i] = list(map(int, input(f"Enter distances from vertex {i} to all vertices (space-separated): ").split()))

s = 0
print("Optimal Cost:", tsp(graph, s))
