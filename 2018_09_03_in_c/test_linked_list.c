#include <stdio.h>
#include <stdlib.h>
#include "linked_list.h"
#include "test_helpers.h"


int main(void) {
  LinkedList *list;

  list = initializeLinkedList();
  list->insert(list, -5);
  list->insert(list, 7);
  list->insert(list, 10);
  list->insert(list, 14);
  assertEquals(list->isInList(list, 10), 1);
  assertEquals(list->isInList(list, 7), 1);
  assertEquals(list->isInList(list, 14), 1);
  assertEquals(list->isInList(list, -5), 1);
  assertEquals(list->isInList(list, 0), 0);
  assertEquals(list->isInList(list, 5), 0);
  if (failCount) {
    printf("\n%d test(s) failed\n", failCount);
  } else {
    printf("\nAll tests passed\n");
  }
}
