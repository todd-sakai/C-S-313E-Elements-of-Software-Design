import sys
from AMGraph import *

if __name__ == "__main__":
    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('topological.in')
    else:
        in_data = sys.stdin
    
    # Initialize the graph
    graph = AMGraph()
    
    # Read number of vertices
    num_vertices = int(in_data.readline().strip())

    # Add num_vertices to the graph
    for i in range(num_vertices):
        vertex_label = in_data.readline().strip()
        graph.add_vertex(vertex_label)
    
    # Read number of edges
    num_edges = int(in_data.readline().strip())

    # Add num_edges to the graph
    for i in range(num_edges):
        edge = in_data.readline().strip().split()
        from_index = graph.get_index(edge[0])
        to_index = graph.get_index(edge[1])
        graph.add_edge(from_index, to_index)

    if graph.has_cycle():
        print("The graph has a cycle")
    else:
        print("The graph does not have a cycle")
        print()

        topo_sort = graph.topological_sort()
        for vertex in topo_sort:
            print(vertex)


