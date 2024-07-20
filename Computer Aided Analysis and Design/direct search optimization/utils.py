import json


def round_nested_list(nested_list, decimal_places=5):
    return [round(x, decimal_places) if isinstance(x, (int, float)) else x for x in nested_list]


def load_config(config_file):
    with open(config_file, 'r') as file:
        return json.load(file)


config = load_config('config.json')
