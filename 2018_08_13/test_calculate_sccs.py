import unittest

from calculate_sccs import build_graph, kosaraju


class TestScc(unittest.TestCase):

    def TestCase1(self):
        g = build_graph("test_case_1.txt")
        self.assertEqual([3, 3, 3], kosaraju(g))

    def TestCase2(self):
        g = build_graph("test_case_2.txt")
        self.assertEqual([3, 3, 2], kosaraju(g))

    def TestCase3(self):
        g = build_graph("test_case_3.txt")
        self.assertEqual([3, 3, 1, 1], kosaraju(g))

    def TestCase4(self):
        g = build_graph("test_case_4.txt")
        self.assertEqual([7, 1], kosaraju(g))

    def TestCase5(self):
        g = build_graph("test_case_5.txt")
        self.assertEqual([6, 3, 2, 1], kosaraju(g))
