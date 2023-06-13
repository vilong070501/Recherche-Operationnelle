import networkx as nx
import matplotlib.pyplot as plt
import utils as ut

def make_directed_eulerian_graph(graph):
    # Check if the graph is strongly connected
    if not nx.is_strongly_connected(graph):
        print("Graph is not strongly connected. Cannot convert to directed Eulerian graph.")
        return None
    
    # Identify vertices with mismatched in-degree and out-degree
    mismatched_vertices = [v for v in graph.nodes if graph.in_degree(v) != graph.out_degree(v)]
    
    # Check if the graph is already a directed Eulerian graph
    if not mismatched_vertices:
        print("Graph is already a directed Eulerian graph.")
        return graph
    
    # Create a copy of the graph to modify
    modified_graph = graph.copy()
    
    # Add edges to balance the in-degree and out-degree
    for v in mismatched_vertices:
        if modified_graph.in_degree(v) == modified_graph.out_degree(v):
            continue
        else:
            if graph.in_degree(v) > graph.out_degree(v):
                out_degree_diff = graph.in_degree(v) - graph.out_degree(v)
                target_nodes = []
                for neighbor in modified_graph.neighbors(v):
                    if modified_graph.out_degree(neighbor) > modified_graph.in_degree(neighbor):
                        target_nodes.append(neighbor)
                if len(target_nodes) > 0:
                    for _ in range(out_degree_diff):
                        target_node = target_nodes.pop(0)
                        modified_graph.add_edge(v, target_node)
                else:
                    for neighbor in modified_graph.predecessors(v):
                        if modified_graph.out_degree(neighbor) > modified_graph.in_degree(neighbor):
                            target_nodes.append(neighbor)
                    if len(target_nodes) == 0:
                        print("Line 38: Unable to modify graph to make it directed Eulerian.")
                        return None
                    else:
                        for _ in range(out_degree_diff):
                            target_node = target_nodes.pop(0)
                            modified_graph.add_edge(v, target_node)
                
            elif graph.out_degree(v) > graph.in_degree(v):
                in_degree_diff = graph.out_degree(v) - graph.in_degree(v)
                source_nodes = []
                for neighbor in modified_graph.neighbors(v):
                    if modified_graph.in_degree(neighbor) > modified_graph.out_degree(neighbor):
                        source_nodes.append(neighbor)
                if len(source_nodes) > 0:
                    for _ in range(in_degree_diff):
                        source_node = source_nodes.pop(0)
                        modified_graph.add_edge(source_node, v)
                else:
                    for neighbor in modified_graph.predecessors(v):
                        if modified_graph.in_degree(neighbor) > modified_graph.out_degree(neighbor):
                            source_nodes.append(neighbor)
                    if len(source_nodes) == 0:
                        print("Line 61: Unable to modify graph to make it directed Eulerian.")
                        return None
                    else:
                        for _ in range(in_degree_diff):
                            source_node = source_nodes.pop(0)  
                            modified_graph.add_edge(source_node, v)

    # Verify if the modified graph is now a directed Eulerian graph
    if nx.is_strongly_connected(modified_graph) and all(modified_graph.in_degree[v] == modified_graph.out_degree[v] for v in modified_graph.nodes):
        print("Graph successfully modified to a directed Eulerian graph.")
        return modified_graph
    else:
        print("Line 53: Unable to modify graph to make it directed Eulerian.")
        return None

# Example usage
# Create a directed graph using NetworkX
graph = nx.MultiDiGraph()
#graph.add_edges_from([(1, 2), (2, 3), (3, 1), (3, 4), (4, 1)])
#graph.add_edges_from([(1, 2), (2, 3), (3, 1), (4, 3), (1, 4)])
graph.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (5, 3), (4, 2)])

# Modify the graph to make it a directed Eulerian graph
eulerian_graph = make_directed_eulerian_graph(graph)
eulerian_circuit = list(nx.eulerian_circuit(eulerian_graph))
print(eulerian_circuit)
ut.draw_simple_graph(eulerian_graph, eulerian_circuit)

# Show the graph
plt.show()