'''
Problem: Build Order
Description: You are given a list of projects and a list of dependencies (which is a list of pairs of projects, where the second project is dependent on the first project). All of a project's dependencies must be built before the project is. Find a build order that will allow the projects to be built. If there is no valid build order, return an error.
Solved: True
'''

class Node(object):
    value = None
    adjacents = []

    def __init__(self, value):
        self.value = value

    def add_adjacent(self, el):
        self.adjacents.append(el)

def find_build_order(projects, dependencies):
    not_dependent = []
    dependent = []
    all_nodes = {}

    for p in projects:
        all_nodes[p] = Node(p)

    for d in dependencies:
        if d[0] not in dependent and d[0] not in not_dependent:
            not_dependent.append(d[0])
        
        if d[1] in not_dependent:
            not_dependent.remove(d[1])
            dependent.append(d[1])
        elif d[1] not in dependent:
            dependent.append(d[1])
        
        all_nodes[d[0]].add_adjacent(d[1])
        print(all_nodes[d[0]])

    if not_dependent:
        print(all_nodes['f'].adjacents)
        for p in not_dependent:
            for p2 in all_nodes[p].adjacents:
                if p2 not in not_dependent:
                    not_dependent.append(p2)

        for p in projects:
            if p not in not_dependent:
                not_dependent.append(p)
        return not_dependent
    else:
        return 'Not possible to create a build order'

        
projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a', 'b'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]

print(find_build_order(projects, dependencies))