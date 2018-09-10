#include <stdio.h>
#include <stdlib.h>
#include "test_helpers.h"


void assertEquals(int expr1, int expr2) {
  if (expr1 == expr2) {
    printf(".");
  } else {
    printf("X");
    failCount++;
  }
}
