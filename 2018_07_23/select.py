import math
import random
import time


def rselect(lst, k):
    """Wrapper around select() - causes select to run as
    RANDOMIZED selection algorithm that runs in O(n) time
    """
    def random_pivot(lst, begin, end):
        return random.randrange(begin, end)

    return select(lst, 0, len(lst), k, random_pivot)


def dselect(lst, k):
    """Wrapper around select() - causes select to run as
    DETERMINISTIC selection algorithm that runs in O(n) time
    """
    def median_idx(lst):
        if len(lst) % 2:
            # lst has an odd number of elements
            return len(lst) // 2
        else:
            return max((len(lst) - 1) // 2, 0)

    def deterministic_pivot(lst_seg, begin, end):
        if lst_seg and not isinstance(lst_seg[0], tuple):
            lst_seg = [(x, lst_seg[x]) for x in range(begin, end)]
        seg_length = len(lst_seg)
        if seg_length < 6:
            lst_seg = sorted(lst_seg, key=lambda x: x[1])
            return lst_seg[median_idx(lst_seg)][0]
        else:
            groups_of_5 = [
                sorted(lst_seg[x*5: x*5 + 5], key=lambda x: x[1])
                for x in range(math.ceil(seg_length / 5))
            ]
            medians = [
                group[median_idx(group)]
                for group in groups_of_5
            ]
            return deterministic_pivot(medians, 0, len(medians))

    return select(lst, 0, len(lst), k, deterministic_pivot)


def select(lst, begin, end, k, pivot_strategy):
    """Return the kth smallest element in a list

    Pivot selection can either be randomized or
    deterministic based on the function passed as
    pivot strategy

    Note: k starts at 0 for the smallest element
    """
    if not begin <= k < end:
        raise ValueError("k out of bounds - begin: {} | k: {}"
                         "| end: {}".format(begin, k, end))

    if end - begin <= 1:
        return lst[begin]

    pivot_idx = pivot_strategy(lst, begin, end)
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

    if k == j - 1:
        # The pivot is the k smallest element, so return it
        return lst[j-1]
    elif k < j - 1:
        # k-smallest element is to the left of pivot
        return select(lst, begin, j-1, k, pivot_strategy)
    else:
        # k-smallest element is to the right of pivot
        return select(lst, j, end, k, pivot_strategy)


def main():
    ARRAY_SIZE = 100000
    test_cnt = 0
    rselect_total_time = 0
    dselect_total_time = 0
    while True:
        lst = [random.randrange(ARRAY_SIZE) for x in range(ARRAY_SIZE)]
        k = random.randrange(ARRAY_SIZE)
        start = time.time()
        rselect_result = rselect(lst, k)
        rselect_time = time.time() - start

        start = time.time()
        dselect_result = dselect(lst, k)
        dselect_time = time.time() - start

        print("rselect found the {}th smallest element to be {} "
              "in {} seconds".format(k, rselect_result, rselect_time))
        print("dselect found the {}th smallest element to be {} "
              "in {} seconds".format(k, dselect_result, dselect_time))
        print("rselect ran in {:.0%} the time of dselect".format(
            rselect_time / dselect_time))

        test_cnt += 1
        rselect_total_time += rselect_time
        dselect_total_time += dselect_time

        print("Average times:\nrselect: {}\ndselect: {}\n"
              "In total, rselect has run in {:.0%} the time of "
              "dselect".format(rselect_total_time / test_cnt,
                               dselect_total_time / test_cnt,
                               rselect_total_time / dselect_total_time))


if __name__ == "__main__":
    main()
