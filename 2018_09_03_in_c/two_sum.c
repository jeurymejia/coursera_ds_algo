#include <stdio.h>
#include <stdlib.h>
#include "hash_table.h"
#include "two_sum.h"

#define DEFAULT_HT_ARRAY_SZ 2749991
#define MAX_NUMBERS_IN_FILE 1000000


int two_sum(HashTable *ht, signed long long int *numbers,
            int numlen, int t) {
  /* 2-sum algorithm
   *
   * Given a set of integers ints and an integer t, return True if
   * there exist distinct elements x and y in ints such that x + y == t
   *
   * Runs in O(n) time - relies on hash table for O(1) lookups
   */
  signed long long int x, y;
  for (int i=0; i<numlen; i++) {
    x = numbers[i];
    y = t - x;
    if (x != y) {
      if (ht->lookup(ht, y)) {
        printf("Found two-sum for %d (x=%lld, y=%lld)\n", t, x, y);
        return 1;
      }
    }
  }
  return 0;
}

int two_sum_wrapper(const char *filename, signed long int t_low_bnd,
                    signed long int t_up_bnd) {
  FILE *fp = fopen(filename, "r");
  signed long long int numbers[MAX_NUMBERS_IN_FILE];
  signed long long int n = 0;
  int i = 0;
  int lineCount = 0;
  while (fscanf(fp, "%lld,", &n) > 0) {
    numbers[i++] = n;
    lineCount++;
  }

  HashTable *ht = initializeHashTable(DEFAULT_HT_ARRAY_SZ);
  for (i=0; i<lineCount; i++) {
    ht->insert(ht, numbers[i]);
  }

  unsigned int successes = 0;
  for (i=t_low_bnd; i<t_up_bnd+1; i++) {
    if (two_sum(ht, numbers, lineCount, i)) {
      successes++;
    } else {
      fprintf(stderr, "Couldn't find two-sum for %d\n", i);
    }
  }
  fprintf(stderr, "Found two-sums for %d numbers\n", successes);
  return successes;
}
