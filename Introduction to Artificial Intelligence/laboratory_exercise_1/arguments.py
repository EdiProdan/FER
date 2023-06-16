import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument('--alg', choices=['bfs', 'ucs', 'astar'], help='kratica za algoritam za pretrazivanje')
argparser.add_argument('--ss', help='putanja do opisnika prostora stanja', required=True)
argparser.add_argument('--h', help='putanja do opisnika heuristike', required=False)
argparser.add_argument('--check-optimistic', action='store_true',
                       help='zastavica koja signalizira da se za danu heuristiku zeli provjeriti optimisticnost')
argparser.add_argument('--check-consistent', action='store_true',
                       help='zastavica koja signalizira da se za danu heuristiku zeli provjeriti konsistentnost')

args = argparser.parse_args()
