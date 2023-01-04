from collections import defaultdict
import heapq
import string
string_dict = {key: val for key, val in enumerate(string.ascii_uppercase)}


def dijkstra_all_paths(graph: dict[dict[int, int]], source: int):
    prev_of = [None for _ in range(len(graph))]
    distUsed = [float('inf') for _ in range(len(graph))]
    distUsed[source] = 0

    visited = set()
    queue = list()
    heapq.heappush(queue, (0, source))

    while queue:
        used_dist, standing_node = heapq.heappop(queue)
        visited.add(standing_node)
    
        #Look at neightbor, to see if neighbor node propose a shorter path
        for neighbor_node, dist in graph[standing_node].items():
            #If already visited, we skip.
            if neighbor_node in visited:
                continue

            #Check if this standing node is a better path for a neighbor node
            new_dist = used_dist + dist 
            old_dist = distUsed[neighbor_node]

            if new_dist < old_dist: # Walking through standing node is shorter
                distUsed[neighbor_node] = new_dist      # Update new shorter distance 
                prev_of[neighbor_node] = standing_node  # Update previous node
            heapq.heappush(queue, (distUsed[neighbor_node], neighbor_node))

    #Print distance used to travel to nodes
    for node_idx, dist in enumerate(distUsed):
        print(string_dict[node_idx],'->', dist)

if __name__ == '__main__':
    edges = [
        (0,1,2),
        (0,2,1),
        (0,3,4),
        (1,2,5),
        (1,5,2),
        (1,4,10),
        (2,0,9),
        (2,4,11),
        (3,2,2),
        (4,3,7),
        (4,6,1),
        (5,7,3),
        (6,4,3),
        (6,5,2),
        (7,6,1),
    ]
    adj_dict = defaultdict(dict)
    for a, b, w in edges:
        adj_dict[a].update({b: w})

    dijkstra_all_paths(adj_dict, 2)


