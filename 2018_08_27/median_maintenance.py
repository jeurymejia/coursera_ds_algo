"""Given a stream of 10,000 numbers, compute the median
among the numbers seen so far
"""


from heaps import Heap as MinHeap, MaxHeap


def main():
    with open("Median.txt", "r") as f:
        numbers = f.readlines()

    numbers = [int(line.strip()) for line in numbers]
    print(calculate_medians(numbers))


def calculate_medians(numbers):
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
    return sum(medians) % 10000


if __name__ == "__main__":
    main()
