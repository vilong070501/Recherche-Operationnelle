import sys
sys.path.insert(0, '../src/')

import networkx as nx
import matplotlib.pyplot as plt
import utils as ut
import parcours_drone as pd
import deneigement as dn

graph = nx.MultiDiGraph()

# Add edges
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0), (6, 7), (7, 8), (8, 9), (9, 6),
         (1, 6), (3, 8), (4, 7), (5, 9), (6, 3), (7, 2), (8, 0), (9, 1), (2, 4), (0, 5)]

graph.add_edges_from(edges)

# Modify the graph to make it a directed Eulerian graph
eulerian_graph = dn.make_directed_eulerian_graph(graph)
eulerian_circuit = list(nx.eulerian_circuit(eulerian_graph))
print(eulerian_circuit)
ut.draw_simple_graph(eulerian_graph, eulerian_circuit)

# Show the graph
plt.show()
