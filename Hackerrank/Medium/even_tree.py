'''
Problem: https://www.hackerrank.com/challenges/even-tree/problem
Solved: True
'''

# read number of nodes, and edges
inp = input().split(" ")
numb_nodes = int(inp[0])
numb_edges = int(inp[1])
tree = {}
number_of_subtrees = {}

# build tree
for _ in range(numb_edges):
    inp = input().split(" ")
    if int(inp[1]) in tree:
        tree[int(inp[1])].append(int(inp[0]))
    else:
        tree[int(inp[1])] = [int(inp[0])]

count = 0

# count the number of nodes in each subtree
def countSubtree(node):
    if node not in tree:
        #leaf
        number_of_subtrees[node] = 1
        return 1
    else:
        counter = 1
        for x in tree[node]:
            counter += countSubtree(x)
        number_of_subtrees[node] = counter
        return counter
    
countSubtree(1)

# now we loop through the tree to see where we cut off the tree
def countDecompositions(node):
    if node not in tree:
        return 0
    else:
        counter = 0
        for x in tree[node]:
            if number_of_subtrees[x]%2 == 0:
                counter += 1
                counter += countDecompositions(x)
            else:
                counter += countDecompositions(x)
        return counter
print(countDecompositions(1))