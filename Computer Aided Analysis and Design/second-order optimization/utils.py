import json


def load_config(config_file):
    with open(config_file, 'r') as file:
        return json.load(file)


def euclidean_norm(x: list) -> float:
    return sum([x_i ** 2 for x_i in x]) ** 0.5


config = load_config('config.json')
