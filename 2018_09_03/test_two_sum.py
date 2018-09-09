import unittest

from hash_tables import dict_wrapper, hash_table, set_wrapper
from two_sum import do_two_sum_over_range


class TestHeap(unittest.TestCase):

    def TestCase1(self):
        with open("test_case_1.txt", "r") as f:
            ints = [int(line) for line in f.readlines()]
        successes = do_two_sum_over_range(ints, 3, 10, dict_wrapper)
        self.assertEqual(successes, 8)
        successes = do_two_sum_over_range(ints, 3, 10, set_wrapper)
        self.assertEqual(successes, 8)
        successes = do_two_sum_over_range(ints, 3, 10, hash_table)
        self.assertEqual(successes, 8)

    def TestCase2(self):
        with open("test_case_2.txt", "r") as f:
            ints = [int(line) for line in f.readlines()]
        successes = do_two_sum_over_range(ints, 0, 4, dict_wrapper)
        self.assertEqual(successes, 2)
        successes = do_two_sum_over_range(ints, 0, 4, set_wrapper)
        self.assertEqual(successes, 2)
        successes = do_two_sum_over_range(ints, 0, 4, hash_table)
        self.assertEqual(successes, 2)
