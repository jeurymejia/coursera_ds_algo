from union_find import Node, union, find


def get_close_values(bin_str, max_diff):
    """Get a list of strings representing numbers in binary that
    differ from an input string by at most max_diff bits

    Args:
        bin_str: A str limited to characters 1 or 0
        diff: The max number of bits the "close" binary strings should
            differ from bin_string by
    """
    close_set = set([bin_str])
    if max_diff == 0:
        return set([bin_str])
    for idx, char in enumerate(bin_str):
        if char == '1':
            new_char = '0'
        else:
            new_char = '1'
        close_set.add(bin_str[:idx] + new_char + bin_str[idx+1:])
    other_closes = set()
    for close in close_set:
        other_closes = other_closes.union(get_close_values(close, max_diff-1))
    return close_set.union(other_closes)


def get_diff_bits(str1, str2):
    diff = 0
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            diff += 1
    return diff


def main():
    with open('clustering_big.txt', 'rt') as file:
        node_cnt, bits = [int(x) for x in file.readline().split()]
        bs_list = [
            "".join(line.split())
            for line in file.readlines()
        ]

    # Build a mapping betwen binary strings and their indicies within
    # the input file -- the indicies will serve as node labels
    #
    # Note: There are duplicate binary strings in the input file
    # (so there will be multiple nodes with the same binary string value)
    bs_dict = {}
    for idx, string in enumerate(bs_list):
        try:
            bs_dict[string].append(idx)
        except KeyError:
            bs_dict[string] = [idx]

    # Initialize list of Nodes for tracking clusters with Union-Find
    uf_nodes = [Node(i) for i in range(node_cnt)]

    # Initialize an empty set to store edges
    edges = set()
    # Iterate over all binary strings and their indicies
    for cur_label, string in enumerate(bs_list):
        # For each binary string, get a list of all binary strings within
        # 2 bits of difference ("close strings")
        close_strs = get_close_values(string, max_diff=2)
        for close_str in close_strs:
            # For each close string, create an edge between the current node
            # and all nodes corresponding to the close string of the form
            # (i, j, difference in bits) where i < j and add to edge set
            nearby_nodes = bs_dict.get(close_str, [])
            if nearby_nodes:
                distance = get_diff_bits(string, close_str)
            for nearby_label in nearby_nodes:
                if cur_label < nearby_label:
                    edges.add((cur_label, nearby_label, distance))
                elif cur_label > nearby_label:
                    edges.add((nearby_label, cur_label, distance))

    # Make a list from the edge set and sort edges in reverse order
    # of bits
    edges = sorted(list(edges), key=lambda x: -x[2])

    # Run Kruskal's algorithm on the edges until none remain
    cluster_cnt = node_cnt
    while edges:
        # Get next smallest edge
        node_label_a, node_label_b, distance = edges.pop()
        node_a, node_b = uf_nodes[node_label_a], uf_nodes[node_label_b]
        if union(node_a, node_b):
            # node_a and node_b were in separate clusters that have
            # been merged by union()
            cluster_cnt -= 1
    # Return the number of clusters
    print("Cluster count: {}".format(cluster_cnt))


if __name__ == "__main__":
    main()
