"""Calculate the strongly-connected components of a graph"""

from itertools import dropwhile


def reverse_edges(graph):
    """Reverse the edges of a graph in place."""
    # Add None to the end of each list of edges to act as sentinel value
    for node in graph:
        try:
            graph[node].append(None)
        except AttributeError:
            graph[node] = [None]
    # Add each new edge after the None sentinel
    for node, edge_heads in graph.items():
        new_key_values = {}
        for head in edge_heads:
            if head is None:
                break
            try:
                graph[head].append(node)
            except KeyError:
                new_key_values[head] = [None, node]
    # Add any new key-values to original adjacency list
    graph.update(new_key_values)
    # Remove all edges before the None sentinel, as well as the sentinel
    for node, edge_heads in graph.items():
        graph[node] = edge_heads[edge_heads.index(None)+1:]
