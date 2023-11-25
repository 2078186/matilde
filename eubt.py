class Node():
    #The Node class represents a node in a tree.
    #Each node has a name, and if it is an internal node (with no assigned name), it is represented by its internal identifier.

    def __init__(self, name):
        self.name = name

    def __str__(self):
        if self.name is not None:
            return self.name
        else:
            return "internal_{}".format(id(self))

class Tree():
    #The Tree class represents a tree.
    #It has nodes and edges, and the copy method creates a deep copy of the tree.
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def __str__(self):
        return "tree_{} edges: {}".format(id(self), [str(x) for x in self.edges])

    def copy(self):
        node_conversion = {node: Node(node.name) for node in self.nodes}
        new_nodes = list(node_conversion.values())
        new_edges = [Edge(node_conversion[edge.nodes[0]], node_conversion[edge.nodes[1]]) for edge in self.edges]

        new_tree = Tree(new_nodes, new_edges)
        return new_tree

class Edge():
    def __init__(self, node1, node2):
        self.nodes = [node1, node2]

    def __str__(self):
        return "{}--{}".format(*self.nodes)
def enumerate_trees(leaves):
    #The enumerate_trees function takes a list of leaves and recursively generates all possible rooted binary trees with those leaves.
    assert(len(leaves) > 1)
    
    if len(leaves) == 2:
        n1, n2 = leaves
        t = Tree()
        t.nodes = [Node(n1), Node(n2)]
        t.edges = [Edge(t.nodes[0], t.nodes[1])]
        return [t]
    if len(leaves) > 2:
       
        old_trees = enumerate_trees(leaves[:-1])
        new_leaf_name = leaves[-1]
        new_trees = []

       
        for old_tree in old_trees:
            for i in range(len(old_tree.edges)):
                new_tree = old_tree.copy()
                edge_to_split = new_tree.edges[i]
                old_node1, old_node2 = edge_to_split.nodes

         
                new_tree.edges.remove(edge_to_split)

                
                internal = Node(None)
                new_tree.nodes.append(internal)

                
                new_leaf = Node(new_leaf_name)
                new_tree.nodes.append(new_leaf)

              
                new_tree.edges.append(Edge(old_node1, internal))
                new_tree.edges.append(Edge(old_node2, internal))
                new_tree.edges.append(Edge(new_leaf, internal))

                
                new_trees.append(new_tree) 

        return new_trees

def newick_format(tree_in):
    tree = tree_in.copy()

    if len(tree.nodes) == 1:
        return "{};".format(tree.nodes[0])
    if len(tree.nodes) == 2:
        return "({},{});".format(*tree.nodes)
    elif len(tree.nodes) > 2:
       
        for candidate_node in tree.nodes:
            
            if candidate_node.name is not None:
                continue

            adjacent_edges = [edge for edge in tree.edges if candidate_node in edge.nodes]
            adjacent_nodes = [node for edge in adjacent_edges for node in edge.nodes if node in edge.nodes and node is not candidate_node]
            adjacent_leaves = [node for node in adjacent_nodes if node.name is not None]

            
            if len(adjacent_leaves) == 2 or len(adjacent_leaves) == 3:
                leaf1, leaf2 = adjacent_leaves[0: 2]
                edges_to_cut = [edge for edge in adjacent_edges if leaf1 in edge.nodes or leaf2 in edge.nodes]
                candidate_node.name = "({},{})".format(leaf1, leaf2)

                tree.nodes.remove(leaf1)
                tree.nodes.remove(leaf2)
                for edge in edges_to_cut: tree.edges.remove(edge)

                
                return newick_format(tree)

if __name__ == '__main__':
    leaves = open('eubt1.py').read().split()
    trees = enumerate_trees(leaves)

    print ('\n'.join([newick_format(tree) for tree in trees]))
    #The main block reads a file ('eubt1.py') containing a list of leaves.
    #It then generates all possible rooted binary trees using the enumerate_trees function and prints their Newick representations using the newick_format function.