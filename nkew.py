import io
from Bio import Phylo
import sys

file = open('inputt13.py', 'r')
#read the content of the file and split it into pairs using '\n\n' as the delimiter. 
#each pair consists of two parts: the first part is a Newick format phylogenetic tree, and the second part is a line containing two node names, separated by a space.
pairs = [i.split('\n') for i in file.read().strip().split('\n\n')]

for i, line in pairs:
    #use a for loop to iterate through each pair in the pairs list.
    #For each pair, split the first part (Newick tree) from the second part (node names) and assign them to i and line, respectively.
    #then split the line to extract the two node names, x and y.
    y,x = line.split()
    tree = Phylo.read(io.StringIO(i), 'newick')
    #calculate the distance between nodes x and y in the tree using the tree.distance(x, y) method. This calculates the phylogenetic distance between the two specified nodes.
    sys.stdout.write('%s' % round(tree.distance(x,y)) + ' ')
sys.stdout.write('\n')
#After processing all pairs, the code writes a newline character to the standard output, effectively moving to the next line in the output.