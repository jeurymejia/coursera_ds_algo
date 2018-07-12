import math


def pad_numbers(x, y):
    """Left pad two string representations of integers with 0s

    x and y will be left-padded with 0 characters such:
    - x and y will have a total length n
    - n is a power of 2
    """
    n = max(len(x), len(y))  # The larger of the two lengths
    n = 2 ** math.ceil(math.log(n, 2))  # Round n to the next power of 2
    x = '0' * (n - len(x)) + x
    y = '0' * (n - len(y)) + y
    return x, y


def split_in_two(x):
    """Split a n-char string into two n/2-char halves

    Assumes n is an even number
    """
    midpoint = len(x) // 2
    return x[:midpoint], x[midpoint:]


def karatsuba(x, y):
    """Perform katasuba multiplication on two numbers

    Input: Two n-digit postive integers, represented as strings
    Output: The product x * y, as a string
    """
    x, y = pad_numbers(x, y)  # Left pad numbers with 0s
    if len(x) == 1:
        return str(int(x) * int(y))
    else:
        n = len(x)
        a, b = split_in_two(x)
        c, d = split_in_two(y)
        p = str(int(a) + int(b))
        q = str(int(c) + int(d))
        ac, bd, pq = karatsuba(a, c), karatsuba(b, d), karatsuba(p, q)
        adbc = str(int(pq) - int(ac) - int(bd))
        ac += '0' * n
        adbc += '0' * (n // 2)
        return str(int(ac) + int(adbc) + int(bd))
