import itertools as it


class Node(object):
    def __init__(self, label):
        self.label = label
        self.parent = self
        self.rank = 0

    def __repr__(self):
        return str(self.label)


def union(x, y):
    """Merge two clusters

    Args:
        x: a Node
        y: a Node

    Returns True if two clusters were merged, or False if x and y
    were already in the same cluster
    """
    x_root = find(x)
    y_root = find(y)
    if x_root.rank > y_root.rank:
        y_root.parent = x_root
    elif x_root.rank < y_root.rank:
        x_root.parent = y_root
    elif x_root != y_root:  # Unless x and y are already in same cluster, merge
        y_root.parent = x_root
        x_root.rank = x_root.rank + 1
    else:
        # The nodes were already in the same cluster
        return False
    return True


def find(x):
    """Find the root (leader) Node of a given Node x's cluster"""
    if x.parent == x:
        return x
    else:
        x.parent = find(x.parent)
        return x.parent
