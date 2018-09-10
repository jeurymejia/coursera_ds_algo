#include <stdio.h>
#include <stdlib.h>
#include "hash_table.h"
#include "test_helpers.h"

#define DEFAULT_HT_ARRAY_SZ 2749991


int main(void) {
  HashTable *ht;

  ht = initializeHashTable(DEFAULT_HT_ARRAY_SZ);
  ht->insert(ht, -5);
  ht->insert(ht, 7);
  ht->insert(ht, 10);
  ht->insert(ht, 14);
  assertEquals(ht->lookup(ht, 10), 1);
  assertEquals(ht->lookup(ht, 7), 1);
  assertEquals(ht->lookup(ht, 14), 1);
  assertEquals(ht->lookup(ht, -5), 1);
  assertEquals(ht->lookup(ht, 0), 0);
  assertEquals(ht->lookup(ht, 5), 0);

  // Now try with tiny internal array to test chaining
  ht = initializeHashTable(10);
  for (int i=0; i<30; i++) {
    ht->insert(ht, i);
  }
  assertEquals(ht->lookup(ht, 19), 1);
  assertEquals(ht->lookup(ht, 3), 1);
  assertEquals(ht->lookup(ht, 28), 1);
  assertEquals(ht->lookup(ht, 0), 1);
  assertEquals(ht->lookup(ht, 5), 1);
  assertEquals(ht->lookup(ht, 15), 1);
  assertEquals(ht->lookup(ht, 25), 1);
  assertEquals(ht->lookup(ht, -5), 0);
  assertEquals(ht->lookup(ht, 40), 0);
  assertEquals(ht->lookup(ht, 30), 0);
  if (failCount) {
    printf("\n%d test(s) failed\n", failCount);
  } else {
    printf("\nAll tests passed\n");
  }
}
