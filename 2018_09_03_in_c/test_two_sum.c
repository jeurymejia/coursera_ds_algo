#include <stdio.h>
#include <stdlib.h>
#include "hash_table.h"
#include "two_sum.h"
#include "test_helpers.h"

#define DEFAULT_HT_ARRAY_SZ 2749991
#define NUMBERS_IN_FILE 1000000


int main(void) {
  assertEquals(two_sum_wrapper("test_case_1.txt", 3, 10), 8);
  assertEquals(two_sum_wrapper("test_case_2.txt", 0, 4), 2);
  if (failCount) {
    printf("\n%d test(s) failed\n", failCount);
  } else {
    printf("\nAll tests passed\n");
  }
}
