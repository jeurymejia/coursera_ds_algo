from hash_tables import dict_wrapper, hash_table, set_wrapper


def two_sum(ints, t, populated_hash_table):
    """2-sum algorithm.

    Given a set of integers ints and an integer t, return True if
    there exist distinct elements x and y in ints such that x + y == t
    """
    for x in ints:
        y = t - x
        if y != x and populated_hash_table.lookup(y) is True:
            return True
    return False


def do_two_sum_over_range(ints, begin_incl, end_incl, hash_table_class):
    """Return the number of times the two-sum algorithm succeeds
    for a given set of integers and a range of possible t values
    """
    populated_hash_table = hash_table_class()
    for integer in ints:
        populated_hash_table.insert(integer, True)

    successes = 0
    for t in range(begin_incl, end_incl + 1):
        if two_sum(ints, t, populated_hash_table):
            print("Found two-sum for {}".format(t))
            successes += 1
        else:
            print("Couldn't find two-sum for {}".format(t))
    return successes


def main():
    with open("two_sum_data.txt", "r") as file:
        ints = [int(line) for line in file.readlines()]
    result = do_two_sum_over_range(ints, -10000, 10000, set_wrapper)
    print("Result: {}".format(result))
    return result


if __name__ == "__main__":
    main()
