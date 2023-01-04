from collections import defaultdict, deque
from typing import Tuple

def bfs_shortest_path(edges: list[Tuple[int, int]], source: int, destination: int):
    # Create two-way connection dict
    adj_dict = defaultdict(list)
    for start, stop in edges:
        adj_dict[start].append(stop)
        adj_dict[stop].append(start)

    # Init variables
    search = [source]
    prev = {source: None}
    visited = {source}
    queue = deque()
    queue.append(source)

    # Start deque node and iterate
    while len(queue) > 0:
        current_node = queue.popleft()
        adj_nodes = adj_dict[current_node]

        # Visit nodes
        for adj_node in adj_nodes:
            if adj_node not in visited:
                print(adj_node)
                queue.append(adj_node)
                visited.add(adj_node)
                search.append(adj_node)
                prev[adj_node] = current_node 

    # Backtrack path
    search_node = prev[destination]
    path = [destination]
    while True:
        if search_node == None:
            return None
        path.append(search_node)
        if search_node == source:
            break
        search_node = prev[search_node]

    path.reverse()
    return path

edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (0, 3),
    (3, 4),
    (3, 5),
    (4, 7),
    (7, 8),
    (7, 9),
    (5, 10)
]

path = bfs_shortest_path(edges, 0 ,10)
print(path)