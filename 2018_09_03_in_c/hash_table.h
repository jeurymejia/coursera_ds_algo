#ifndef HASH_TABLE_   /* Include guard */
#define HASH_TABLE_

typedef struct HashTable {
  struct LinkedList **buckets;  // Pointer to array of ListNode pointers
  long unsigned int size;
  void (*insert)();
  int (*lookup)();
  signed long int (*hash)();
} HashTable;

HashTable *initializeHashTable(unsigned long int arrSize);

#endif // HASH_TABLE_
