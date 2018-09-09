import numpy as np
from collections import deque


DEFAULT_NP_ARRAY_SZ = 2749991


class dict_wrapper(object):
    """Wrapper around Python dict"""
    def __init__(self):
        self.internal_dict = {}

    def insert(self, key, value):
        self.internal_dict[key] = value

    def lookup(self, key):
        return self.internal_dict.get(key)


class set_wrapper(object):
    """Wrapper around Python set"""
    def __init__(self):
        self.internal_set = set()

    def insert(self, key, value):
        self.internal_set.add(key)

    def lookup(self, key):
        return key in self.internal_set


class hash_table(object):
    """Custom hash table using chaining

    Implemented using numpy array and deque for lists
    """
    def __init__(self, size=DEFAULT_NP_ARRAY_SZ):
        self.size = size
        self.arr = np.full(size, fill_value=-1, dtype=int)
        self.deques = []
        self.deque_cnt = 0

    def hash(self, key):
        # Size should be a prime number not close to a power of
        # 2 or a power of 10
        return key % self.size

    def insert(self, key, value):
        i = self.hash(key)
        if self.arr[i] == -1:
            # The bucket at index is empty, so create a new chain
            # and set the value of self.arr[i] to the index of
            # the new chain within self.deques
            self.deques.append(deque([(key, value)]))
            self.arr[i] = self.deque_cnt
            self.deque_cnt += 1
        else:
            self.deques[self.arr[i]].appendleft((key, value))

    def lookup(self, key):
        i = self.hash(key)
        if self.arr[i] == -1:
            return None
        else:
            for tup_key, tup_val in self.deques[self.arr[i]]:
                if key == tup_key:
                    return tup_val
            return None
