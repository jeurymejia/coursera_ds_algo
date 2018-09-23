"""Implementations of a Min Heap and a Max Heap"""


class Heap(object):
    """A Min Heap"""

    def __init__(self, input_list=None, key=lambda x: x):
        self.a = [] if input_list is None else input_list
        self.key = key
        self.build_heap()

    def __repr__(self):
        return "Heap({})".format(self.a)

    def build_heap(self):
        for i in reversed(range(self.size // 2)):
            self._sift_down(i)

    def insert(self, val):
        self.a.append(val)
        new_i = self._last_i
        self._sift_up(new_i)

    def peek_min(self):
        try:
            return self.a[0]
        except IndexError:
            return None

    def extract_min(self):
        min = self.a[0]
        try:
            leaf = self.a.pop()
            try:
                self.a[0] = leaf
            except IndexError:
                # leaf was last element in the heap
                return leaf
        except IndexError:
            return None
        self._sift_down(0)
        return min

    @property
    def size(self):
        return len(self.a)

    def _sift_up(self, i):
        parent_i = (i - 1) // 2
        if parent_i >= 0:
            if self.key(self.a[parent_i]) > self.key(self.a[i]):
                self.a[parent_i], self.a[i] = self.a[i], self.a[parent_i]
                self._sift_up(parent_i)

    def _sift_down(self, i):
        lc_i = ((i + 1) * 2) - 1  # Left child index
        rc_i = (i + 1) * 2  # Right child index
        if lc_i <= self._last_i:
            # The element at index i has at least a left child
            if rc_i <= self._last_i:
                # The element at index i has two children
                if self.key(self.a[lc_i]) < self.key(self.a[rc_i]):
                    small_c_i = lc_i
                else:
                    small_c_i = rc_i
            else:
                # Since there's only a left child, it's the smallest child
                small_c_i = lc_i
            if self.key(self.a[i]) > self.key(self.a[small_c_i]):
                self.a[small_c_i], self.a[i] = self.a[i], self.a[small_c_i]
                self._sift_down(small_c_i)

    @property
    def _last_i(self):
        return self.size - 1


class MaxHeap(Heap):
    """A Max Heap

    Turns Heap into a max heap by multiplying each key by -1
    on insert

    Keys are also multiplied by -1 on extraction
    """

    def __init__(self, input_list=None, key=lambda x: x):
        self.a = [] if input_list is None else input_list
        self.key = lambda x: key(x) * -1
        self.build_heap()

    def extract_max(self):
        return self.extract_min()

    def peek_max(self):
        try:
            return self.a[0]
        except IndexError:
            return None
