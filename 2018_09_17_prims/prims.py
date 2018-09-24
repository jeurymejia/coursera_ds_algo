from node_heap import NodeHeap


class Node(object):
    def __init__(self, label, adj_list, min_cost_edge=None):
        self.label = label
        self.adj_list = set(adj_list)
        self.min_cost_edge = min_cost_edge

    def __repr__(self):
        return ("Node(label={}, adj_list={}, min_cost_edge={})"
                .format(self.label, self.adj_list, self.min_cost_edge))


class Edge(object):
    def __init__(self, node1, node2, weight):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight


def prims_mst(nodes, edges):
    # initialize X = set(s) chosen arbitrarily)
    # T = set()  (the spanning tree is initially empty)
    # while X != V
    #   let e=(u,v) be the cheapest edge of G with u in X and v not in X
    #   add e to T
    #   add v to X
    pass
