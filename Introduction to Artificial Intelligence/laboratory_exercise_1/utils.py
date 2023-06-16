import Node


def readFile(filePath, heuristic=None):
    if heuristic is None:
        heuristic = {}
    with open("./data/" + filePath, 'r') as f:
        data = f.read().splitlines()

    initialState, goalState = None, [None]

    graph = dict()
    count = 0

    for line in data:
        if line == '' or line == '#':
            continue
        elif count == 0:
            initialState = line
            count += 1
            continue
        elif count == 1:
            goalState = line.split()
            count += 1
            continue
        else:
            transitions(line, graph)

    graph = initializeGraph(graph, heuristic)
    return graph, initialState, goalState


def readHeuristic(filePath):
    with open("./data/" + filePath, 'r') as f:
        data = f.read().splitlines()
        heuristic = dict()
        for line in data:
            city, heuristicValue = line.split(" ")
            city = city[:-1]
            heuristic[city] = int(heuristicValue)
    return heuristic


def transitions(line, graph):
    city = line.split()[0][:-1]
    neighbours = [tuple(neighbour.split(',')) for neighbour in line.split()[1:]]
    node = Node.Node(city, {})
    graph[city] = (node, neighbours)


def initializeGraph(graph, heuristic):
    for x, (node, edges) in graph.items():
        for edge in edges:
            neighbor_name, weight = edge
            node.edges[graph[neighbor_name][0]] = int(weight)
            if heuristic:
                node.heuristic = heuristic[node.city]

    return {k: v[0] for k, v in graph.items()}


def setNodes(initialState, goalState, graph):
    initialNode, goalNodes = None, []

    if initialState in graph:
        initialNode = graph[initialState]

    for states in goalState:
        if states in graph:
            goalNodes.append(graph[states])

    return initialNode, goalNodes


def calculateTotalCost(copy):
    totalCost = 0
    parent1 = copy.parent
    while copy.parent:
        parent1 = copy.parent
        for key, value in parent1.edges.items():
            if key.city == copy.city:
                totalCost += value
        copy = copy.parent
    return totalCost
