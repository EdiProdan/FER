import argparse

argParser = argparse.ArgumentParser()
subparsers = argParser.add_subparsers(dest='command')

init_parser = subparsers.add_parser('init', help='Inicijalizacija alata')
init_parser.add_argument('arg1', help='Glavna zaporka')

put_parser = subparsers.add_parser('put', help='Pohrana para adresa, zaporka')
put_parser.add_argument('arg1', help='Glavna zaporka')
put_parser.add_argument('arg2', help='Adresa')
put_parser.add_argument('arg3', help='Zaporka')

get_parser = subparsers.add_parser('get', help='Dohvaćanje pohranjene zaporke za zadanu adresu')
get_parser.add_argument('arg1', help='Glavna zaporka')
get_parser.add_argument('arg2', help='Adresa')


args = argParser.parse_args()