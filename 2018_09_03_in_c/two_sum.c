#include <stdio.h>
#include <stdlib.h>
#include "linked_list.h"

int main(void) {
  LinkedList *list;

  list = initializeLinkedList();
  list->insert(list, 1);
  fprintf(stderr, "After insert 1\n");
  list->insert(list, 2);
  fprintf(stderr, "After insert 2\n");
  list->insert(list, -5);
  fprintf(stderr, "After insert 2\n");
  list->insert(list, 3);
  fprintf(stderr, "After insert 3\n");
  fprintf(stderr, "~~Beginning list traversal~~\n");
  traverseList(list);
  fprintf(stderr, "~~Finished list traversal~~\n");
  if (list->isInList(list, 2)) {
    printf("2 is in the list.");
  } else {
    printf("2 is NOT in the list.");
  }
  if (list->isInList(list, 3)) {
    printf("3 is in the list.");
  } else {
    printf("3 is NOT in the list.");
  }
  if (list->isInList(list, 4)) {
    printf("4 is in the list.");
  } else {
    printf("4 is NOT in the list.");
  }
  if (list->isInList(list, -5)) {
    printf("-5 is in the list.");
  } else {
    printf("-5 is NOT in the list.");
  }

}
