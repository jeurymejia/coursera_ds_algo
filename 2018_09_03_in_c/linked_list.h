#ifndef LINKED_LIST_   /* Include guard */
#define LINKED_LIST_


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

void traverseList(LinkedList *list);

LinkedList *initializeLinkedList(void);

#endif // LINKED_LIST_
