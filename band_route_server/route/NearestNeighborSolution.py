def nearest_neighbor(dists):
    """

    :param dists: Data matrix containing distance between two nodes.
    :return: A tuple, (cost, path taken).
    """
    # Create variables to hold total distance, path taken, and current node
    total_distance = 0
    path = [0]
    current = 0

    # Loop through nodes finding shortest path according to nearest neighbor approach.
    while(len(path) < len(dists[0])):
        # On current node, find nearest node.
        shortest_distance = 2_000_000_000  # Sentinel value for shortest distance.
        next_node = 0
        i = 0

        # Loop through all nodes adjenct to current node, and find nearest node not already visited.
        for distance in dists[current]:
            if distance < shortest_distance and i not in path:
                shortest_distance = distance
                next_node = i
            # Increment i
            i += 1

        # After shortest distance to next node found, move to that node and repeat.
        current = next_node
        path.append(next_node)
        total_distance += shortest_distance

    # Add distance from last node visited to first node
    total_distance += dists[0][current]

    # Return tuple containing total distance and path taken.
    return total_distance, path





