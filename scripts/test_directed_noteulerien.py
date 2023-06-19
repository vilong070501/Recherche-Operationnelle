import sys
sys.path.insert(0, '../src/')

import networkx as nx
import matplotlib.pyplot as plt
import utils as ut
import parcours_drone as pd
import deneigement as dn

graph = nx.MultiDiGraph()

# Add edges
edges = [(1, 2), (2, 3), (1, 4), (7, 4), (8, 7), (5, 3), (3, 6), (7, 1), (7,3),
        (7,5), (6,1), (4,5), (4,8)]

graph.add_edges_from(edges)
pos = nx.spring_layout(graph)
nx.draw_networkx(graph, pos, with_labels=True, arrows=True, node_color='lightblue', node_size=500)

# Show the graph
plt.title("Directed Non-Eulerian Graph")
plt.axis('off')
plt.show()

# Modify the graph to make it a directed Eulerian graph
eulerian_graph = dn.make_directed_eulerian_graph(graph)
eulerian_circuit = list(nx.eulerian_circuit(eulerian_graph))
print(eulerian_circuit)
ut.draw_simple_graph(eulerian_graph, eulerian_circuit)

# Show the graph
plt.show()
