import sys
sys.path.insert(0, '../src/')

import osmnx as ox
import parcours_drone as pd
import utils as ut
from datetime import date

if len(sys.argv) == 1:
    print("\tUsage: python3 drone.py <cityName>")
    exit()

# Define the location or address
city = sys.argv[1]
address = city + ", Montréal"

# Use OSMnx to download the street network
graph = ox.graph_from_place(address, network_type='drive')

def weight(v, u, e):
    return e[0]['length']

# Convert the graph to an undirected graph
graph = graph.to_undirected()

eulerian_circuit, distance = pd.shortest_travel(graph, weight)
cost, jours = ut.cost_drone(distance)

output_file = open("result_drone.txt", "a")
output_file.write("-------------------------------------------------------------\n")
output_file.write(date.today().strftime("%B %d, %Y") + "\n")
output_file.write("Parcours du drône sur le quartier " + address + "\n")
output_file.write("Longueur totale du parcours = " + str(distance) +"km\n")
output_file.write("Temps de parcours = " + ut.pretty_time(jours) + "\n")
output_file.write("Coût du parcours = " + str(cost) + "€\n")
output_file.close()

print(date.today().strftime("%B %d, %Y"))
print("Parcours du drône sur le quartier \033[91m" + address + "\033[0m")
print("Longueur totale du parcours = \033[92m" + str(distance) +"km\033[0m")
print("Temps de parcours = \033[92m" + ut.pretty_time(jours) + "\033[0m")
print("Coût du parcours = \033[92m" + str(cost) + "€\033[0m")
print("Chemin complet\n")
print(eulerian_circuit)

ut.draw_graph_with_animation(graph, eulerian_circuit)