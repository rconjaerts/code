'''
Problem: Build Order
Description: You are given a list of projects and a list of dependencies (which is a list of pairs of projects, where the second project is dependent on the first project). All of a project's dependencies must be built before the project is. Find a build order that will allow the projects to be built. If there is no valid build order, return an error.
Solved: True
'''

class Node(object):
    def __init__(self, value):
        self.value = value
        self.incoming = []
        self.outgoing = []

def build_graph(projects, dependencies):
    all_nodes = {}

    for p in projects:
        all_nodes[p] = Node(p)

    for source, target in dependencies:
        all_nodes[source].outgoing.append(target)
        all_nodes[target].incoming.append(source)
    return all_nodes

def get_no_incoming(graph):
    no_incoming = []

    for value, node in graph.iteritems():
        if not node.incoming:
            for out in node.outgoing:
                graph[out].incoming.remove(node.value)
            no_incoming.append(node)

    return no_incoming

def find_build_order(projects, dependencies):
    build_order = []
    graph = build_graph(projects, dependencies)

    while projects:
        no_incoming = get_no_incoming(graph)
        if no_incoming:
            for node in no_incoming:
                del graph[node.value]
                projects.remove(node.value)
                build_order.extend(node.value)
        else:
            return 'Not possible'

    return build_order

projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a', 'b'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]

print(find_build_order(projects, dependencies))