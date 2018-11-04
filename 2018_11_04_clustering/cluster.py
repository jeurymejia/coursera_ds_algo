import itertools as it

from union_find import Node, union, find


def main():
    K = 4  # Desired number of clusters

    with open('clustering1.txt', 'rt') as file:
        cluster_cnt = int(file.readline())  # First line is count of nodes
        edges = file.readlines()

    edges = [
        tuple([int(x) for x in line.split()])
        for line in edges
    ]
    # Sort edges in decreasing order of distance.  Sorting in reverse
    # order lets us pop() the next smallest edge in O(1) time
    edges.sort(key=lambda x: -x[2])
    nodes = [Node(x) for x in range(1, 501)]
    distance = 0  # Assuming distance between nodes is always nonnegative

    # >= because we want the mininum distance between clusters AFTER
    # we only have K clusters
    while cluster_cnt >= K:
        while True:
            # Get next smallest edge
            node_label_a, node_label_b, distance = edges.pop()
            node_a, node_b = nodes[node_label_a-1], nodes[node_label_b-1]
            if union(node_a, node_b):
                # node_a and node_b were in separate clusters that have
                # been merged by union()
                cluster_cnt -= 1
                break
    return distance


if __name__ == "__main__":
    print(main())  # 106
