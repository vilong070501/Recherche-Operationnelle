import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the location or address
#address = "Montreal, Canada"

# Use OSMnx to download the street network
#graph = ox.graph_from_place(address, network_type='all_private')

graph = nx.MultiGraph()

# Ajout des sommets et des arêtes avec leurs poids (distances)
edges = [
    (0, 1, 10),
    (0, 2, 7),
    (0, 3, 4),
    (1, 4, 8),
    (1, 6, 10),
    (2, 3, 3),
    (2, 6, 2),
    (3, 4, 1),
    (3, 7, 9),
    (4, 5, 7),
    (4, 8, 13),
    (5, 7, 2),
    (6, 8, 0),
    (7, 8, 25)
]

# Ajout des arêtes avec les poids associés
graph.add_weighted_edges_from(edges)

# Identify nodes with odd degrees
odd_degree_nodes = [node for node, degree in graph.degree if degree % 2 != 0]

# Create a complete graph among the odd degree nodes
complete_graph = nx.complete_graph(odd_degree_nodes)


# Compute minimum weight matching on the complete graph
matching = nx.algorithms.matching.min_weight_matching(complete_graph)

# Add matching edges to the original graph
graph.add_edges_from(matching)

# Calculate the Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(graph))
print(eulerian_circuit)

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
    nx.draw_networkx_edges(graph, pos=layout, edgelist=highlighted_edges, edge_color='red')

# Set the number of frames equal to the length of M
num_frames = len(eulerian_circuit)

# Create the animation using the update function and the number of frames
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=1000)

# Show the animation
plt.show()
