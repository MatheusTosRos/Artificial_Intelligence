from collections import deque
import heapq

def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        (node, path) = queue.popleft()
        if node in visited:
            continue
        
        visited.add(node)

        if node == goal:
            return path

        for neighbor, _ in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None

# Exemplo de uso:
graph = {
    'Ulm': [('München', 123), ('Würzburg', 183), ('Stuttgart', 83)],
    'München': [('Rosenheim', 59), ('Ulm', 123)],
    'Würzburg': [('Frankfurt', 111), ('Ulm', 183), ('Nürnberg', 104)],
    'Stuttgart': [('Karlsruhe', 64), ('Mannheim', 140), ('Ulm', 83)],
    'Rosenheim': [('Salzburg', 81), ('München', 59)],
    'Frankfurt': [('Würzburg', 111)],
    'Nürnberg': [('Würzburg', 104), ('Bayreuth', 75)]
}

print(bfs(graph, 'Ulm', 'Frankfurt'))

#---------------------------------------------------------------------------------#
def dfs(graph, start, goal, path=None, visited=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    if start == goal:
        return path

    for neighbor, _ in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, path, visited)
            if result:
                return result
    
    path.pop()
    return None

# Exemplo de uso:
print(dfs(graph, 'Ulm', 'Frankfurt'))

#---------------------------------------------------------------------------------#
def ucs(graph, start, goal):
    queue = [(0, start, [start])]
    visited = set()

    while queue:
        (cost, node, path) = heapq.heappop(queue)
        
        if node in visited:
            continue
        
        visited.add(node)

        if node == goal:
            return path, cost

        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(queue, (cost + edge_cost, neighbor, path + [neighbor]))

    return None, float('inf')

# Exemplo de uso:
print(ucs(graph, 'Ulm', 'Frankfurt'))
