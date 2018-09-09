#include <stdio.h>
#include <stdlib.h>

typedef struct ListNode {
  struct ListNode *prev;
  struct ListNode *next;
  signed long long int key;
} ListNode;

typedef struct LinkedList {
  ListNode *head;
  void (*insert)();
  int (*isInList)();
} LinkedList;

void insert(LinkedList *self, signed long long int key) {
  fprintf(stderr, "-----Inside insert------\n");
  ListNode *new;
  fprintf(stderr, "After 'ListNode *new;'\n");
  new = malloc(sizeof(ListNode));
  fprintf(stderr, "After 'new = malloc(sizeof(ListNode));'\n");
  new->prev = NULL;
  fprintf(stderr, "After 'new->prev = NULL;'\n");
  new->next = self->head;
  fprintf(stderr, "After 'new->next = self->head;'\n");
  new->key = key;
  fprintf(stderr, "After 'new->key = key;'\n");
  if (self->head) {
    self->head->prev = new;
    fprintf(stderr, "After 'self->head->prev = new;'\n");
  }
  self->head = new;
  fprintf(stderr, "After 'self->head = new;'\n");
}

int isInList(LinkedList *self, signed long long int key) {
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
  ListNode *cur;

  fprintf(stderr, "In traverseList\n");
  cur = list->head;
  while (cur) {
    fprintf(stderr, "Saw %d\n", cur->key);
    cur = cur->next;
  }
}

LinkedList *initializeLinkedList(void) {
  LinkedList *list = malloc(sizeof(LinkedList));
  list->head = NULL;
  list->insert = insert;
  list->isInList = isInList;
}

int main(void) {
  LinkedList *list;
  list = initializeLinkedList();
  list->insert(list, 1);
  fprintf(stderr, "After insert 1\n");
  list->insert(list, 2);
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

}
