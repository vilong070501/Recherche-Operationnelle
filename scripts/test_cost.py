import sys
sys.path.insert(0, '../src/')
import networkx as nx
import matplotlib.pyplot as plt
import utils as ut
import numpy as np

dist = 1000
print("type1 : ", ut.cost_deneigement_1(dist))
print("type2 : ", ut.cost_deneigement_2(dist))

def plot_functions(f1, f2):
    distances = range(dist + 1)
    values1 = [f1(distance) for distance in distances]
    values2 = [f2(distance) for distance in distances]
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
    values1 = [f1(distance) for distance in distances]
    values2 = [f2(distance) for distance in distances]
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
        print(j,k)
        values3 = [f3(distance, j, k) for distance in distances]
        plt.plot(distances, values3, label=f"type_1:{j}, type_2:{k}", linestyle='dotted')
    plt.legend()
    plt.show()

plot_functions(ut.cost_deneigement_1, ut.cost_deneigement_2)
plot_functions_mixte(ut.cost_deneigement_1, ut.cost_deneigement_2, ut.cost_deneigement_mixte)
