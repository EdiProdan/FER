import argparse

argParser = argparse.ArgumentParser()
subparsers = argParser.add_subparsers(dest='command')

resolution_parser = subparsers.add_parser(
    'resolution', help='Implrementacija rezolucije opovrgavanjem')
resolution_parser.add_argument(
    'path_to_clauses', help='Putanja do datoteke s popisom klauzula')

cooking_parser = subparsers.add_parser(
    'cooking', help='Implementacija kuharskog asistenta')
cooking_parser.add_argument(
    'path_to_clauses', help='Putanja do datoteke s popisom klauzula')
cooking_parser.add_argument(
    'path_to_user_commands', help='Putanja do datoteke korisnickih naredbi')

args = argParser.parse_args()

