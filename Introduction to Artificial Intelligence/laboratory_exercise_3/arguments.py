import argparse

parser = argparse.ArgumentParser()
parser.add_argument("train", type=str, help="Putanja do datoteke skupa podataka za treniranje")
parser.add_argument("test", type=str, help="Putanja do datoteke skupa podataka za testiranje")
parser.add_argument("depth", type=int, nargs='?', help="Dubina ID3 stabla (opcionalno)")

args = parser.parse_args()
