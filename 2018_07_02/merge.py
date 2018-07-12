def mergesort(unsorted):
    if len(unsorted) == 1:
        return unsorted
    else:
        left = mergesort(unsorted[:len(unsorted)//2])
        right = mergesort(unsorted[len(unsorted)//2:])
        return merge(left, right)


def merge(list1, list2):
    i, j = 0, 0
    merged = []
    while i < len(list1) or j < len(list2):
        if i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                merged.append(list1[i])
                i += 1
            else:
                merged.append(list2[j])
                j += 1
        elif i < len(list1):
            # list2 is exhausted, so just add the rest of list1 to merged
            merged += list1[i:]
            break
        else:
            # list1 is exhausted, so just add the rest of list2 to merged
            merged += list2[j:]
            break
    return merged
