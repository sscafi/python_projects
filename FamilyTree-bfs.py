from collections import deque

# Function to perform breadth-first search and generate minimal spanning tree
def bfs(graph, start_vertex):
    # Initialize the queue with the start vertex
    queue = deque([start_vertex])

    # Initialize visited set to keep track of visited vertices
    visited = set([start_vertex])

    # Initialize minimal spanning tree
    mst = {}

    # Iterate until the queue is empty
    while queue:
        current_vertex = queue.popleft()
        mst[current_vertex] = []

        # Explore neighbors of the current vertex
        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                # Add the neighbor to the minimal spanning tree
                mst[current_vertex].append(neighbor)
                visited.add(neighbor)
                queue.append(neighbor)

    return mst

# Function to calculate the shortest path from start_vertex to each other vertex
def shortest_path(graph, start_vertex):
    # Perform breadth-first search to generate the minimal spanning tree
    mst = bfs(graph, start_vertex)

    # Initialize dictionary to store the shortest path distances
    shortest_distances = {}

    # Initialize queue with the start vertex and distance 0
    queue = deque([(start_vertex, 0)])

    # Iterate until the queue is empty
    while queue:
        current_vertex, distance = queue.popleft()

        # Update shortest distance if it's not already set or a shorter distance is found
        if current_vertex not in shortest_distances or distance < shortest_distances[current_vertex]:
            shortest_distances[current_vertex] = distance

        # Explore neighbors of the current vertex
        for neighbor in mst[current_vertex]:
            queue.append((neighbor, distance + 1))

    return shortest_distances

# Test the algorithm with sample data

# Define the graph representing parent-child relationships between people
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': [],
    'G': ['I', 'J'],
    'H': [],
    'I': [],
    'J': [],
}

# Starting vertex
start_vertex = 'A'

# Calculate the shortest path from start_vertex to each other vertex
shortest_distances = shortest_path(graph, start_vertex)

# Print the shortest path distances
print("Shortest Path Distances:")
for vertex, distance in shortest_distances.items():
    print(f"{vertex}: {distance}")
