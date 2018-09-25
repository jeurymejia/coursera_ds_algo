"""Unittests for NodeHeap class"""

import random
import unittest

from node_heap import NodeHeap
from prims import Node


class TestHeap(unittest.TestCase):

    def TestMinHeapProperty(self):
        input = [
            Node(label=0, edges=[], min_cost_edge=6),
            Node(label=1, edges=[], min_cost_edge=1),
            Node(label=2, edges=[], min_cost_edge=4),
            Node(label=3, edges=[], min_cost_edge=5),
            Node(label=4, edges=[], min_cost_edge=3),
            Node(label=5, edges=[], min_cost_edge=2),
        ]
        h = NodeHeap()
        for node in input:
            h.insert(node)
        self.assertEqual(h.extract_min().min_cost_edge, 1)

    def TestSizeReducedAfterExtractMin(self):
        input = [
            Node(label=0, edges=[], min_cost_edge=6),
            Node(label=1, edges=[], min_cost_edge=1),
            Node(label=2, edges=[], min_cost_edge=4),
            Node(label=3, edges=[], min_cost_edge=5),
            Node(label=4, edges=[], min_cost_edge=3),
            Node(label=5, edges=[], min_cost_edge=2),
        ]
        h = NodeHeap()
        for num in input:
            h.insert(num)
        initial_size = h.size
        self.assertEqual(initial_size, len(h.a))
        h.extract_min()
        self.assertEqual(initial_size - 1, h.size)

    def TestMinHeapWithRandomInput(self):
        input = [
            Node(label=i, edges=[], min_cost_edge=random.randrange(100))
            for i, _ in enumerate(range(5000))
        ]
        h = NodeHeap()
        for num in input:
            h.insert(num)
        sorted_input = sorted(input, key=lambda x: x.min_cost_edge)
        for i in range(len(input)):
            self.assertEqual(h.extract_min().min_cost_edge,
                             sorted_input[i].min_cost_edge)

    def TestBuildMinHeap(self):
        input = [
            Node(label=i, edges=[], min_cost_edge=random.randrange(100))
            for i, _ in enumerate(range(5000))
        ]
        h = NodeHeap(input)
        sorted_input = sorted(input, key=lambda x: x.min_cost_edge)
        for i in range(len(input)):
            print(h.m)
            self.assertEqual(h.peek_min().min_cost_edge,
                             sorted_input[i].min_cost_edge)
            self.assertEqual(h.extract_min().min_cost_edge,
                             sorted_input[i].min_cost_edge)

    def TestDelete(self):
        input = [
            Node(label=i, edges=[], min_cost_edge=random.randrange(100))
            for i, _ in enumerate(range(10000))
        ]
        h = NodeHeap()
        for num in input:
            h.insert(num)
        for _ in range(100):
            to_delete = input.pop(random.randrange(len(input)))
            deleted = h.delete(to_delete.label)
            self.assertEqual(to_delete, deleted)
        sorted_input = sorted(input, key=lambda x: x.min_cost_edge)
        for i in range(len(input)):
            self.assertEqual(h.peek_min().min_cost_edge,
                             sorted_input[i].min_cost_edge)
            self.assertEqual(h.extract_min().min_cost_edge,
                             sorted_input[i].min_cost_edge)

    def TestDeleteWithBuildHeap(self):
        input = [
            Node(label=i, edges=[], min_cost_edge=random.randrange(100))
            for i, _ in enumerate(range(10000))
        ]
        h = NodeHeap(input)
        for _ in range(100):
            to_delete = input.pop(random.randrange(len(input)))
            deleted = h.delete(to_delete.label)
            self.assertEqual(to_delete, deleted)
        sorted_input = sorted(input, key=lambda x: x.min_cost_edge)
        for i in range(len(input)):
            self.assertEqual(h.peek_min().min_cost_edge,
                             sorted_input[i].min_cost_edge)
            self.assertEqual(h.extract_min().min_cost_edge,
                             sorted_input[i].min_cost_edge)
