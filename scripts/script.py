import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import parcours_drone as pd

# Define the location or address
address = "Outremont, Montreal"

# Use OSMnx to download the street network
graph = ox.graph_from_place(address, network_type='drive')

# Convert the graph to an undirected graph
graph = graph.to_undirected()

eulerian_circuit, distance = pd.shortest_travel(graph)

# Dessinez le sous-graphe en gris
fig, ax = ox.plot_graph(graph, figsize=(10,10), edge_color='gray', edge_linewidth=0.5, 
                        node_size=3, node_color='gray', node_zorder=1, bgcolor='black',
                        show=False, close=False)

# Layout for the graph
layout = nx.spring_layout(graph, seed=42)

# Function to update the edge colors for each frame of the animation
def update(frame):
    # Get the edges to highlight in the current frame
    highlighted_edges = eulerian_circuit[:frame+1]
    
    # Convert edges to nodes
    highlighted_nodes = [edge[0] for edge in highlighted_edges]

    # Add the last node of the last edge, if it exists
    if highlighted_edges:
        highlighted_nodes.append(highlighted_edges[-1][1])
    
    # Draw the graph with default edge colors
    ox.plot_graph_route(graph, highlighted_nodes, route_color='red', 
                        route_linewidth=2, node_size=0, bgcolor='black', show=False, close=False, 
                        ax=ax, edge_color='red')
 

# Set the number of frames equal to the length of M
num_frames = len(eulerian_circuit)

# Create the animation using the update function and the number of frames
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=20)

# Show the animation
plt.show()
