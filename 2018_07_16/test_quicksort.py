import copy
import random
import unittest

from quicksort import median_of_three, quicksort


class TestQuicksort(unittest.TestCase):

    def TestBaseCases(self):
        lst = [1]
        quicksort(lst)
        self.assertEqual(lst, [1])
        lst = []
        quicksort(lst)
        self.assertEqual(lst, [])

    def TestSortSmall(self):
        lst = [1, 2, 3]
        quicksort(lst)
        self.assertEqual(lst, [1, 2, 3])
        lst = [9, 8, 7]
        quicksort(lst)
        self.assertEqual(lst, [7, 8, 9])
        lst = [6, 4, 5]
        quicksort(lst)
        self.assertEqual(lst, [4, 5, 6])

    def TestSortLarge(self):
        lst = [random.randrange(0, 100000) for i in range(0, 200000)]
        lst_copy = copy.deepcopy(lst)
        quicksort(lst)
        self.assertEqual(lst, sorted(lst_copy))

    def TestBaseCasesDeterm(self):
        lst = [1]
        quicksort(lst, choose_pivot=median_of_three)
        self.assertEqual(lst, [1])
        lst = []
        quicksort(lst, choose_pivot=median_of_three)
        self.assertEqual(lst, [])

    def TestSortSmallDeterm(self):
        lst = [1, 2, 3]
        quicksort(lst, choose_pivot=median_of_three)
        self.assertEqual(lst, [1, 2, 3])
        lst = [9, 8, 7]
        quicksort(lst, choose_pivot=median_of_three)
        self.assertEqual(lst, [7, 8, 9])
        lst = [6, 4, 5]
        quicksort(lst, choose_pivot=median_of_three)
        self.assertEqual(lst, [4, 5, 6])

    def TestSortLargeDeterm(self):
        lst = [random.randrange(0, 100000) for i in range(0, 200000)]
        lst_copy = copy.deepcopy(lst)
        quicksort(lst, choose_pivot=median_of_three)
        self.assertEqual(lst, sorted(lst_copy))
