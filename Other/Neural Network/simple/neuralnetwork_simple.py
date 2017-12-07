import numpy as np 

class NeuralNetwork:
    def __init__(self, numb_of_layers, nodes_per_layer, input_size):
        self.weights = []
        
        #np.empty(numb_of_layers)
        prev_layer_numb_nodes = input_size
        for i in range(numb_of_layers):
            self.weights.append(np.fromiter(self.create_layer(prev_layer_numb_nodes), dtype=float, count=nodes_per_layer[i]))
            #self.weights[i] = np.array([np.divide(np.random.randint(-5, 5, prev_layer_numb_nodes).astype(float), 100) for _ in range(nodes_per_layer[i])])
            prev_layer_numb_nodes = nodes_per_layer[i]

    def create_layer(self, prev_layer_numb_nodes):
        yield np.divide(np.random.randint(-5, 5, prev_layer_numb_nodes).astype(float), 100)


    #  possible activation functions
    def perform_activation_function(self, activation_function, x):
        if activation_function == 'sigmoid':
            return 1/(1+np.exp(-x))
        elif activation_function == 'tanh':
            return (1-np.exp(-2*x))/(1+np.exp(-2*x))
        elif activation_function == 'relu':
            return np.max(0, x)

    def run(self, numb_of_iterations, training, output):
        for _ in range(numb_of_iterations):
            for instance in training:
                prev_layer_output = instance
                
                layer_outputs = []

                for layer in self.weights:
                    curr_layer = []
                    for node in layer:
                        weighted_sum = np.sum(np.multiply(prev_layer_output, node))
                        node_output = perform_activation_function('sigmoid', weighted_sum)
                        curr_layer.append(node_output)
                    layer_outputs.append(curr_layer)
                    prev_layer_output = layer_outputs[-1]
                print(layer_outputs)