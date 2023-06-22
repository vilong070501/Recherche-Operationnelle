import sys
sys.path.insert(0, '../../src/')

import networkx as nx
import utils as ut
import parcours_drone as pd
import utils as ut

# Créer un graph vide
graph = nx.MultiDiGraph()

# Ajout des sommets et des arêtes
edges = [
    (0, 1, 10),
    (1, 2, 7),
    (2, 1, 3),
    (2, 0, 8),
    (2, 3, 10),
    (3, 4, 6),
    (4, 2, 4)
]

# Ajout des arêtes avec le poids associé
graph.add_weighted_edges_from(edges)

print(ut.DFS(graph))

# Test si le graph est eulérien ou non
if nx.is_eulerian(graph):
    # Calcul du circuit eulérien
    eulerian_circuit, distance = pd.shortest_travel(graph)
    print("Cylce eulérien\n")
    print(eulerian_circuit)
    print("distance = " + str(distance))
    # Affichage du graph
    ut.draw_simple_graph(graph, eulerian_circuit)
else:
    print("Le graph n'est pas eulerien")
