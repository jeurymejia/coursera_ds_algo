#include <stdio.h>
#include <stdlib.h>
#include "linked_list.h"
#include "hash_table.h"


void htInsert(HashTable *self, signed long long int key) {
  signed long int i;

  i = self->hash(self, key);
  if (!self->buckets[i]) {
    self->buckets[i] = initializeLinkedList();
  }
  self->buckets[i]->insert(self->buckets[i], key);
}

int htLookup(HashTable *self, signed long long int key) {
  signed long int i;

  i = self->hash(self, key);
  if (self->buckets[i]) {
    return self->buckets[i]->isInList(self->buckets[i], key);
  }
  return 0;
}

signed long int htHash(HashTable *self, signed long long int key) {
  return key % self->size;
}

HashTable *initializeHashTable(unsigned long int arrSize) {
  HashTable *ht = malloc(sizeof(HashTable));
  ht->size = arrSize;
  ht->buckets = malloc(arrSize * sizeof(LinkedList *));
  // Initialize array to all NULLs
  for (int i=0; i<arrSize; i++) {
    ht->buckets[i] = NULL;
  }

  ht->insert = htInsert;
  ht->lookup = htLookup;
  ht->hash = htHash;
}
