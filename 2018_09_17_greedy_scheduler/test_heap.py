"""Unittests for Heap class"""

import random
import unittest

from heap import Heap


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

    def TestKeyLambda(self):
        input = [random.randrange(100) for _ in range(100)]
        h = Heap(input, key=lambda x: x * -1)
        sorted_input = sorted(input, reverse=True)
        print(sorted_input)
        for i in range(len(input)):
            self.assertEqual(h.peek_min(), sorted_input[i])
            self.assertEqual(h.extract_min(), sorted_input[i])
