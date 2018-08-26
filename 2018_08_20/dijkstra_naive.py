"""Naive implementation of Dijkstra's algorithm that runs in O(nm) time"""


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
    def get_edges():
        """Return a list of all edges where the tail of the edge has
        been visited and the head of the edge has not

        Each edge in the list is a 3-tuple of the form
        (tail, head, edge_weight)
        """
        edges = []
        for tail in visited:
            for head, edge_weight in graph[tail]:
                if head not in visited:
                    edges.append((tail, head, edge_weight))
        return edges

    def get_edges_with_greedy_score():
        """Return a list of edges with their corresponding greedy score"""
        edges_with_scores = []
        for tail, head, edge_weight in get_edges():
            greedy_score = A[tail-1] + edge_weight
            edges_with_scores.append((tail, head, greedy_score))
        return edges_with_scores

    A = [1000000 for _ in range(len(graph))]  # Computed shortest distances
    A[s-1] = 0  # Distance from s to s is 0; subtract 1 for zero-based index
    B = [[] for _ in range(len(graph))]  # Node-to-node shortest paths
    visited = set([s])  # Nodes processed so far
    while len(visited) < len(graph):
        tail, head, greedy_score = min(get_edges_with_greedy_score(),
                                       key=lambda x: x[2])
        visited.add(head)
        A[head-1] = greedy_score
        B[head-1] = B[tail-1] + [head]
    return A


def main():
    target_nodes = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    g = build_graph("DijkstraData.txt")
    shortest_path_distances = dijkstra(g, 1)
    distances = [shortest_path_distances[x-1] for x in target_nodes]
    print(",".join([str(x) for x in distances]))


if __name__ == "__main__":
    main()
