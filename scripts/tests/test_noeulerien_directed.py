import sys
sys.path.insert(0, '../../src/')

import networkx as nx
import matplotlib.pyplot as plt
import utils as ut
import parcours_drone as pd
import deneigement as dn

graph = nx.MultiDiGraph()

# Add edges
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0), (6, 7), (7, 8), (8, 9), (9, 6),
         (1, 6), (3, 8), (4, 7), (5, 9), (6, 3), (7, 2), (8, 0), (9, 1), (2, 4), (0, 5),
         (7, 1), (3, 5)]
graph.add_edges_from(edges)

print(nx.is_eulerian(graph))

# Modify the graph to make it a directed Eulerian graph
eulerian_graph = dn.eulerize_directed_graph(graph)
eulerian_circuit, distance = pd.shortest_travel(eulerian_graph)
print("Cylce eulérien\n")
print(eulerian_circuit)
print("distance = " + str(distance))
ut.draw_simple_graph(eulerian_graph, eulerian_circuit)


# Show the graph
plt.show()
