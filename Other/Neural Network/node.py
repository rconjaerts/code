import numpy as np

class Node:

    # constructor
    def __init__(self, input_size, activation_function, position):
        self.current_weights = np.random.randint(-5, 5, input_size)/100
        self.activation_function = activation_function
        self.latest_output = 0
        self.position = position

    # calculate the error rating of the node
    def calculate_error_term(self, target_output, next_layer):
        next_layer_weights = [x.current_weights[self.position] for x in next_layer]
        next_layer_error = [x.error_term for x in next_layer]
        self.error_term = self.latest_output*(1-self.latest_output)*np.sum(np.multiply(next_layer_weights, next_layer_error))
        return self.error_term

    # use stochastic gradient descent we update the weights
    def update_weights(self, x, target_output, learning_rate, next_layer):
        error_term = calculate_error_term(target_output, next_layer)
        weight_update = learning_rate*error_term*x
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
    def calculate_output(self, x):
        weighted_sum = np.sum(np.multiply(x, self.current_weights))
        self.latest_output = self.perform_activation_function(weighted_sum)
        return self.latest_output