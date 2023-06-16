from arguments import args
import algorithms
import utils
import output

if __name__ == '__main__':
    if args:
        if args.h:
            heuristic = utils.readHeuristic(args.h)
            graph, initialState, goalState = utils.readFile(args.ss, heuristic)
        else:
            graph, initialState, goalState = utils.readFile(args.ss)

        initialNode, goalNodes = utils.setNodes(initialState, goalState, graph)

        if args.alg == 'bfs':

            n, visited = algorithms.breadthFirstSearch(initialNode, goalNodes)
            output.printAlgorithmResult(args.alg, n, len(visited))

        elif args.alg == 'ucs':

            n, visited = algorithms.uniformCostSearch(initialNode, goalNodes)
            output.printAlgorithmResult(args.alg, n, len(visited))

        elif args.alg == 'astar':

            n, visited = algorithms.aStarSearch(initialNode, goalNodes)
            output.printAlgorithmResult(args.alg, n, len(visited))

        if args.check_optimistic:

            for states in goalState:
                if states in graph:
                    goalNodes.append(graph[states])

            for key, node in graph.items():
                initialNode = graph[key]
                n, visited = algorithms.uniformCostSearch(initialNode, goalNodes)
                node.check_optimistic = utils.calculateTotalCost(n)

            output.printCheckOptimistic(graph, args.h)

        if args.check_consistent:

            for states in goalState:
                if states in graph:
                    goalNodes.append(graph[states])

            output.printCheckConsistent(graph, args.h)
