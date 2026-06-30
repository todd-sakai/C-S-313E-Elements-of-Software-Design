import sys
from ImageGraph import *

# Helper function for creating an instance of ImageGraph
def create_graph(data):
    # creates graph from read in data
    data_list = data.split("\n")

    # get size of image, number of vertexes
    image_size = int(data_list[0])
    vertex_count = int(data_list[1])

    graph = ImageGraph(image_size)

    index = 2

    # create vertexes
    for i in range(vertex_count):
        # vertex info has the format "x,y,color"
        vertex_info = data_list[index].split(",")
        new_vertex = ColorVertex(len(graph.vertexes), int(vertex_info[0]), int(vertex_info[1]), vertex_info[2])
        graph.vertexes.append(new_vertex)
        index += 1

    # read edge count
    edge_count = int(data_list[index])
    index += 1

    # create edges between vertexes
    for i in range(edge_count):
        # edge info has the format "fromIndex,toIndex"
        edge_info = data_list[index].split(",")
        # connect vertex 1 to vertex 2 and the other way around
        graph.vertexes[int(edge_info[0])].add_edge(int(edge_info[1]))
        graph.vertexes[int(edge_info[1])].add_edge(int(edge_info[0]))
        index += 1

    # read search info
    search_info = data_list[index].split(",")
    search_start = int(search_info[0])
    search_color = search_info[1]

    return graph, search_start, search_color

# Helper function for printing output files
def display_output_file(filename):
    print("\n--- Contents of", filename, "---\n")
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                # Strip newline and print exactly as-is
                print(line.rstrip())
    except FileNotFoundError:
        print(f"Could not open {filename}. Make sure the file name is correct.")
    print("\n--- End of", filename, "---\n")

''' ##### DRIVER CODE ##### '''
if __name__ == "__main__":
    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('image.in')
    else:
        in_data = sys.stdin

    # read input
    data = in_data.read()

    # create graph
    graph, search_start, search_color = create_graph(data)

    # For debugging - print matrix
    # graph.print_adjacency_matrix()

    # run bfs
    graph.bfs(search_start, search_color)

    # reset by creating graph again
    graph, search_start, search_color = create_graph(data)

    # run dfs
    graph.dfs(search_start, search_color)

    if debug:
        display_output_file('image.out')
