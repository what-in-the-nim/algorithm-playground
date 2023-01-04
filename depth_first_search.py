from collections import defaultdict, deque
from typing import Tuple

def dfs_connectivity_recur(adj_dict: dict[int, list[int]], source: int, destination: int, visited: set = None):
    if source == destination:
        return True

    if visited is None:
        visited = set()
    visited.add(source)

    for adj_node in adj_dict[source]:
        if adj_node in visited:
            continue
        
        if dfs_connectivity_recur(adj_dict, adj_node, destination, visited):
            return True

def dfs_connectivity(adj_dict: dict[int, list[int]], source: int, destination: int):
    stack = [source]
    visited = {source}

    while stack:
        current_node = stack.pop()
        for adj_node in adj_dict[current_node]:

            if adj_node == destination:
                return True
            if adj_node in visited:
                continue
 
            visited.add(adj_node)
            stack.append(adj_node)
        
    return False

def dfs_shortest_path_recur(
    adj_dict: dict[int, list[int]], 
    source: int, 
    destination: int, 
    visited: set = None,
    path: list[int] = None):

    if visited is None:
        visited = set()
    visited.add(source)

    if source == destination:
        return path

    for adj_node in adj_dict[source]:
        if adj_node in visited:
            continue
        result = dfs_shortest_path_recur(adj_dict, adj_node, destination, visited)
        if result is not None:
            print(source, result)
            return [source] + result


def dfs_shortest_path(adj_dict: dict[int, list[int]], source: int, destination: int):
    # Init variables
    prev = {source: None}
    visited = {source}
    visit_queue = deque([source])

    # Start deque node and iterate
    while visit_queue:
        current_node = visit_queue.pop()
        adj_nodes = adj_dict[current_node]

        # Visit nodes
        for adj_node in adj_nodes:
            if adj_node in visited:
                continue

            prev[adj_node] = current_node 
            if adj_node == destination:
                break
            visit_queue.append(adj_node)
            visited.add(adj_node)

        if adj_node == destination:
            break

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
    (0, 11),
    (11, 12),
    (12, 13),
    (3, 4),
    (3, 5),
    (4, 7),
    (7, 8),
    (7, 9),
    (5, 10)
]

# Create two-way connection dict
adj_dict = defaultdict(list)
for start, stop in edges:
    adj_dict[start].append(stop)
    adj_dict[stop].append(start)

path = dfs_shortest_path_recur(adj_dict, 0 ,13)
print(path)