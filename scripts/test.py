import networkx as nx
import sys
import utils as ut
import parcours_drone as pd
graph = nx.MultiGraph()

# Ajout des sommets et des arêtes avec leurs poids (distances)
edges = [
    (0, 1, 10),
    (0, 2, 7),
    (0, 3, 4),
    (1, 4, 8),
    (1, 6, 10),
    (2, 3, 3),
    (2, 6, 2),
    (3, 4, 1),
    (3, 7, 9),
    (4, 5, 7),
    (4, 8, 13),
    (5, 7, 2),
    (6, 8, 0),
    (7, 8, 25)
]

# Ajout des arêtes avec les poids associés
graph.add_weighted_edges_from(edges)

eulerian_circuit, distance = pd.shortest_travel(graph, 2)
print(eulerian_circuit)
print(distance)
ut.draw_simple_graph(graph, eulerian_circuit)
