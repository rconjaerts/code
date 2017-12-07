import numpy as np

class Node:

    # constructor
    def __init__(self, input_size, activation_function, position):
        self.current_weights = np.divide(np.random.randint(-5, 5, input_size).astype(float), 100)
        self.activation_function = activation_function
        self.latest_output = 0
        self.position = position
        self.x = None
        self.error_term = None

    # calculate the error rating of the node
    def calculate_error_term(self, next_layer):
        next_layer_weights = [x.current_weights[self.position] for x in next_layer.nodes]
        next_layer_error = [x.error_term for x in next_layer.nodes]
        self.error_term = self.latest_output*(1-self.latest_output)*np.sum(np.multiply(next_layer_weights, next_layer_error))
        return self.error_term

    # use stochastic gradient descent we update the weights
    def update_weights(self, learning_rate, next_layer):
        error_term = self.calculate_error_term(next_layer)
        weight_update = np.multiply(learning_rate*error_term, self.x)
        #print(weight_update)
        self.current_weights = np.add(self.current_weights, weight_update)
        return True
        
    # depending on the variable we use an activation function
    def perform_activation_function(self, x):
        if self.activation_function == 'sigmoid':
            return 1/(1+np.exp(-x))
        elif self.activation_function == 'tanh':
            return (1-np.exp(-2*x))/(1+np.exp(-2*x))
        elif self.activation_function == 'relu':
            return np.max(0, x)

    # we calculate the output of the node by multiplying the weights with the input (x), and performing the activation function
    def calculate_output(self, x, output_layer):
        self.x = x
        weighted_sum = np.sum(np.multiply(x, self.current_weights))
        if output_layer:
            self.latest_output = weighted_sum
            return weighted_sum
        else:
            self.latest_output = self.perform_activation_function(weighted_sum)
            return self.latest_output