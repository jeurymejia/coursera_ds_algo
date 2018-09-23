"""Unittests for Heap class"""


import random
import unittest

from heaps import Heap, MaxHeap


class TestHeap(unittest.TestCase):

    def TestMinHeapProperty(self):
        input = [6, 1, 4, 5, 3, 2]
        h = Heap()
        for num in input:
            h.insert(num)
        self.assertEqual(h.extract_min(), 1)

    def TestSizeReducedAfterExtractMin(self):
        input = [6, 1, 4, 5, 3, 2]
        h = Heap()
        for num in input:
            h.insert(num)
        initial_size = h.size
        self.assertEqual(initial_size, len(h.a))
        h.extract_min()
        self.assertEqual(initial_size - 1, h.size)

    def TestMinHeapWithRandomInput(self):
        input = [random.randrange(100) for _ in range(100)]
        h = Heap()
        for num in input:
            h.insert(num)
        sorted_input = sorted(input)
        for i in range(len(input)):
            self.assertEqual(h.extract_min(), sorted_input[i])

    def TestBuildMinHeap(self):
        input = [random.randrange(100) for _ in range(100)]
        h = Heap(input)
        sorted_input = sorted(input)
        for i in range(len(input)):
            self.assertEqual(h.peek_min(), sorted_input[i])
            self.assertEqual(h.extract_min(), sorted_input[i])

    def TestMaxHeapProperty(self):
        input = [6, 1, 4, 5, 3, 2]
        h = MaxHeap()
        for num in input:
            h.insert(num)
        self.assertEqual(h.extract_max(), 6)

    def TestSizeReducedAfterExtractMax(self):
        input = [6, 1, 4, 5, 3, 2]
        h = MaxHeap()
        for num in input:
            h.insert(num)
        initial_size = h.size
        self.assertEqual(initial_size, len(h.a))
        h.extract_max()
        self.assertEqual(initial_size - 1, h.size)

    def TestMaxHeapWithRandomInput(self):
        input = [random.randrange(100) for _ in range(100)]
        h = MaxHeap()
        for num in input:
            h.insert(num)
        sorted_input = sorted(input)
        for i in reversed(range(len(input))):
            self.assertEqual(h.extract_max(), sorted_input[i])

    def TestBuildMaxHeap(self):
        input = [random.randrange(100) for _ in range(100)]
        h = MaxHeap(input)
        sorted_input = sorted(input)
        for i in reversed(range(len(input))):
            self.assertEqual(h.peek_max(), sorted_input[i])
            self.assertEqual(h.extract_max(), sorted_input[i])

    def TestMinHeapWithTuples(self):
        input = [(random.randrange(100), "Hullo!") for _ in range(100)]
        h = Heap(key=lambda x: x[0])
        for num in input:
            h.insert(num)
        sorted_input = sorted(input)
        for i in range(len(input)):
            self.assertEqual(h.extract_min(), sorted_input[i])
