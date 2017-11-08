from node import Node

class Layer:
    # constructor
    def __init__(self, numb_of_nodes, type_of_output, number, prev_layer_numb_nodes):
        self.numb_of_nodes = numb_of_nodes
        self.nodes = [Node(prev_layer_numb_nodes, 'sigmoid', i) for i in range(numb_of_nodes)]
        self.type_of_output = type_of_output
        
    def run_instance(self, input):
        if self.type_of_output:
            return self.nodes[0].calculate_output(input, True)
        else:
            return [node.calculate_output(input, False) for node in self.nodes]

    def update_weights(self, learning_rate, next_layer):
        for node in self.nodes:
            node.update_weights(learning_rate, next_layer)