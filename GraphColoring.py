from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, subject1, subject2):
        self.graph[subject1].append(subject2)
        self.graph[subject2].append(subject1)

    def get_minimum_time_slots(self):
        max_degree = 0
        for subject, neighbors in self.graph.items():
            max_degree = max(max_degree, len(neighbors))
        return max_degree
      
subjects = [input(f"Enter subject {i + 1}: ").lower() for i in range(int(input("Enter the number of subjects: ")))]
students = {subject: [input(f"Enter student {j + 1} for {subject}: ") for j in range(int(input(f"Enter the number of students for {subject}: ")))] for subject in subjects}
num_edges = int(input("Enter the number of edges: "))
graph = Graph()

for _ in range(num_edges):
    subject1, subject2 = input("Enter edge (subject1 subject2): ").split()
    graph.add_edge(subject1, subject2)
  
minimum_time_slots = graph.get_minimum_time_slots()
print(f"\nMinimum time slots needed: {minimum_time_slots}")

