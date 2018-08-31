"""Test driver to confirm build_heap method runs in O(n) time"""


import random
import time

from heaps import Heap

inputs = []
for x in range(1, 10):
    inputs.append([random.randrange(10000) for _ in range(x * 100000)])

for i, input in enumerate(inputs):
    start = time.time()
    Heap(input)
    ellapsed = time.time() - start
    print("Took {} seconds to build a heap from {}00,000 "
          "elements".format(ellapsed, i + 1))
