#include <stdio.h>
#include <stdlib.h>
#include "linked_list.h"

void llInsert(LinkedList *self, signed long long int key) {
  ListNode *new;

  new = malloc(sizeof(ListNode));
  new->prev = NULL;
  new->next = self->head;
  new->key = key;
  if (self->head) {
    self->head->prev = new;
  }
  self->head = new;
}

int llIsInList(LinkedList *self, signed long long int key) {
  ListNode *cur;

  cur = self->head;
  while (cur) {
    if (cur->key == key){
      return 1;
    }
    cur = cur->next;
  }
  return 0;
}

void traverseList(LinkedList *list){
  /* For debugging only */
  ListNode *cur;

  cur = list->head;
  while (cur) {
    fprintf(stderr, "Saw %lld\n", cur->key);
    cur = cur->next;
  }
}

LinkedList *initializeLinkedList(void) {
  LinkedList *list = malloc(sizeof(LinkedList));
  list->head = NULL;
  list->insert = llInsert;
  list->isInList = llIsInList;
  return list;
}
