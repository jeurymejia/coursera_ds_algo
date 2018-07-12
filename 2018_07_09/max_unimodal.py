"""Week 2 - Optional Theory Problem 2

Given a unimodal array of n *unique* elements, find the maximum
element in O(log n) time
"""


def get_max(lst):
    """Divide and conquer algorithm for getting the maximum
    element in a unimodal list of unique numbers
    """
    length = len(lst)
    if length == 0:
        return None
    if length == 1:
        return lst[0]
    if length == 2:
        if lst[0] > lst[1]:
            return lst[0]
        else:
            return lst[1]
    else:
        mid_idx = length // 2
        if lst[mid_idx - 1] < lst[mid_idx] and lst[mid_idx + 1] < lst[mid_idx]:
            # We've stumbled across the maximum
            return lst[mid_idx]
        elif lst[mid_idx - 1] > lst[mid_idx]:
            # The max is in the left half of the array
            return get_max(lst[:mid_idx])
        else:
            # The max is in the right half
            return get_max(lst[mid_idx:])
