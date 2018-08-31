"""Tests for median maintenance algorithm"""


import unittest

from median_maintenance import calculate_medians


class TestHeap(unittest.TestCase):

    def TestCase1(self):
        with open("test_case_1.txt", "r") as f:
            numbers = f.readlines()

        numbers = [int(line.strip()) for line in numbers]
        self.assertEqual(calculate_medians(numbers), 142)

    def TestCase2(self):
        with open("test_case_2.txt", "r") as f:
            numbers = f.readlines()

        numbers = [int(line.strip()) for line in numbers]
        self.assertEqual(calculate_medians(numbers), 9335)
