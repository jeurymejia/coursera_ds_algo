#include <stdio.h>
#include <stdlib.h>
#include "hash_table.h"
#include "two_sum.h"
#include "test_helpers.h"

#define DEFAULT_HT_ARRAY_SZ 2749991
#define NUMBERS_IN_FILE 1000000


int main(void) {
  FILE *fp = fopen("test_case_1.txt", "r");
  assertEquals(two_sum_wrapper(fp, 3, 10), 8);
  fp = fopen("test_case_2.txt", "r");
  assertEquals(two_sum_wrapper(fp, 0, 4), 2);
  if (failCount) {
    printf("\n%d test(s) failed\n", failCount);
  } else {
    printf("\nAll tests passed\n");
  }
}
