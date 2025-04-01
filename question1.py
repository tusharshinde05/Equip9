from collections import deque

def find_shortest_path(n, edges, availability, start_provider, target_equipment):
    graph = {i: [] for i in range(1, n + 1)}
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    for node in graph:
        graph[node].sort(reverse=True)
    
    queue = deque([(start_provider, [start_provider])])
    visited = set([start_provider])

    possible_paths = []

    while queue:
        current, path = queue.popleft()

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                if target_equipment in availability.get(neighbor, []):
                    possible_paths.append(new_path)
                queue.append((neighbor, new_path))
    
    return max(possible_paths, key = lambda p: p[-1]) if possible_paths else -1

n = 5
edges = [(1, 2), (2, 3), (3, 4), (4, 5)]
availability = {1: ["excavator"], 2: [], 3: ["bulldozer"], 4: ["excavator"], 5: ["crane"]}
start_provider = 2
target_equipment = "excavator"

print(find_shortest_path(n, edges, availability, start_provider, target_equipment))
