# Importing the heapq module for heap queue operations
import heapq

# Implementation of Dijkstra's algorithm
def dijkstra(graph, start, end):
    # Initializing distances dictionary with all nodes set to infinity (Because we don't know the distance yet)
    distances = {node: float('inf') for node in graph}
    # Setting distance of starting node to 0
    distances[start] = 0

    # Initializing a priority queue with start node and its distance (0)
    queue = [(0, start)]
    # Storing shortest paths from start node to other nodes
    shortest_paths = {start: [start]}

    # Loop until priority queue is empty
    while queue:
        # Pop the node with the smallest distance from the priority queue
        current_distance, current_node = heapq.heappop(queue)

        # If the destination node is reached, return shortest path and distance
        if current_node == end:
            return shortest_paths[current_node], distances[current_node]

        # If current distance is greater than the recorded distance, skip (so we don't add it)
        if current_distance > distances[current_node]:
            continue

        # Iterating over the neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            # Calculating new distance to neighbor
            distance = current_distance + weight
            # If new distance is smaller, update distance and path
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
                shortest_paths[neighbor] = shortest_paths[current_node] + [neighbor]

    # If no path is found, return None
    return None, None

# Function to create a graph from the list of houses
def create_graph(houses):
    # Initializing an empty graph
    graph = {}

    # Iterating over the list of houses
    for source, destination, distance in houses:
        # If source house not in graph, add it
        if source not in graph:
            graph[source] = {}
        # If the destination house not in the graph, add it
        if destination not in graph:
            graph[destination] = {}
        # Add edges between source and destination with the given distance
        graph[source][destination] = distance
        graph[destination][source] = distance

    return graph

# List of houses with distances between them
houses = [('H1', 'H2', 20), ('H1', 'H3', 40), ('H2', 'H4', 10), ('H3', 'H5', 15),
          ('H4', 'H6', 25), ('H5', 'H7', 30), ('H6', 'H8', 35), ('H7', 'H9', 40),
          ('H8', 'H10', 20), ('H9', 'H11', 18), ('H10', 'H12', 22), ('H11', 'H13', 27),
          ('H12', 'H14', 32), ('H13', 'H15', 28), ('H14', 'H16', 24), ('H15', 'H17', 19),
          ('H16', 'H18', 15), ('H17', 'H19', 10), ('H18', 'H20', 12), ('H19', 'H21', 8),
          ('H20', 'H22', 6), ('H21', 'H23', 4), ('H22', 'H24', 5), ('H23', 'H25', 7)]

# Creating a graph from the list of houses
graph = create_graph(houses)

#----------------------------------------------------
# Test case 1
start_node = 'H14'
end_node = 'H25'

# Finding the shortest path and distance from start to end node
shortest_path, distance = dijkstra(graph, start_node, end_node)

# Printing the result of test case 1
if shortest_path:
    print(" \nShortest path from ", start_node, "to", end_node, ":", shortest_path)
    print(" Distance:", distance)
else:
    print(" \nNo path found from", start_node, "to", end_node)

#----------------------------------------------------
# Test case 2
start_node = 'H4'
end_node = 'H19'

# Finding the shortest path and distance from start to end node
shortest_path, distance = dijkstra(graph, start_node, end_node)

# Printing the result of test case 2
if shortest_path:
    print(" \nShortest path from ", start_node, "to", end_node, ":", shortest_path)
    print(" Distance:", distance)
else:
    print(" \nNo path found from", start_node, "to", end_node)

#----------------------------------------------------
# Test case 3
start_node = 'H4'
end_node = 'H1'

# Finding the shortest path and distance from start to end node
shortest_path, distance = dijkstra(graph, start_node, end_node)

# Printing the result of test case 3
if shortest_path:
    print(" \nShortest path from ", start_node, "to", end_node, ":", shortest_path)
    print(" Distance:", distance)
else:
    print(" \nNo path found from", start_node, "to", end_node)

#----------------------------------------------------
# Test case 4
start_node = 'H4'
end_node = 'H50'

# Finding the shortest path and distance from start to end node
shortest_path, distance = dijkstra(graph, start_node, end_node)

# Printing result of test case 4
if shortest_path:
    print(" \nShortest path from ", start_node, "to", end_node, ":", shortest_path)
    print(" Distance:", distance)
else:
    print(" \nNo path found from", start_node, "to", end_node)
