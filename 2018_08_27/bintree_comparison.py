"""
Comparison of how quickly heap-based implementation of
median maintenance algorithm runs versus an implementation
using red black trees
"""

import random
import time

from bintrees import RBTree

from heaps import Heap as MinHeap, MaxHeap


def main():
    with open("Median.txt", "r") as f:
        numbers = f.readlines()

    numbers = [int(line.strip()) for line in numbers]
    start = time.time()
    calculate_medians_with_heaps(numbers)
    delta = time.time() - start
    print("Took {} seconds to run calculate_medians_with_heaps".format(delta))
    start = time.time()
    calculate_medians_with_rbt(numbers)
    delta = time.time() - start
    print("Took {} seconds to run calculate_medians_with_rbt".format(delta))

    print("\nWith randomized input:")
    numbers = [random.randrange(10000) for _ in range(10000)]
    start = time.time()
    calculate_medians_with_heaps(numbers)
    delta = time.time() - start
    print("Took {} seconds to run calculate_medians_with_heaps".format(delta))
    start = time.time()
    calculate_medians_with_rbt(numbers)
    delta = time.time() - start
    print("Took {} seconds to run calculate_medians_with_rbt".format(delta))


def calculate_medians_with_heaps(numbers):
    """Calculate the sum of all 10,000 medians, modulo 10000"""
    max_heap = MaxHeap()  # For storing the smaller half of numbers
    min_heap = MinHeap()  # For storing the larger half of numbers
    medians = []
    for number in numbers:
        if max_heap.peek_max() is None or max_heap.peek_max() > number:
            max_heap.insert(number)
            if max_heap.size > min_heap.size + 1:
                min_heap.insert(max_heap.extract_max())
        else:
            min_heap.insert(number)
            if min_heap.size > max_heap.size + 1:
                max_heap.insert(min_heap.extract_min())
        if max_heap.size >= min_heap.size:
            medians.append(max_heap.peek_max())
        else:
            medians.append(min_heap.peek_min())
    return medians


def calculate_medians_with_rbt(numbers):
    """Calculate the sum of all 10,000 medians, modulo 10000"""
    smaller = RBTree()  # For storing the smaller half of numbers
    larger = RBTree()  # For storing the larger half of numbers
    medians = []
    for number in numbers:
        if not len(smaller) or smaller.max_item()[0] > number:
            smaller.insert(number, None)
            if len(smaller) > len(larger) + 1:
                larger.insert(smaller.max_item()[0], None)
        else:
            larger.insert(number, None)
            if len(larger) > len(smaller) + 1:
                smaller.insert(larger.min_item()[0], None)
        if len(smaller) >= len(larger):
            medians.append(smaller.max_item()[0])
        else:
            medians.append(larger.min_item()[0])
    return medians


if __name__ == "__main__":
    main()
