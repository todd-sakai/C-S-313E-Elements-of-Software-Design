from MinPriorityQueue import *
from Stack import *

class Vertex:
    def __init__(self, index, label):
        self.index = index
        self.label = label
    
    def __lt__(self, other):
        return self.label < other.label
    
    def __str__(self):
        return 'Vertex ' + self.label

class AMGraph:
    def __init__(self):
        # List of Vertex objects
        self.vertices = []

        # 2D list / matrix of edges
        self.adjacency_matrix = []
    
    def get_index(self, label):
        for vertex in self.vertices:
            if vertex.label == label:
                return vertex.index
        return None
    
    def add_vertex(self, label):
        self.vertices.append(Vertex(len(self.vertices), label))
        num_vertices = len(self.vertices)

        for i in range(num_vertices - 1):
            self.adjacency_matrix[i].append(0)
        
        new_row = [0] * num_vertices
        self.adjacency_matrix.append(new_row)
    
    def add_edge(self, from_index, to_index, weight=1):
        self.adjacency_matrix[from_index][to_index] = weight
    
    def has_cycle(self):
        """
        Purpose:
            1. Runs modified DFS from every vertex to check for cycles.
        Input:
            None
        Variables:
            [vertex_states]: A list tracking the visitation state of each vertex (0=unvisited, 1=visiting, 2=traversed).
            [initialization_index]: Integer used to initialize the states list.
            [cycle_found]: A boolean flag indicating if a cycle has been detected.
            [starting_vertex]: The current vertex object being checked as a starting point.
            [dfs_stack]: A stack containing the vertex indices we visit.
            [current_vertex_index]: The integer index of the current vertex.
            [target_vertex_index]: The index of the vertex adjacent to the current vertex.
        Output:
            [cycle_found]: Returns True if the graph contains a cycle, False otherwise.
        """
        vertex_states = []
        for initialization_index in range(len(self.vertices)):
            vertex_states.append(0)
            
        cycle_found = False
        
        for starting_vertex in self.vertices:
            if cycle_found == True:
                break
                
            if vertex_states[starting_vertex.index] == 0:
                dfs_stack = Stack()
                dfs_stack.push(starting_vertex.index)
                
                while dfs_stack.is_empty() == False:
                    if cycle_found == True:
                        break
                        
                    current_vertex_index = dfs_stack.peek()
                    
                    if vertex_states[current_vertex_index] == 0:
                        vertex_states[current_vertex_index] = 1
                        
                        for target_vertex_index in range(len(self.vertices)):
                            if cycle_found == True:
                                break
                                
                            if self.adjacency_matrix[current_vertex_index][target_vertex_index] != 0:
                                if vertex_states[target_vertex_index] == 1:
                                    cycle_found = True
                                    break
                                elif vertex_states[target_vertex_index] == 0:
                                    dfs_stack.push(target_vertex_index)
                                    
                    elif vertex_states[current_vertex_index] == 1:
                        vertex_states[current_vertex_index] = 2
                        dfs_stack.pop()
                        
                    elif vertex_states[current_vertex_index] == 2:
                        dfs_stack.pop()
                        
        return cycle_found


    def get_incoming_edge_count(self, vertex_index, remaining_edges):
        """
        Purpose:
            1. Counts the number of edges incoming to a specific vertex.
        Input:
            [vertex_index]: The integer index of the vertex to check.
            [remaining_edges]: A 2D list representing the current adjacency matrix.
        Variables:
            [incoming_count]: An integer tracking the number of incoming edges.
            [from_vertex_index]: The integer index of the potential source vertex.
        Output:
            [incoming_count]: Returns the integer number of incoming edges.
        """
        incoming_count = 0
        
        for from_vertex_index in range(len(self.vertices)):
            if remaining_edges[from_vertex_index][vertex_index] != 0:
                incoming_count += 1
                
        return incoming_count


    def topological_sort(self):
        """
        Purpose:
            1. Determines the topological ordering of the graph using Kahn's Algorithm.
        Input:
            None
        Variables:
            [remaining_edges]: A 2D list deep copy of the adjacency matrix.
            [matrix_row]: The current row being iterated over in the original adjacency matrix.
            [current_row]: The new row being built for the deep copy.
            [element]: The current element in the row being copied.
            [priority_queue]: A MinPriorityQueue to track which vertexes should be added next.
            [vertex]: The vertex object being evaluated for initial 0 incoming edges.
            [sorted_vertices]: A list of Vertex objects indicating the topological sort for the graph.
            [current_vertex]: The vertex currently being processed from the priority queue.
            [from_index]: The index of the current vertex.
            [to_index]: The index of the destination vertex.
        Output:
            [sorted_vertices]: Returns a list of Vertex objects representing the sorted order.
        """
        remaining_edges = []
        for matrix_row in self.adjacency_matrix:
            current_row = []
            for element in matrix_row:
                current_row.append(element)
            remaining_edges.append(current_row)
            
        priority_queue = MinPriorityQueue()
        
        for vertex in self.vertices:
            if self.get_incoming_edge_count(vertex.index, remaining_edges) == 0:
                priority_queue.enqueue(vertex)
                
        sorted_vertices = []
        
        while priority_queue.is_empty() == False:
            current_vertex = priority_queue.dequeue()
            sorted_vertices.append(current_vertex)
            
            from_index = current_vertex.index
            
            for to_index in range(len(self.vertices)):
                if remaining_edges[from_index][to_index] != 0:
                    remaining_edges[from_index][to_index] = 0
                    
                    if self.get_incoming_edge_count(to_index, remaining_edges) == 0:
                        priority_queue.enqueue(self.vertices[to_index])
                        
        return sorted_vertices
