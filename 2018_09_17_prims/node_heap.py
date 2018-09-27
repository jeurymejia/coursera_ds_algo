import copy


class NodeHeap(object):
    """A Min Heap that supports deletions

    Attributes:
        a: The underlying array containing the nodes in the heap
        m: Mapping between node labels and their position within the array
        key: Function to be called on heap elements to determine
            comparative order

    """

    def __init__(self, input_list=None, key=lambda node: node.min_cost_edge):
        self.a = [] if input_list is None else copy.copy(input_list)
        if self.a:
            self.m = {node.label: i for i, node in enumerate(self.a)}
        else:
            self.m = {}
        self.key = key
        self.build_heap()

    def __repr__(self):
        return "Heap({})".format(self.a)

    def build_heap(self):
        for i in reversed(range(self.size // 2)):
            self._sift_down(i)
        for i, node in enumerate(self.a):
            self.m[node.label] = i

    def insert(self, val):
        self.a.append(val)
        new_i = self._last_i
        self.m[val.label] = new_i
        self._sift_up(new_i)

    def peek_min(self):
        try:
            return self.a[0]
        except IndexError:
            return None

    def extract_min(self):
        min = self.a[0]
        self.m.pop(min.label)
        try:
            leaf = self.a.pop()
            try:
                self.a[0] = leaf
                self.m[leaf.label] = 0
            except IndexError:
                # leaf was last element in the heap
                return leaf
        except IndexError:
            return None
        self._sift_down(0)
        return min

    def delete(self, label):
        try:
            index = self.m.pop(label)
        except KeyError:
            raise ValueError("No node with label {} in heap".format(label))

        if index == self._last_i:
            # This node is the last in the heap, so just remove it from array
            deleted_node = self.a.pop()
        else:
            # Pop last leaf and move to deleted node's location
            deleted_node = self.a[index]
            leaf = self.a.pop()
            self.m[leaf.label] = index
            self.a[index] = leaf

            # Depending on value of leaf, we need to sift it up or down
            parent_i = (index - 1) // 2

            if self.key(leaf) > self.key(self.a[parent_i]):
                # If leaf > parent, sift down
                self._sift_down(index)
            else:
                # If leaf <= parent, sift up
                self._sift_up(index)
        return deleted_node

    @property
    def size(self):
        return len(self.a)

    @property
    def _last_i(self):
        return self.size - 1

    def _sift_up(self, i):
        parent_i = (i - 1) // 2
        if parent_i >= 0:
            if self.key(self.a[parent_i]) > self.key(self.a[i]):
                # Update map
                parent = self.a[parent_i].label  # Parent label
                child = self.a[i].label  # Child label
                self.m[parent], self.m[child] = self.m[child], self.m[parent]
                # Update array
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
                # Update map
                parent = self.a[i].label  # Parent label
                child = self.a[small_c_i].label  # Child label
                self.m[parent], self.m[child] = self.m[child], self.m[parent]
                # Update array
                self.a[small_c_i], self.a[i] = self.a[i], self.a[small_c_i]
                self._sift_down(small_c_i)
