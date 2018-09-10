#ifndef TWO_SUM_   /* Include guard */
#define TWO_SUM_

int two_sum(HashTable *ht, signed long long int *numbers, int numlen, int t);

int two_sum_wrapper(const char *filename, signed long int t_low_bnd,
                    signed long int t_up_bnd);

#endif // TWO_SUM_
