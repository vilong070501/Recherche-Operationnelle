import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import ceil

def draw_simple_graph(graph, eulerian_circuit):
    # Create a figure and axis for the animation
    fig, ax = plt.subplots()

    # Layout for the graph
    layout = nx.spring_layout(graph, seed=42)

    # Function to update the edge colors for each frame of the animation
    def update(frame):
        ax.clear()
        # Get the edges to highlight in the current frame
        highlighted_edges = eulerian_circuit[:frame+1]
        
        # Draw the graph with default edge colors
        nx.draw_networkx(graph, pos=layout, with_labels=True, ax=ax)
        
        # Draw the highlighted edges with a different color
        nx.draw_networkx_edges(graph, pos=layout, edgelist=highlighted_edges, edge_color='red', width=3)

    # Set the number of frames equal to the length of M
    num_frames = len(eulerian_circuit)

    # Create the animation using the update function and the number of frames
    ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=800)

    # Show the animation
    plt.show()

def pretty_print(jours):
    """Prints days and hours
    Args:
        jours (float): jours
    """
    entier = int(jours)
    reste = ceil((jours - entier) * 12)
    return f"{entier} jours et {reste} heures"

def cost_drone(distance):
    """Cost of drone walktrough
    Args:
        distance (float): total distance in km
    
    Returns:
        cost (float): euros
        time (float): jours
    """
    #hyp : 12 hours of work
    vitesse = 40
    heures = distance/vitesse
    jours_float = heures/12
    jours = ceil(jours_float)
    return 100 * jours + distance * 0.01, jours_float

#distance en km/h
def cost_deneigement_1(distance):
    """Cost of snow removal using one type 1 vehicule
    Args:
        distance (float): total distance in km
    
    Returns:
        cost (float): euros
        time (float): jours
    """
    #hyp : 12hours of work
    vitesse = 10
    heures = distance/vitesse
    jours_float = heures/12
    jours = ceil(jours_float)
    entier = int(jours_float)
    #hyp : 8 premiers heures chaque jour
    heure_reste = ceil((jours_float - entier) * 12)
    if heure_reste - 8 > 0 :
        depassement = heure_reste - 8
    else :
        depassement = 0
    normal = heure_reste - depassement
    cout_fixe = 500 * jours
    cout_kilometrique = 1.1 * distance
    cout_horaire_entier = (8 * 1.1 + 4 * 1.3) * entier
    cout_horaire_reste = normal * 1.1 + depassement * 1.3
    return cout_fixe + cout_kilometrique + cout_horaire_entier + cout_horaire_reste, jours_float

def cost_deneigement_2(distance):
    """Cost of snow removal using one type 2 vehicule
    Args:
        distance (float): total distance in km
    
    Returns:
        cost (float): euros
        time (float): jours
    """
    #hyp : 12hours of work
    vitesse = 20
    heures = distance/vitesse
    jours_float = heures/12
    jours = ceil(jours_float)
    entier = int(jours_float)
    #hyp : 8 premiers heures chaque jour
    heure_reste = ceil((jours_float - entier) * 12)
    if heure_reste - 8 > 0 :
        depassement = heure_reste - 8
    else :
        depassement = 0
    normal = heure_reste - depassement
    cout_fixe = 800 * jours
    cout_kilometrique = 1.3 * distance
    cout_horaire_entier = (8 * 1.3 + 4 * 1.5) * entier
    cout_horaire_reste = normal * 1.3 + depassement * 1.5
    return cout_fixe + cout_kilometrique + cout_horaire_entier + cout_horaire_reste, jours_float

def cost_deneigement_mixte(distance, k1, k2):
    """Mixted cost of snow removal using one type 1 vehicule and one type 2 vehicule
    
    Args:
        distance (float): total distance in km
        k1 (float): coefficient < 1
        k2 (float): coefficient < 1

    Returns:
        cost (float): euros
        time (float): jours
    """
    res1 = cost_deneigement_1(k1 * distance)
    res2 = cost_deneigement_2(k2 *distance)
    return round(res1[0] + res2[0], 2), res1[1] + res2[1]
