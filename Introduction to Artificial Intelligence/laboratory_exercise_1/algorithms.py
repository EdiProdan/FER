import Node


def breadthFirstSearch(initialNode, goalNodes):
    open_ = [initialNode]
    goalNodes = [node.city for node in goalNodes]
    visited = set()
    while open_:
        n = open_.pop(0)

        if n.city in goalNodes:
            return n, visited

        visited.add(n.city)

        n.edges = dict(sorted(n.edges.items(), key=lambda item: item[0].city))

        for m in n.edges:
            if m.city not in visited:
                newNode = Node.Node(m.city, m.edges)
                newNode.parent = n
                open_.append(newNode)

    return None, None


def uniformCostSearch(initialNode, goalNodes):
    open_ = [initialNode]  # open_ is priority queue
    goalNodes = [node.city for node in goalNodes]
    visited = set()
    while open_:

        n = open_.pop(0)

        visited.add(n.city)

        if n.city in goalNodes:
            return n, visited

        n.edges = dict(sorted(n.edges.items(), key=lambda item: item[0].city))

        for m in n.edges:
            if m.city not in visited:
                newNode = Node.Node(m.city, m.edges)
                newNode.parent = n
                newNode.cost = n.cost + n.edges[m]

                if len(open_) == 0:
                    open_.append(newNode)
                else:
                    left, right = 0, len(open_) - 1
                    while left <= right:
                        mid = int((left + right) / 2)
                        if newNode.cost < open_[mid].cost:
                            right = mid - 1
                        else:
                            left = mid + 1
                    open_.insert(left, newNode)

    return None, None


def aStarSearch(initialNode, goalNodes):
    open_ = [initialNode]
    goalNodes = [node.city for node in goalNodes]
    visited = []
    while open_:

        n = open_.pop(0)

        if n.city in goalNodes:
            visited_by_city = set()
            for node in visited:
                visited_by_city.add(node.city)
            return n, visited_by_city

        visited.append(n)

        n.edges = dict(sorted(n.edges.items(), key=lambda item: item[0].city))

        for m in n.edges:
            newNode = Node.Node(m.city, m.edges)
            newNode.parent = n
            newNode.cost = n.cost + n.edges[m]
            newNode.heuristic = m.heuristic
            newNode.f = newNode.cost + newNode.heuristic
            for open_node in open_:
                if open_node.city == m.city:
                    if newNode.cost <= open_node.cost:
                        open_.remove(open_node)

            for visited_node in visited:
                if visited_node.city == m.city:
                    if newNode.cost <= visited_node.cost:
                        visited.remove(visited_node)

            if len(open_) == 0:
                open_.append(newNode)
            else:
                left, right = 0, len(open_) - 1
                while left <= right:
                    mid = int((left + right) / 2)
                    if newNode.f < open_[mid].f:
                        right = mid - 1
                    else:
                        left = mid + 1
                open_.insert(left, newNode)

    return None, None
