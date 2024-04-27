# Defining the road network as a dictionary
road_network = {
    # Intersection A with roads leading to B and C
    'A': {'B': {'id': 1, 'name': 'Sheikh Zayed Road', 'length': 5}, 'C': {'id': 2, 'name': 'Al Khail Road', 'length': 7}},
    # Intersection B with roads leading to A and D
    'B': {'A': {'id': 1, 'name': 'Sheikh Zayed Road', 'length': 5}, 'D': {'id': 3, 'name': 'Dubai Bypass Road', 'length': 4}},
    # Intersection C with roads leading to A and E
    'C': {'A': {'id': 2, 'name': 'Al Khail Road', 'length': 7}, 'E': {'id': 4, 'name': 'Emirates Road', 'length': 6}},
    # Intersection D with roads leading to B and F
    'D': {'B': {'id': 3, 'name': 'Dubai Bypass Road', 'length': 4}, 'F': {'id': 5, 'name': 'Jumeirah Beach Road', 'length': 3}},
    # Intersection E with roads leading to C and G
    'E': {'C': {'id': 4, 'name': 'Emirates Road', 'length': 6}, 'G': {'id': 6, 'name': 'SMBZ Road', 'length': 4}},
    # Intersection F with roads leading to D and H
    'F': {'D': {'id': 5, 'name': 'Jumeirah Beach Road', 'length': 3}, 'H': {'id': 7, 'name': 'Al Ain Road', 'length': 5}},
    # Intersection G with roads leading to E and I
    'G': {'E': {'id': 6, 'name': 'SMBZ Road', 'length': 4}, 'I': {'id': 8, 'name': 'Al Maktoum Airport Street', 'length': 3}},
    # Intersection H with roads leading to F and J
    'H': {'F': {'id': 7, 'name': 'Al Ain Road', 'length': 5}, 'J': {'id': 9, 'name': 'Dubai-Al Ain Road', 'length': 6}},
    # Intersection I with roads leading to G and J
    'I': {'G': {'id': 8, 'name': 'Al Maktoum Airport Street', 'length': 3}, 'J': {'id': 10, 'name': 'E611 Road', 'length': 5}},
    # Intersection J with roads leading to H and I
    'J': {'H': {'id': 9, 'name': 'Dubai-Al Ain Road', 'length': 6}, 'I': {'id': 10, 'name': 'E611 Road', 'length': 5}}
}

# Printing the road network
for intersection, roads in road_network.items():
    # Printing the intersection name
    print(f" Intersection: {intersection}")
    # Iterating over the roads connected to the intersection
    for destination, road_info in roads.items():
        # Printing information about each road (name, ID, length)
        print(f"  Road: {road_info['name']} (ID: {road_info['id']}) Length:  {road_info['length']} ")
