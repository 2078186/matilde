#I take three arguments: T (the Newick format tree), y (the first node), and x (the second node).
#I start by finding the indices of the nodes y and x in the Newick tree string T.
#Next, create a substring t by extracting the characters from the Newick tree string between the indices of x and y, inclusive, and filtering it to contain only characters '(', ')', and ','.
#The code enters a loop that replaces any occurrences of '(,)' in the t string with an empty string, effectively removing empty branches. This loop continues until there are no more occurrences of '(,)' in the t string.
#The code then checks if the remaining characters in t consist only of '(' characters or only ',' characters. If so, it returns a distance of the count of such characters. For example, if t contains only '(', it returns the count of '(' characters plus 2. If t contains only ',', it also returns the count of ',' characters plus 2.
#If neither of the above conditions is met, it calculates the distance between nodes x and y by counting the number of ')' and '(' characters in the t string, and adding 2 to the count. This calculation considers x and y to be the ends of a path in the tree.
def dis_tree(T, y,x):
    y_index = T.find(y)
    x_index = T.find(x)
    t = [i for i in T[min(x_index, y_index):max(x_index, y_index)] if i in [')','(',',']]
    bracket = ''

    for i in t:
        bracket += i
    while '(,)' in bracket:
        bracket = bracket.replace('(,)','')
    if bracket.count('(') == len(bracket):
        return len(bracket)
    if bracket.count(',') == len(bracket):
        return 2
    else:
        return bracket.count(')') + bracket.count('(') + 2
    
if __name__=='__main__':
    with open('input11.py', 'r') as file:
        tree = [line.strip().replace(';','') for line in file.readlines() if len(line.strip()) > 0]
        # iterate over the tree list with a step of 2, assuming that each pair of lines in the file represents a tree and the pair of nodes for which the distance needs to be calculated.
    for i in range(0, len(tree), 2):
        T = tree[i]
        y,x = tree[i+1].split(' ')
        print(dis_tree(T, y, x), end=" ")
    print() #This line prints a newline character to end the output after processing all the tree-node pairs.