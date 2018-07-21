import copy
import random
import unittest

from quicksort import quicksort


class TestQuicksort(unittest.TestCase):

    def TestBaseCases(self):
        self.assertEqual(quicksort([1]), [1])
        self.assertEqual(quicksort([]), [])

    def TestSortSmall(self):
        self.assertEqual(quicksort([1, 2, 3]), [1, 2, 3])
        self.assertEqual(quicksort([9, 8, 7]), [7, 8, 9])
        self.assertEqual(quicksort([6, 4, 5]), [4, 5, 6])

    def TestSortLarge(self):
        lst = [random.randrange(0, 100) for i in range(0, 200)]
        lst_copy = copy.deepcopy(lst)
        self.assertEqual(quicksort(lst), sorted(lst_copy))
