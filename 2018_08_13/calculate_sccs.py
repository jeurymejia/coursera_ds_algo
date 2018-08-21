"""Calculate the strongly-connected components of a graph"""

from collections import defaultdict, Counter
from itertools import dropwhile


def build_graph(filepath):
    graph = defaultdict(list)
    with open(filepath, 'r') as file:
        for edge in file:
            head, tail = edge.split()
            graph[head].append(tail)
    return graph


def reverse_edges(graph):
    """Reverse the edges of a graph in place.

    Args:
        graph (defaultdict(list)): An adjacency list representation
            of a directed graph
    Returns:
        None (graph is modified in-place)
    """
    # Add None to the end of each list of edges to act as sentinel value
    for node in graph:
        graph[node].append(None)
    # Add each new edge after the None sentinel
    new_key_values = defaultdict(lambda: list([None]))
    for node, edge_heads in graph.items():
        for head in edge_heads:
            if head is None:
                break
            if head in graph:
                graph[head].append(node)
            else:
                # Don't add new keys to dict while iterating over it
                new_key_values[head].append(node)
    # Add any new key-values to original adjacency list
    graph.update(new_key_values)
    # Remove all edges before the None sentinel, as well as the sentinel
    for node, edge_heads in graph.items():
        graph[node] = edge_heads[edge_heads.index(None)+1:]


def kosaraju(graph):
    """Kosaraju's algorithm for calculating the stongly-connected
    components of a graph in O(n) time
    """

    def dfs_loop(graph, ordered_nodes):
        def dfs(graph, node):
            nonlocal finishing_times
            nonlocal visited
            nonlocal sccs
            nonlocal t
            visited[node] = True
            for neighbor_node in graph[node]:
                # print("In dfs - Value of visited: {}".format(visited))
                # print("In dfs - Value of neighbor nodes: {}".format(graph[node]))
                if not visited[neighbor_node]:
                    # print("{} has not been visited".format(neighbor_node))
                    visited[neighbor_node] = True
                    dfs(graph, neighbor_node)
            # print("Value of node: {}".format(node))
            # print(finishing_times)
            finishing_times[t] = node
            t += 1
            sccs[s] += 1

        n = len(graph)
        finishing_times = [None for _ in range(n)]
        visited = {node: False for node in graph}
        sccs = Counter()

        t = 0  # Finishing time
        s = None  # Leader node
        # print("ordered_nodes: {}".format(ordered_nodes))
        for node in ordered_nodes:
            # print("In dfs_loop - Value of visited: {}".format(visited))
            if not visited[node]:
                s = node
                dfs(graph, node)
        return finishing_times, sccs

    reverse_edges(graph)
    finishing_times, disregard = dfs_loop(graph, list(graph))
    reverse_edges(graph)
    disregard, sccs = dfs_loop(graph, reversed(finishing_times))
    return sccs.most_common(5)
    # print(disregard)
    # print(sccs)
