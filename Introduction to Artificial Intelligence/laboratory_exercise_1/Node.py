class Node:
    def __init__(self, city, edges):
        self.city = city
        self.val = 0
        self.edges = edges
        self.parent = None
        self.heuristic = 0
        self.cost = 0
        self.f = 0
        self.check_optimistic = 0
