import numpy as np
import utils


class NeuralNetwork:
    def __init__(self, input_dim, hidden_dims, output_dim):
        self.input_dim = input_dim
        self.hidden_dims = hidden_dims
        self.output_dim = output_dim
        self.weights = self.initialize_weights(input_dim, hidden_dims, output_dim)
        self.biases = self.initialize_biases(hidden_dims, output_dim)
        self.fitness = 0

    @staticmethod
    def initialize_weights(input_dim, hidden_dims, output_dim):
        weights = [np.random.normal(0, 0.01, (hidden_dims[0], input_dim))]

        for i in range(1, len(hidden_dims)):
            weights.append(np.random.normal(0, 0.01, (hidden_dims[i], hidden_dims[i - 1])))

        weights.append(np.random.normal(0, 0.01, (output_dim, hidden_dims[-1])))
        return weights

    @staticmethod
    def initialize_biases(hidden_dims, output_dim):
        """n x 1 matrix of normally distributed random numbers"""
        biases = []

        for i in range(len(hidden_dims)):
            biases.append(np.random.normal(0, 0.01, (hidden_dims[i], 1)))

        biases.append(np.random.normal(0, 0.01, (output_dim, 1)))
        return biases

    @staticmethod
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    def feed_forward(self, x: np.ndarray):
        x = np.array(x)
        y = x.reshape(-1, 1)

        for i in range(len(self.weights) - 1):
            y = self.sigmoid(np.dot(self.weights[i], y) + self.biases[i])

        y = np.dot(self.weights[-1], y) + self.biases[-1]
        return y.item()  # vrati prvi element iz matrice

    def calculate_fitness(self, X, y):
        y_hat = utils.y_hat_list(X, self)
        self.fitness = 1 / (utils.calculate_mse(y, y_hat) + 1e-10)
