import numpy as np 
from .layer import Layer

class NeuralNetwork:
    def __init__(self, numb_of_layers, nodes_per_layer, type_of_output, input, targets):
        self.numb_of_layers = numb_of_layers
        self.nodes_per_layer = nodes_per_layer
        self.type_of_output = type_of_output
        self.input = input
        self.targets = targets
        self.layers = []

        prev_layer_numb_nodes = len(input[0])
        for i in range(numb_of_layers):
            l = Layer(nodes_per_layer[i], None, i, prev_layer_numb_nodes)
            self.layers.append(l)
            prev_layer_numb_nodes = nodes_per_layer[i]
        
        # add the last regression layer
        self.layers.append(Layer(1, type_of_output, numb_of_layers, prev_layer_numb_nodes))

    def run(self, numb_of_iterations):
        error_per_i = []
        for i in range(numb_of_iterations):
            error_i = []
            for j in range(len(self.input)):
                input = self.input[j]
                target = self.targets[j]

                # go forward through network, and calculate the output
                for layer in self.layers:
                    input = layer.run_instance(input)

                error = ((target-input)**2)/2
                self.layers[-1].nodes[0].error_term = error
                error_i.append(error)

                for k in range(len(self.layers)-2, -1, -1):
                    self.layers[k].update_weights(0.1, self.layers[k+1])

            error_per_i.append(sum(error_i))
            if i%50 == 0:
                print(i)
        print(error_per_i[0])
        print(error_per_i[-1])