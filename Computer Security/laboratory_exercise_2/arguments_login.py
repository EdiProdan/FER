import argparse

parser = argparse.ArgumentParser(description="Login to the system")
parser.add_argument("username" ,help="Enter your username")

args = parser.parse_args()