"""Week 2 - Optional Theory Problem 3

Given a sorted array of *distinct* numbers, return True
if there exists an element A[i] such that A[i] == i

Runs in O(log n) time
"""


def match_index(sorted):
    """Wrapper around match_index_recur"""
    return match_index_recur(sorted, 0)


def match_index_recur(sorted, offset):
    if len(sorted) == 0:
        return False
    if len(sorted) == 1:
        return sorted[0] == offset

    mid_idx = len(sorted) // 2
    midpoint = sorted[mid_idx]
    if midpoint == mid_idx + offset:
        # The midpoint satisfies A[i] == i
        return True
    elif midpoint < mid_idx + offset:
        # A[i] == i, if it exists, is to the right of the
        # current midponint
        return match_index_recur(sorted[mid_idx:], mid_idx + offset)
    else:
        # A[i] == i, if it exists, is to the left
        return match_index_recur(sorted[:mid_idx], offset)
