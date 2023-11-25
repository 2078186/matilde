nds = [] #nds stands for nodes
#The Node class represents a node in a tree.
#It has attributes:
#p: Parent node.
#s: Set of child nodes.
#lab: Label of the node.
#sonlabs: Set of labels of its children nodes.
#When a node is created, it is appended to the global list nds.
class Node:

    def __init__(self, parent_node):
        self.p = parent_node
        self.s = set()
        self.lab = ''
        self.sonlabs = set()
        nds.append(self)

    def __repr__(self):
        return '%s(s=%s)' % (self.lab or 'node', self.s)


def buildtree(tree):
#buildtree takes a string tree as input and constructs a tree.
#It uses a nested function getnode to recursively build nodes based on the input string.
#The constructed tree and a dictionary mapping labels to nodes (dd) are returned.
    class cur:

        pos = 0

    dd = {}

    def getnode(par):
        cc = Node(par)
        if tree[cur.pos] == '(':
            while tree[cur.pos] in '(,':
                cur.pos += 1
                cc.s.add(getnode(cc))
            cur.pos += 1
        ff = cur.pos
        while tree[cur.pos] not in '), ;':
            cur.pos += 1
        nam = tree[ff:cur.pos]
        cc.lab = nam
        if nam != '':
            dd[nam] = cc
        return cc

    return (getnode(None), dd)


def cnt(cur):
#cnt takes a node cur and recursively collects all labels of its descendants.
#The collected labels are stored in the sonlabs attribute of the node.
#The function returns a set of labels.
    trt = set()
    for son in cur.s:
        trt.update(cnt(son))
    if cur.lab:
        trt.add(cur.lab)
    cur.sonlabs = trt
    return trt


with open('ctbl1.py') as file:
    (root, d) = buildtree(file.readline().strip())
    alllabs = sorted(cnt(root))
    nn = len(alllabs)
    for j in nds:
        if len(j.sonlabs) not in (0, 1, nn - 1, nn):
            print (''.join(map(str, map(int, map(j.sonlabs.__contains__, alllabs)))))
#The code iterates through all nodes (j) in the global list nds.
#For each node, it checks if the number of unique labels in its descendants (len(j.sonlabs)) is not one of the valid values (0, 1, nn - 1, nn).
#If the condition is not met, it prints a string of 0s and 1s based on whether each label in alllabs is present in j.sonlabs