#include <stdio.h>
#include <stdlib.h>
#include "hash_table.h"
#include "two_sum.h"

#define LOW_T_BOUND -10000 // Inclusive lower bound
#define UP_T_BOUND 10000  // Inclusive upper bound


int main(int argc, char **argv) {
  if (argc < 2) {
      fprintf(stderr, "Missing arg: filepath to input data\n");
      return -1;
  }
  FILE *fp = fopen(argv[1], "r");
  if (fp == NULL) {
      perror("Failed to open file: ");
      return -1;
  }
  two_sum_wrapper(fp, LOW_T_BOUND, UP_T_BOUND);
  return 0;
}
