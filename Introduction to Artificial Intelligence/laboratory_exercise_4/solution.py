import numpy as np
from arguments import args
from read_data import read_train_data, read_test_data
from neuralnet import NeuralNetwork
import utils

if __name__ == "__main__":

    features, target, X_train, y_train = read_train_data(args.train)
    X_test, y_test = read_test_data(args.test)

    hidden_dim = [int(x) for x in args.nn.split('s')[:-1]]


    def create_initial_population(popsize):
        population = []
        for i in range(popsize):
            nn = NeuralNetwork(len(features), hidden_dim, 1)
            population.append(nn)

        return population


    def evaluate(population):
        for p in population:
            p.calculate_fitness(X_train, y_train)


    def crossover(elites):
        """Operator krizanja implementirajte kao aritmeticku sredinu"""
        D = NeuralNetwork(len(features), hidden_dim, 1)
        D.weights = np.mean([e.weights for e in elites], axis=0)
        return D


    def mutate(D, mutation_probability, mutation_stddev):
        """operator mutacije implementirajte kao Gaussov sum, tako da kromosomu tezina pribrojite vektor uzorkovan iz normalne razdiobe sa standardnom devijacijom K. Svaku tezinu kromosoma mutirajte s vjerojatnoscu p"""
        for i in range(len(D.weights)):
            if np.random.random() <= mutation_probability:
                noise = np.random.normal(0, mutation_stddev, D.weights[i].shape)
                D.weights[i] += noise

        # mutate bias
        for i in range(len(D.biases)):
            if np.random.random() <= mutation_probability:
                noise = np.random.normal(0, mutation_stddev, D.biases[i].shape)
                D.biases[i] += noise


    def elitism(population, elite_num):
        """najbolja (ili vise najboljih) jedinki se prenosi u iducu generaciju"""
        elites = [population[x] for x in range(elite_num)]

        # iterate over population
        for p in population:
            for e in elites:
                if p.fitness > e.fitness:
                    elites.remove(e)
                    elites.append(p)

        return elites


    def selection(population):
        """
        Funkcija vraca listu odabranih jedinki iz populacije
        Odabrane jedinke biraju se proporcionalno njihovoj dobroti koristeci roulette wheel selection
        """
        total_fitness = sum([p.fitness for p in population])
        selection_probabilities = [p.fitness / total_fitness for p in population]
        # Sto je jedinka bolja, to je veca vjerojatnost da ce biti odabrana

        selected_population = []

        for _ in range(len(population)):
            # iteriramo kroz duljinu populacije jer zelimo odabrati jednako mnogo jedinki koliko ih ima u populaciji
            # p=selection_probabilities -> vjerojatnost da ce biti odabrana jedinka
            # sto je jedinka bolja, to je veca vjerojatnost da ce biti odabrana
            selected_index = np.random.choice(range(len(population)), p=selection_probabilities)
            selected_population.append(population[selected_index])

        return selected_population


    def print_train_error(population, iteration):
        nn_best = utils.find_best_in_population(population)

        y_hat = utils.y_hat_list(X_train, nn_best)

        mse = utils.calculate_mse(y_train, y_hat)
        print(f"[Train error @{iteration}]: {mse}")


    def print_test_error(population):
        nn_best = utils.find_best_in_population(population)

        y_hat = utils.y_hat_list(X_test, nn_best)

        mse = utils.calculate_mse(y_test, y_hat)
        print(f"[Test error]: {mse}")


    def genetic_algorithm(popsize, elitism_count, mutation_prob, mutation_std, num_iterations):

        P = create_initial_population(popsize)
        evaluate(P)

        for iteration in range(1, num_iterations + 1):

            if iteration % 2000 == 0:
                print_train_error(P, iteration)

            new_P = []
            while len(new_P) < len(P):
                elites = elitism(P, elitism_count)

                D = crossover(elites)

                mutate(D, mutation_prob, mutation_std)

                new_P.append(D)

            P = new_P
            evaluate(P)

        return P


    population = genetic_algorithm(args.popsize, args.elitism, args.p, args.K, args.iter)
    # find best in population
    print_test_error(population)
