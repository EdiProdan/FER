import argparse

parser = argparse.ArgumentParser(description='User management')
subparsers = parser.add_subparsers(dest='command', help='sub-command help')

add_parser = subparsers.add_parser('add', help='add help')
add_parser.add_argument('username', help='username to add')

passwd_parser = subparsers.add_parser('passwd', help='passwd help')
passwd_parser.add_argument('username', help='username to change password')

forcepass_parser = subparsers.add_parser(
    'forcepass', help='forcepass help')
forcepass_parser.add_argument(
    'username', help='username to force password change')

del_parser = subparsers.add_parser('del', help='del help')
del_parser.add_argument('username', help='username to delete')

args = parser.parse_args()
