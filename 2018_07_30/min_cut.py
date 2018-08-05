import copy
import math
import random


def min_cut(adj_list):
    def get_edges(adj_list):
        edges = []
        for node, neighbors in adj_list.items():
            for neighbor in neighbors:
                edges.append((node, neighbor))

        # Detect self loops:
        for edge in edges:
            if edge[0] == edge[1]:
                # print(edges)
                print(edge)
                raise ValueError("Deteted self loop")
        return edges

    def contract(adj_list, edge):
        merged_away, merged_into = edge[0], edge[1]
        merged_away_edges = adj_list[merged_away]
        adj_list[merged_into] += merged_away_edges
        del adj_list[merged_away]
        for node, neighbors in adj_list.items():
            adj_list[node] = [
                (neighbor if neighbor != merged_away else merged_into)
                for neighbor in neighbors
            ]
        for node, neighbors in adj_list.items():
            adj_list[node] = [
                neighbor
                for neighbor in neighbors
                if neighbor != node
            ]

        # neighbors_to_update = adj_list[merged_away]
        # for neighbor in neighbors_to_update:
        #     adj_list[neighbor] = [
        #         node if node != merged_away else merged_into
        #         for node in adj_list[neighbor]
        #     ]
        #     # Delete self-loops
        #     adj_list[neighbor] = [
        #         node
        #         for node in adj_list[neighbor]
        #         if node != neighbor
        #     ]
        # del adj_list[merged_away]

        # for neighbor_node in adj_list[merged_away]:
        #     adj_list[neighbor_node] = [
        #         (neighbor if neighbor != merged_away else merged_into)
        #         for neighbor in adj_list[neighbor_nodeu]
        #     ]
        #     adj_list[neighbor_node] = [
        #         neighbor
        #         for neighbor in adj_list[neighbor_node]
        #         if neighbor != neighbor_node  # remove self-loops
        #     ]
        # del(adj_list[merged_away])

    edges = get_edges(adj_list)
    iterations = 0
    while len(adj_list) > 2:
        edge = random.choice(edges)
        contract(adj_list, edge)
        edges = get_edges(adj_list)
        iterations += 1
    return len(edges) // 2


def main():
    adj_list = {}
    with open("input.txt", "r", encoding="UTF-8") as file:
        for line in file:
            node_and_neighbors = [int(num) for num in line.split()]
            adj_list[node_and_neighbors[0]] = node_and_neighbors[1:]

    n = len(adj_list)
    trials = (n ** 2) * math.log(n)
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
