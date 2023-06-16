import utils


def printGraph(graph):
    for node in graph:
        print(f"Node: {node} : Heuristic: {graph[node].heuristic}")
        for edge in graph[node].edges:
            print(f"    Edge: {edge.city} {graph[node].edges[edge]}")


def printAlgorithmResult(algorithm, n, visited):
    print(f"# {algorithm.upper()}")
    if n:
        print(f"[FOUND_SOLUTION]: yes")
    else:
        print(f"[FOUND_SOLUTION]: no")
    print(f"[STATES_VISITED]: {visited + 1}")

    copy = n
    path = []
    if n:
        path = [n.city]

    while n.parent:
        n = n.parent
        path.append(n.city)

    totalCost = utils.calculateTotalCost(copy)

    print(f"[PATH_LENGTH]: ", len(path))

    print("[TOTAL_COST]: {:.1f}".format(totalCost))

    print(f"[PATH]: ", ' => '.join(path[::-1]))


def printCheckOptimistic(graph, filePath):
    print(f"# HEURISTIC-OPTIMISTIC {filePath}")

    optimistic = 'Heuristic is optimistic.'
    for key, node in graph.items():
        condition = "[OK]"
        if node.check_optimistic < node.heuristic:
            condition = "[ERR]"
            optimistic = 'Heuristic is not optimistic.'
        print(
            f"[CONDITION]: {condition} h({node.city}) <= h*: {float(node.heuristic)} <= {float(node.check_optimistic)}")

    print(f"[CONCLUSION]: {optimistic}")


def printCheckConsistent(graph, filePath):
    print(f"# HEURISTIC-CONSISTENT {filePath}")
    conclusion = 'Heuristic is consistent.'
    for key, node in graph.items():
        for edge in node.edges:
            condition = "[OK]"
            if node.heuristic > edge.heuristic + node.edges[edge]:
                condition = "[ERR]"
                conclusion = 'Heuristic is not consistent.'
            print(
                f"[CONDITION]: {condition} h({node.city}) <= h({edge.city}) + c: {float(node.heuristic)} <= {float(edge.heuristic)} + {float(node.edges[edge])}")
    print(f"[CONCLUSION]: {conclusion}")
