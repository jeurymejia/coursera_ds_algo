"""Programming exercise 2

Algorithm for counting inversions in a list in nlog(n) time
"""


def count_inversions(input_list):
    """Get count of inversions for a given list

    Wrapper around count_invs_recur - returns the inversion
    count only, not a tuple with a sorted list
    """
    return count_invs_recur(input_list)[1]  # Just the inversion count


def count_invs_recur(input_list):
    if len(input_list) <= 1:
        return input_list, 0
    else:
        l_list, l_cnt = count_invs_recur(input_list[:len(input_list) // 2])
        r_list, r_cnt = count_invs_recur(input_list[len(input_list) // 2:])
        mrg_list, split_cnt = merge_and_count_split(l_list, r_list)
        return mrg_list, l_cnt + r_cnt + split_cnt


def merge_and_count_split(left, right):
    split_cnt = 0
    merged = []
    i, j = 0, 0
    while i < len(left) or j < len(right):
        if i < len(left) and j < len(right):
            # There are unmerged elements in both lists
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                # There are n inversions, where n is equal
                # to the number of unmerged elements in the
                # left list
                split_cnt += len(left) - i
        elif i < len(left):
            # Only the left list has unmerged elements
            merged += left[i:]
            break
        else:
            # Only the right list has unmerged elemen
            merged += right[j:]
            break
    return merged, split_cnt


def main():
    with open("integer_array.txt", "r", encoding="UTF-8") as file:
        input_list = [int(num) for num in file]
        print(count_inversions(input_list))


if __name__ == "__main__":
    main()
