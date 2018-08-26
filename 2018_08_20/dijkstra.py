"""Dijkstra's algorithm"""


import heapq as h

from collections import defaultdict


def build_graph(filepath):
    graph = {}
    with open(filepath, "r") as file:
        for line in file:
            node_and_edges = line.split()
            node = int(node_and_edges[0])
            edges = node_and_edges[1:]
            graph[node] = []
            for edge in edges:
                neighbor, weight = [int(x) for x in edge.split(",")]
                graph[node].append((neighbor, weight))
    return graph


def dijkstra(graph, s):
    """Find the shortest path between nodes in a directed weighted graph

    Args:
        s: The starting node
        graph: Dict-based implementation of adjacency list
            {
                <node label> : [(<neighbor node>, <edge weight>), ...],
                ...
            }
    """

    def get_smallest_greedy(node):
        """Given a starting node, return a 3-tuple containng the lowest
        greedy score, node, and the corresponding neighboring node among s's
        non-visited neighbors
        """
        smallest_greedy = None
        for edge in (x for x in graph[node] if x[0] not in visited):
            neighbor, weight = edge
            greedy_score = A[node-1] + weight
            print("Edge {} has greedy score {}".format(edge, greedy_score))
            if smallest_greedy is None or greedy_score < smallest_greedy[0]:
                smallest_greedy = (greedy_score, node, neighbor)
        return smallest_greedy

    def get_unvisited_neighbors(node):
        """Given a node, return a list of the node's unvisited neighbors"""
        l = [
            edge[0]
            for edge in graph[node]
            if edge[0] not in visited
        ]
        print("In get_unvisited_neighbors: about to return {}".format(l))
        return l

    A = [1000000 for _ in range(len(graph))]  # Computed shortest distances
    A[s-1] = 0  # Distance from s to s is 0; subtract 1 for zero-based index
    B = [[] for _ in range(len(graph))]
    visited = set([s])  # Nodes processed so far
    heap = []
    
    # for neighbor in get_unvisited_neighbors(s):
    #     smallest_greedy = get_smallest_greedy(neighbor)
    #     if smallest_greedy:
    #         h.heappush(heap, smallest_greedy)
    print("Value of B before while loop {}".format(B))
    while heap:
        # Among all edges (v,w) with v member of x, w not a member of x,
        # pick one that minimizes a[v-1] + length from v to w
        # (Dijstra's greedy criterion)

        while True:
            print("Heap: {}".format(heap))
            greedy_score, v, w = h.heappop(heap)
            if w in visited:
                # Recalculate greedy_score and put back in heap
                h.heappush(heap, get_smallest_greedy(v))
            else:
                break
        visited.add(w)
        A[w-1] = greedy_score
        for neighbor in get_unvisited_neighbors(w):
            smallest_greedy = get_smallest_greedy(neighbor)
            if smallest_greedy:
                h.heappush(heap, smallest_greedy)

        # print("Value of B before append: {}".format(B))
        # print("Value of B[w-1]: {}".format(B[w-1]))
        # print("Value of B[v-1]: {}".format(B[v-1]))
        # print("Value of w: {}".format(w))
        # print("Value of B[v-1].append(w): {}".format(B[v-1].append(w)))
        B[w-1] = B[v-1] + [w]
        # print("Value of B after append: {}".format(B))

    return A
