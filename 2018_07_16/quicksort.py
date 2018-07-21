import copy
import random


def get_random_pivot(lst, begin, end):
    """Default pivot selection strategy"""
    return random.randrange(begin, end)


def quicksort(lst, choose_pivot=get_random_pivot):
    """Wrapper around quicksort_recur.


    lst: The list to be sorted in place
    choose_pivot: The function used to choose the pivot element. Takes
        three arguments: lst, begin, end

    Returns the total number of comparisons required to sort the list,
    not including comparisons made within the choose_pivot function
    """
    return quicksort_recur(lst, 0, len(lst), choose_pivot)


def quicksort_recur(lst, begin, end, choose_pivot):
    """Sort a list in place

    lst: The entire list (rather than list segment this occurance
        of quicksort is to sort).  For the first occurance of
        quicksort_recur, len(lst) == end (that is, the entire list
        is the list to be sorted)
    begin: The first index of the list segment to be sorted
    end: The index beyond the last element of the list segment
        to be sorted
    choose_pivot: The function used to choose the pivot element.  Takes
        three arguments: lst, begin, end
    """
    comparisons = 0

    if end - begin <= 1:
        return comparisons

    pivot_idx = choose_pivot(lst, begin, end)
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
    comparisons += quicksort_recur(lst, begin, j-1, choose_pivot)
    comparisons += len(lst[begin:j-1])
    comparisons += quicksort_recur(lst, j, end, choose_pivot)
    comparisons += len(lst[j:end])
    return comparisons


def median_of_three(lst, begin, end):
    """Alternate strategy for selecting pivot index

    The index of the median element among the first, last,
    and middle elements in the lst segment is returned
    """
    first = lst[begin]
    final = lst[end - 1]
    middle = lst[(((end - begin) - 1) // 2) + begin]
    if first <= middle <= final or final <= middle <= first:
        return (((end - begin) - 1) // 2) + begin
    elif middle <= first <= final or final <= first <= middle:
        return begin
    else:
        return end - 1


def main():
    """Test driver: sort 10,000 unique integers and print
    number of comparisons required using four different
    pivot selection strategies
    """

    with open("input.txt", "r", encoding="UTF-8") as file:
        lst = [int(line) for line in file.readlines()]

    # Use first element in lst segment as pivot
    print(quicksort(copy.deepcopy(lst),
                    choose_pivot=lambda lst, begin, end: begin))

    # Use last element in lst segment as pivot
    print(quicksort(copy.deepcopy(lst),
                    choose_pivot=lambda lst, begin, end: end - 1))

    # Use median of first, last, and middle elements as pivot
    print(quicksort(copy.deepcopy(lst),
                    choose_pivot=median_of_three))

    # Use random pivot
    print(quicksort(copy.deepcopy(lst)))


if __name__ == "__main__":
    main()
