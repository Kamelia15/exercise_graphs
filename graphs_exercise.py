edges = [("P1", "P2"), ("P1", "P3"), ("P2", "P3"), ("P3", "P4"), ("P4", "P5")]

#________________________TASK_1________________________
def build_adjacency_list(edges, directed=False):
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []

        graph[u].append(v)
        if not directed:
            graph[v].append(u)

    return graph


def degrees(graph):
    return {v: len(neighbors) for v, neighbors in graph.items()}


def in_out_degree(graph):
    out_degree = {v: len(neighbors) for v, neighbors in graph.items()}
    in_degree = {v: 0 for v in graph}

    for neighbors in graph.values():
        for target in neighbors:
            in_degree[target] += 1

    return in_degree, out_degree


undirected_graph = build_adjacency_list(edges, directed=False)
deg_dict = degrees(undirected_graph)

directed_graph = build_adjacency_list(edges, directed=True)
in_deg, out_deg = in_out_degree(directed_graph)

# print("Undirected Graph:", undirected_graph)
# print("Degrees:", deg_dict)
# print("In-degrees:", in_deg)
# print("Out-degrees:", out_deg)



#________________________TASK_3________________________
def dfs(graph, start):
    visited = []

    def explore(v):
        visited.append(v)
        for neighbor in sorted(graph.get(v, [])):
            if neighbor not in visited:
                explore(neighbor)

    explore(start)
    return visited


def connected_components(graph):
    components = []
    visited_all = set()

    for vertex in sorted(graph.keys()):
        if vertex not in visited_all:
            component_nodes = set(dfs(graph, vertex))
            components.append(component_nodes)
            visited_all.update(component_nodes)

    return components


def is_weakly_connected(graph):
    if not graph:
        return True

    undirected = {v: set() for v in graph}
    for u, neighbors in graph.items():
        for v in neighbors:
            undirected[u].add(v)
            if v not in undirected:
                undirected[v] = set()
            undirected[v].add(u)

    undirected_graph = {v: list(neighbors) for v, neighbors in undirected.items()}
    components = connected_components(undirected_graph)
    return len(components) == 1


edges = [("P1", "P2"), ("P1", "P3"), ("P2", "P3"), ("P3", "P4"), ("P4", "P5")]

graph = {}
for u, v in edges:
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)

print("DFS from P1:", dfs(graph, "P1"))
print("Connected components:", connected_components(graph))

directed_graph = {
    "A": ["B"],
    "B": [],
    "C": ["D"],
    "D": []
}

print("Is weakly connected:", is_weakly_connected(directed_graph))