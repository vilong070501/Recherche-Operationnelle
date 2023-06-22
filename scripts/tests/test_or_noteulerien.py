import sys
sys.path.insert(0, '../../src/')

import networkx as nx
import utils as ut
import parcours_drone as pd
import deneigement as dn

# Créer un graphe vide
graph = nx.MultiDiGraph()

# Ajouter des sommets et des arêtes avec leurs poids (distances)
edges = [
    (0, 1, 10),
    (1, 2, 7),
    (2, 0, 8),
    (2, 3, 10),
    (3, 4, 6),
    (4, 1, 8),
    (3, 1, 6)
]

# Ajouter les arêtes avec les poids associés
graph.add_weighted_edges_from(edges)
# Vérifier si le graphe est eulérien
if nx.is_eulerian(graph):
    print("Le graphe est eulérien.")
else:
    # Calculate the Eulerian circuit
    try:
        graph = dn.eulerize_directed_graph(graph)
        eulerian_circuit, distance = pd.shortest_travel(graph)
        print("Cylce eulérien\n")
        print(eulerian_circuit)
        print("distance = " + str(distance))
        # Dessiner le graphe avec le circuit eulérien
        ut.draw_simple_graph(graph, eulerian_circuit)

    except KeyError as e:
        print(f"KeyError: {e}. Some vertices might be isolated or unreachable.")

