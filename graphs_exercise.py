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

print("Undirected Graph:", undirected_graph)
print("Degrees:", deg_dict)
print("In-degrees:", in_deg)
print("Out-degrees:", out_deg)