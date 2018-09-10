#include <stdio.h>
#include <stdlib.h>
#include "hash_table.h"
#include "two_sum.h"

#define LOW_T_BOUND -10000 // Inclusive lower bound
#define UP_T_BOUND 10000  // Inclusive upper bound


int main(void) {
  two_sum_wrapper("two_sum_data.txt", LOW_T_BOUND, UP_T_BOUND);
  return 0;
}
