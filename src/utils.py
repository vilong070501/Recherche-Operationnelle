import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import ceil

vitesse = 40

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

def cost(distance):
    #12hours of work
    t = distance/vitesse
    j = ceil(t/12)
    return 100 * j + distance * 0.01
