import networkx as nx
import utils as ut
from collections import defaultdict


def eulerize_directed_graph(DG):
    # Check if the graph is strongly connected
    if not nx.is_strongly_connected(DG):
        print("Graph is not strongly connected. Cannot convert to directed Eulerian graph.")
        return None
    # Vérifie si le graphe est déjà eulérien
    if nx.is_eulerian(DG):
        return DG

    # Crée une copie du graphe pour ne pas modifier l'original
    G = DG.copy()

    # Calcule le degré de chaque nœud (entrant - sortant)
    diff_degree = defaultdict(int)
    for node in G.nodes():
        diff_degree[node] = G.out_degree(node) - G.in_degree(node)

    # Identifie les nœuds avec plus d'arêtes sortantes que d'arêtes entrantes (sources)
    # et plus d'arêtes entrantes que d'arêtes sortantes (puits)
    sources = [node for node, diff in diff_degree.items() if diff > 0]
    sinks = [node for node, diff in diff_degree.items() if diff < 0]

    while sources and sinks:
        source = sources.pop()
        sink = sinks.pop()
        G.add_weighted_edges_from([(sink, source, nx.shortest_path_length(DG, sink, source))])

        diff_degree[source] -= 1
        diff_degree[sink] += 1
        if diff_degree[source] > 0:
            sources.append(source)
        if diff_degree[sink] < 0:
            sinks.append(sink)

    return G


def shortest_travel(graph, weight_function):
    distance = 0
    optimal_path = []

    diff_degree = defaultdict(int)
    for node in graph.nodes():
        diff_degree[node] = graph.out_degree(node) - graph.in_degree(node)

    """
    path = ut.DFS(graph, dict(diff_degree), 'length')
    print(len(path))

    for path in path:
        for u,v,d in path:
            distance += d
    print(distance)
    """

    condensed_graph = nx.condensation(graph)
    mapping = condensed_graph.graph["mapping"]
    components = nx.strongly_connected_components(graph)
    link_edges = set(graph.edges())
    for component in components:
        subgraph = graph.subgraph(component).copy()

        eulerian_component = eulerize_directed_graph(subgraph)

        if nx.has_eulerian_path(eulerian_component):
            eulerian_path = nx.eulerian_path(eulerian_component)
            tmp = []
            for u, v in eulerian_path:
                tmp.append((u,v))
                distance += nx.shortest_path_length(graph, u, v, weight_function)
            optimal_path.append(tmp)
        link_edges -= set(subgraph.edges())
    """
    print(link_edges)
    print(nx.shortest_path(graph, 213955306, 4774155870))
    print(nx.shortest_path(graph, 4774155870, 213955306))
    """
    
    l = []
    for u, v in link_edges:
        l.append((mapping[u], mapping[v], graph[u][v][0]['length']))

    new_graph = nx.MultiDiGraph()
    new_graph.add_weighted_edges_from(l)

    diff_degree = defaultdict(int)
    for node in new_graph.nodes():
        diff_degree[node] = new_graph.out_degree(node) - new_graph.in_degree(node)

    path = ut.DFS(new_graph, dict(diff_degree), 'weight')
    #optimal_path += path

    for path in path:
        for u, v, d in path:
            distance += d

    return optimal_path, distance / 1000
