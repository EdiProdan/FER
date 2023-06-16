import numpy as np


def find_best_in_population(population):
    best = max(population, key=lambda p: p.fitness)
    return best


def y_hat_list(X, nn):
    y_hat = [nn.feed_forward(x) for x in X]
    return y_hat


def calculate_mse(y_test, y_hat):
    y_test = np.array(y_test)
    y_hat = np.array(y_hat)
    mse = np.mean((y_test - y_hat) ** 2)

    return mse
