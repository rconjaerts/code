class Layer:
    def __init__(self, numb_of_nodes, hidden, number):
        self.numb_of_nodes = numb_of_nodes
        self.nodes = [Node() for _ in range(numb_of_nodes)]
