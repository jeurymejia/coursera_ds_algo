CC=gcc

all: two_sum test_two_sum test_hash_table test_linked_list

two_sum: main.o two_sum.o hash_table.o linked_list.o
	$(CC) main.o two_sum.o hash_table.o linked_list.o -o two_sum

test_two_sum: test_two_sum.o test_helpers.o two_sum.o hash_table.o linked_list.o
	$(CC) test_two_sum.o test_helpers.o two_sum.o hash_table.o linked_list.o -o test_two_sum

test_hash_table: test_hash_table.o test_helpers.o hash_table.o linked_list.o
	$(CC) test_hash_table.o test_helpers.o hash_table.o linked_list.o -o test_hash_table

test_linked_list: test_linked_list.o test_helpers.o linked_list.o
	$(CC) test_linked_list.o test_helpers.o linked_list.o -o test_linked_list

test_two_sum.o: test_two_sum.c
	$(CC) -c test_two_sum.c

test_hash_table.o: test_hash_table.c
	$(CC) -c test_hash_table.c

test_linked_list.o: test_linked_list.c
	$(CC) -c test_linked_list.c

main.o: main.c
	$(CC) -c main.c

test_helpers.o: test_helpers.c
	$(CC) -c test_helpers.c

two_sum.o: two_sum.c
	$(CC) -c two_sum.c

hash_table.o: hash_table.c
	$(CC) -c hash_table.c

linked_list.o: linked_list.c
	$(CC) -c linked_list.c

clean:
	rm *o two_sum test_two_sum test_hash_table test_linked_list

main: linked_list.c hash_table.c two_sum.c main.c
	$(CC) -o hellomake hellomake.o hellofunc.o
