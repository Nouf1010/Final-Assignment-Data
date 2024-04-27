# Importing the heapq module for heap queue operations
import heapq

# Implementation of Dijkstra's algorithm to find the shortest distance between two points
def dijkstra(graph, start, end):
    # Initialize distances dictionary with all nodes set to infinity (Because we don't know the distance yet)
    distances = {node: float('inf') for node in graph}
    # Setting the distance of the starting node to 0
    distances[start] = 0
    # Initializing the priority queue with the start node and its distance (0)
    queue = [(0, start)]

    # Loop until priority queue is empty
    while queue:
        # Pop node with the smallest distance from the priority queue
        current_distance, current_node = heapq.heappop(queue)

        # If the destination node is reached, return distance to it
        if current_node == end:
            return distances[end]

        # If the current distance is greater than recorded distance, skip
        if current_distance > distances[current_node]:
            continue

        # Iterating over the neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            # Calculating the new distance to neighbor
            distance = current_distance + weight
            # If new distance is smaller, update distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    # If no path is found, return infinity
    return float('inf')

# Function to create graph from list of roads
def create_graph(roads):
    # Initializing an empty graph
    graph = {}
    # Iterating over the list of roads
    for source, destination, distance in roads:
        # If source road not in the graph, add it
        if source not in graph:
            graph[source] = {}
        # If destination road not in the graph, add it
        if destination not in graph:
            graph[destination] = {}
        # Adding edges between source and destination with given distance
        graph[source][destination] = distance
        graph[destination][source] = distance

    return graph

# List of roads with distances between them
roads = [('A', 'B', 5), ('A', 'C', 7), ('B', 'D', 4), ('C', 'E', 6),
         ('D', 'F', 3), ('E', 'G', 4), ('F', 'H', 5), ('G', 'I', 3),
         ('H', 'J', 6), ('I', 'J', 5)]

# Creating a graph from the list of roads
graph = create_graph(roads)

# Inputs points (we can change this to any starting and ending point)
start_point = 'A'
end_point = 'Z'

# Finding the shortest distance between start and end points using Dijkstra's algorithm
shortest_distance = dijkstra(graph, start_point, end_point)

# Checking if it is possible to reach between points
if shortest_distance != float('inf'):
    print(" Shortest distance from", start_point, " to ", end_point, " : ", shortest_distance)
else:
    print(" No path found from", start_point, " to ", end_point)
