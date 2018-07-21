import random


def quicksort(lst):
    """Wrapper around quicksort_recur"""
    return quicksort_recur(lst, 0, len(lst))


def quicksort_recur(lst, begin, end):
    """Sort a list in place

    lst: The entire list (rather than list segment this occurance
        of quicksort is to sort).  For the first occurance of
        quicksort_recur, len(lst) == end (that is, the entire list
        is the list to be sorted)
    begin: The first index of the list segment to be sorted
    end: The index beyond the last element of the list segment
        to be sorted
    """
    if end - begin <= 1:
        return lst

    pivot_idx = random.randrange(begin, end)
    pivot_val = lst[pivot_idx]

    # Move pivot element to front of lst segment
    lst[begin], lst[pivot_idx] = lst[pivot_idx], lst[begin]

    # Partition lst segment in terms of size relative to pivot_val
    j = begin + 1
    for i in range(begin + 1, end):
        if lst[i] < pivot_val:
            lst[i], lst[j] = lst[j], lst[i]
            j += 1
        i += 1
    # Move pivot element between elements larger than / smaller than it
    lst[begin], lst[j-1] = lst[j-1], lst[begin]

    # Recursively call quicksort on the partitioned sections
    quicksort_recur(lst, begin, j-1)
    quicksort_recur(lst, j, end)
    return lst
