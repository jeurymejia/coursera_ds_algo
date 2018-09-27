"""
Heap-based implementation of Prim's MST algorithm that
runs in O(m log n) time.

Script expects a file formatted as follows:

[number_of_nodes] [number_of_edges]
[one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]
[one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]
...

"""

import argparse
import math

from node_heap import NodeHeap


class Node(object):
    def __init__(self, label, edges, min_cost_edge=math.inf):
        self.label = label
        self.edges = set(edges)  # A set of edge IDs
        self.min_cost_edge = min_cost_edge  # Initially infinitely large
        self.min_cost_edge_id = None

    def __repr__(self):
        return ("Node(label={}, edges={}, min_cost_edge={}, "
                "min_cost_edge_id= {})"
                .format(self.label, self.edges, self.min_cost_edge,
                        self.min_cost_edge_id))


class Edge(object):
    def __init__(self, label, node1, node2, weight):
        self.label = label
        self.node1 = node1
        self.node2 = node2
        self.weight = weight

    def __repr__(self):
        return ("Edge({}<->{}, weight={})"
                .format(self.node1, self.node2, self.weight))

    def is_frontier(self, visited):
        """Whether the edge crosses from a visited to unvisited node"""
        visited_nodes = 0
        if self.node1 in visited:
            visited_nodes += 1
        if self.node2 in visited:
            visited_nodes += 1
        return visited_nodes == 1


def prims_mst(edges):
    """Generate minimum spanning tree for a graph."""

    def update_frontier_neighbors(node):
        """For a given *visited* node, update the min_cost_edge
        values of any unvisited neighboring nodes (e.g., those
        nodes connected by an edge that crossed from the set of
        visited nodes to the set of unvisited nodes)
        """
        if node.label not in visited:
            raise ValueError("Can't call update_frontier_neighbors: "
                             "Node {} has not been visited yet"
                             .format(node.label))
        edges_objs = [edges[edge_id] for edge_id in node.edges]
        edges_objs = [
            edge
            for edge in edges_objs
            if edge.is_frontier(visited)
        ]
        updated_neighbors = []
        for edge in edges_objs:
            for node_id in edge.node1, edge.node2:
                if node_id != node.label:
                    frontier_neighbor = nodes[node_id]
                    if edge.weight < frontier_neighbor.min_cost_edge:
                        frontier_neighbor.min_cost_edge = edge.weight
                        frontier_neighbor.min_cost_edge_id = edge.label
                        updated_neighbors.append(frontier_neighbor)
        for neighbor in updated_neighbors:
            heap.delete(neighbor.label)
            heap.insert(neighbor)

    visited = set()  # Stores node labels
    nodes = {}
    # Initialize nodes with initial min_cost_edge values
    for edge_id, edge in enumerate(edges):
        for node_id in edge.node1, edge.node2:
            if not visited:
                # Add the first node_id to visited set
                visited.add(node_id)

            if node_id not in nodes:
                # Must instantiate node
                nodes[node_id] = Node(label=node_id, edges=[edge_id])
            else:
                # Update node's adjacency list
                nodes[node_id].edges.add(edge_id)

            # If the edge is a frontier edge and has weight lower than
            # the node's min_cost_edge, update the min_cost_edge
            if edge.is_frontier(visited):
                if edge.weight < nodes[node_id].min_cost_edge:
                    nodes[node_id].min_cost_edge = edge.weight
                    nodes[node_id].min_cost_edge_id = edge.label

    # Initialize heap
    heap = NodeHeap([
        node
        for node_id, node in nodes.items()
        if node_id not in visited
    ])

    # Main loop -- iterate over unvisited edges
    mst = []
    while len(visited) < len(nodes):
        newly_visited = heap.extract_min()
        mst.append(edges[newly_visited.min_cost_edge_id])
        visited.add(newly_visited.label)
        update_frontier_neighbors(newly_visited)
    return mst


def main(filename):
    with open(filename, 'r') as file:
        file.readline()  # Discard first header line
        lines = file.readlines()
    edges = [
        Edge(*(int(element) for element in [id] + line.split()))
        for id, line in enumerate(lines)
    ]
    mst = prims_mst(edges)
    print("MST: {}".format(mst))
    print("Number of edges in MST: {}".format(len(mst)))
    print("Cost of MST: {}".format(sum(edge.weight for edge in mst)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Prim's MST Algorithm")
    parser.add_argument('filename', help='Path to input file')
    args = parser.parse_args()

    main(args.filename)
