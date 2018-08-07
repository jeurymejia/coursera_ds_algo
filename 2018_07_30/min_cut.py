import copy
import math
import random


def min_cut(adj_list):

    edges = []
    for node, neighbors in adj_list.items():
        for neighbor in neighbors:
            edges.append((node, neighbor))

    def contract_edges(adj_list, edges, merged_away, merged_into):
        del adj_list[merged_away]
        edges = [
            (edge[0] if edge[0] != merged_away else merged_into,
             edge[1] if edge[1] != merged_away else merged_into)
             for edge in edges
        ]
        # Remove self-loops
        edges = [edge for edge in edges if edge[0] != edge[1]]
        return edges

    while len(adj_list) > 2:
        edge = random.choice(edges)
        edges = contract_edges(adj_list, edges, edge[0], edge[1])
    return len(edges) // 2


def main():
    adj_list = {}
    with open("input.txt", "r", encoding="UTF-8") as file:
        for line in file:
            node_and_neighbors = [int(num) for num in line.split()]
            adj_list[node_and_neighbors[0]] = node_and_neighbors[1:]

    n = len(adj_list)  # Number of nodes in the graphs
    trials = (n ** 2) * math.log(n)  # Trials needed to get failure risk of 1/n
    min_cut_so_far = None
    for i in range(math.ceil(trials)):
        result = min_cut(copy.deepcopy(adj_list))
        if min_cut_so_far is None or result < min_cut_so_far:
            min_cut_so_far = result
        print("min_cut so far is {} after {} trials".format(min_cut_so_far, i))
    # print("value of trials: {}".format(trials))
    # print("value of n: {}".format(n))


if __name__ == "__main__":
    main()
