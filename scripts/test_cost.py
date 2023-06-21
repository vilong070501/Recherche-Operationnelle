import sys
sys.path.insert(0, '../src/')
import networkx as nx
import matplotlib.pyplot as plt
import utils as ut
import numpy as np

dist = 1000
res1 = ut.cost_deneigement_1(dist)
res2 = ut.cost_deneigement_2(dist)
res3 = ut.cost_deneigement_mixte(dist, 0.1, 0.9)
print("distance=", dist, "km")
print("type1 : cout=", res1[0], "temps=", ut.pretty_print(res1[1]))
print("type2 : cout=", res2[0], "temps=", ut.pretty_print(res2[1]))
print("type_mixte (0.1 type1, 0.9 type2): cout=", res3[0], "temps=", ut.pretty_print(res3[1]))

def plot_functions(f1, f2):
    distances = range(dist + 1)
    values1 = [f1(distance)[0] for distance in distances]
    values2 = [f2(distance)[0] for distance in distances]
    plt.figure(figsize=(10, 6))
    plt.plot(distances, values1, label='type_1')
    plt.plot(distances, values2, label='type_2')
    plt.title('Cost comparison')
    plt.xlabel('Distance(km)')
    plt.ylabel('Cost(euro)')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_functions_mixte(f1, f2, f3):
    distances = range(dist + 1)
    values1 = [f1(distance)[0] for distance in distances]
    values2 = [f2(distance)[0] for distance in distances]
    plt.figure(figsize=(10, 6))
    plt.plot(distances, values1, label='type_1', linewidth = '3')
    plt.plot(distances, values2, label='type_2', linewidth = '3')
    plt.title('Cost comparison')
    plt.xlabel('Distance(km)')
    plt.ylabel('Cost(euro)')
    plt.grid(True)
    values3 = []
    j = 0.0
    k = 1.0
    for i in range(0, 9):
        j = round(j + 0.1, 2)
        k = round(k - 0.1, 2)
        values3 = [f3(distance, j, k)[0] for distance in distances]
        plt.plot(distances, values3, label=f"type_1:{j}, type_2:{k}", linewidth= '2', linestyle='dotted')
    plt.legend()
    plt.show()

plot_functions(ut.cost_deneigement_1, ut.cost_deneigement_2)
plot_functions_mixte(ut.cost_deneigement_1, ut.cost_deneigement_2, ut.cost_deneigement_mixte)
