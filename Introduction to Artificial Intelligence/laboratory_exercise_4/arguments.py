import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--train", help="path to training data")
parser.add_argument("--test", help="path to test data")
parser.add_argument("--nn", help="neural network architecture")
parser.add_argument("--popsize", type=int, help="population size")
parser.add_argument("--elitism", type=int, help="elitism")
parser.add_argument("--p", type=float, help="mutation probability")
parser.add_argument("--K", type=float, help="standard deviation of gaussian noise")
parser.add_argument("--iter", type=int, help="number of iterations")

args = parser.parse_args()
