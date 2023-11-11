class Graph:
    def __init__(self, edges, nodes):
        self.nodes = nodes
        self.edges = edges


def create_graph(f_path):
    #This function takes a file path f_path as input and reads a graph from that file.
    #with open(f_path) as f: opens the file specified by f_path.
    #n = int(f.readline()) reads the first line of the file, which is assumed to contain an integer n, representing the number of nodes in the graph. It converts the read value to an integer and assigns it to n.
    #edges = [] initializes an empty list called edges to store the edges of the graph.
    #The code then iterates over the remaining lines in the file and processes them. Each line is split by spaces, and the resulting tokens (presumably representing node pairs) are stripped of leading and trailing whitespace. These token pairs are added to the edges list.
    #finally, the function returns an instance of the Graph class initialized with the list of edges and the number of nodes read from the file.
    with open(f_path) as f:
        n = int(f.readline())
        edges = []
        for line in f:
            raw_edge = line.split(' ')
            #nds stands for nodes
            edge = [nds.strip() for nds in raw_edge]
            edges.append(edge)

        return Graph(edges,n)


new_graph = create_graph('input2.py')
expected_edges = new_graph.nodes - 1 #This line calculates the expected number of edges in a tree graph. In a tree with n nodes, there are n - 1 edges. It assigns this value to the variable expected_edges.
edges_to_add = expected_edges - len(new_graph.edges)#This line calculates the number of edges that need to be added to the graph to turn it into a tree with the expected number of edges. It subtracts the length of the edges list in the new_graph from the expected_edges and assigns the result to edges_to_add.
print(edges_to_add)# print the number of edges that need to be added to the graph to make it a tree with the expected number of edges.
#This code assumes that 'input2.py' contains data for a graph and calculates how many edges need to be added to make it a tree with n - 1 edges.