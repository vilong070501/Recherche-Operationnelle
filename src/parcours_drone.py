import networkx as nx

def shortest_travel(graph, source_node=None):
    #if not nx.is_eulerian(graph):
    augmented_graph = graph.copy()

    # Identify nodes with odd degrees
    odd_degree_nodes = [node for node, degree in graph.degree if degree % 2 != 0]

    # Compute distance matrix with dijkstra algorithm
    distance_matrix = dict(nx.all_pairs_dijkstra_path_length(graph, weight='weight'))

    # Create a complete graph among the odd degree nodes
    complete_graph = nx.complete_graph(odd_degree_nodes)
    weights = {(x,y): {"weight": distance_matrix[x][y]} for x, y in complete_graph.edges}
    nx.set_edge_attributes(complete_graph, weights)


    # Compute minimum weight matching on the complete graph
    matching = nx.algorithms.matching.min_weight_matching(complete_graph, weight='weight')
    weighted_matching = [(x, y, distance_matrix[x][y]) for x, y in matching]
    seen = []
    
    # Add matching edges to the original graph
    augmented_graph.add_weighted_edges_from(weighted_matching)
    print(matching)

    # Calculate the Eulerian circuit
    eulerian_circuit = []
    naive_circuit = list(nx.eulerian_circuit(augmented_graph, source_node))

    for edge in naive_circuit:
        x = (edge[1], edge[0])
        if edge in matching or x in matching:
            if edge not in graph.edges:
                aug_path = nx.shortest_path(graph, edge[0], edge[1])
                eulerian_circuit += list(zip(aug_path[:-1], aug_path[1:]))
            else:
                sorted_edge = tuple(sorted(edge))
                if sorted_edge not in seen:
                    eulerian_circuit.append(edge)
                    seen.append(sorted_edge)
                else:
                    aug_path = nx.shortest_path(graph, edge[0], edge[1])
                    eulerian_circuit += list(zip(aug_path[:-1], aug_path[1:]))
        else:
            eulerian_circuit.append(edge)
    somme = 0
    for edge in eulerian_circuit:
        somme += distance_matrix[edge[0]][edge[1]]
    return eulerian_circuit, somme
