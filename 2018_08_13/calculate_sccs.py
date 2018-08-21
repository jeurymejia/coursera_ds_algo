"""Calculate the strongly-connected components of a graph"""

from collections import defaultdict, Counter
from itertools import dropwhile


def build_graph(filepath):
    """Construct a dict-based adjacency list given a text file

    The text file should represent a directed graph as a series of edges,
    with one edge per row.  The first column is the tail of the edge, the
    second is the head.

    Args:
        filepath: Path to input file
    """
    graph = defaultdict(list)
    with open(filepath, 'r') as file:
        for edge in file:
            head, tail = edge.split()
            graph[head].append(tail)
    return graph


def kosaraju(graph):
    """Kosaraju's algorithm for calculating the stongly-connected
    components of a graph in O(n) time

    Args:
        graph: A dict adjacency list where keys are nodes and values
            are lists of neighboring nodes
            e.g., {'node_a': ['node_b', 'node_d', ...], ...}
    Returns:
        A list container the counts of nodes in the five largest
        strongly-connected components of the graph, in descending
        order
    """

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

    def dfs_loop(graph, ordered_nodes):
        # def dfs(graph, node):
        #     nonlocal finishing_times
        #     nonlocal visited
        #     nonlocal sccs
        #     nonlocal t
        #     visited[node] = True
        #     for neighbor_node in graph[node]:
        #         # print("In dfs - Value of visited: {}".format(visited))
        #         # print("In dfs - Value of neighbor nodes: {}".format(graph[node]))
        #         if not visited[neighbor_node]:
        #             # print("{} has not been visited".format(neighbor_node))
        #             visited[neighbor_node] = True
        #             dfs(graph, neighbor_node)
        #     # print("Value of node: {}".format(node))
        #     # print(finishing_times)
        #     finishing_times[t] = node
        #     t += 1
        #     sccs[s] += 1

        def dfs_inorder_iter(graph, start_node):
            """Do iterative *in-order* DFS traversal of graph"""
            nonlocal finishing_times
            nonlocal visited
            nonlocal sccs
            nonlocal t

            if visited[start_node]:
                return

            seen_once = {}
            nodes_seen = 0
            stack = [start_node]
            nodes_in_stack = set(stack)

            while stack:
                # print("stack: {}".format(stack))
                node = stack.pop()
                nodes_in_stack.remove(node)
                if not seen_once.get(node):
                    # It's our first time visiting the node,
                    # so put it back on the stack
                    stack.append(node)
                    nodes_in_stack.add(node)
                    seen_once[node] = True
                    for neighbor_node in graph[node]:
                        if (not visited[neighbor_node]
                                and not seen_once.get(neighbor_node)
                                and neighbor_node not in nodes_in_stack):
                            stack.append(neighbor_node)
                            nodes_in_stack.add(neighbor_node)
                else:
                    # We're backtracking
                    visited[node] = True
                    # print("node: {}".format(node))
                    # print(finishing_times)
                    try:
                        finishing_times[t] = node
                    except IndexError:
                        print("Value of node: {}".format(node))
                        print("IndexError: {}".format(finishing_times))
                        print("Stack: {}".format(stack))
                        print("len(finishing_times): {} | len(stack): {}".format(len(finishing_times), len(stack)))
                        raise
                    t += 1
                    sccs[s] += 1

        n = len(graph)
        finishing_times = [None for _ in range(n)]
        visited = {node: False for node in graph}
        sccs = Counter()

        t = 0  # Finishing time
        s = None  # Leader node
        # print("ordered_nodes: {}".format(ordered_nodes))
        iter_times = 1
        for node in ordered_nodes:
            # print("In dfs_loop - Value of visited: {}".format(visited))
            if not visited[node]:
                s = node
                # print("Going into dfs_inorder_iter for the {} time".format(iter_times))
                dfs_inorder_iter(graph, node)
                # print("Done with {} iteration(s) of dfs_inorder_iter".format(iter_times))
                iter_times += 1
        return finishing_times, sccs

    print("Reversing edges for first time...")
    reverse_edges(graph)
    print("Beginning first iteration of dfs_loop...")
    finishing_times, disregard = dfs_loop(graph, list(graph))
    print("Reversing edges for second time...")
    reverse_edges(graph)
    print("Beginning second iteration of dfs_loop...")
    disregard, sccs = dfs_loop(graph, reversed(finishing_times))
    return [count for leader, count in sccs.most_common(5)]
    # print(disregard)
    # print(sccs)
