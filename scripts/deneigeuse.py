import sys
sys.path.insert(0, '../src/')

import osmnx as ox
import deneigement as dn
import utils as ut
from datetime import date

if len(sys.argv) == 1:
    print("\tUsage: python3 script.py <cityName>")
    exit()

# Define the location or address
city = sys.argv[1]
address = city + ", Montréal"

# Use OSMnx to download the street network
graph = ox.graph_from_place(address, network_type='drive')
def weight(v, u, e):
    return e[0]['length']

optimal_path, distance = dn.shortest_travel(graph, weight)
cost1, jours1 = ut.cost_deneigement_1(distance)
cost2, jours2 = ut.cost_deneigement_2(distance)
cost_mixte, jours_mixte = ut.cost_deneigement_mixte(distance, 0.1, 0.9)


output_file = open("result_deneigeuse.txt", "a")
output_file.write("-------------------------------------------------------------\n")
output_file.write(date.today().strftime("%B %d, %Y") + "\n")
output_file.write("Parcours des déneigeuses sur le quartier " + address + "\n")
output_file.write("Longueur totale du parcours = " + str(distance) +"km\n")
output_file.write("Type1 : Coût total = " + str(cost1) + "€, Temps nécessaire =" + ut.pretty_time(jours1) + "\n")
output_file.write("Type2 : Coût total = " + str(cost2) + "€, Temps nécessaire =" + ut.pretty_time(jours2) + "\n")
output_file.write("Type_mixte (0.1 type1, 0.9 type2): Coût total = " + str(cost_mixte) + "€, Temps nécessaire = " + ut.pretty_time(jours_mixte) + "\n")
output_file.close()

print(date.today().strftime("%B %d, %Y") + "\n")
print("Parcours des déneigeuses sur le quartier \033[91m" + address + "\033[0m")
ut.pretty_print(distance)
print("Chemin complet\n")
print(optimal_path)

