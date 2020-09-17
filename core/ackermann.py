import sys


sys.setrecursionlimit(1000000)


# naive recursive solution
def ackermann_naive(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann_naive(m - 1, 1)
    else:
        return ackermann_naive(m - 1, ackermann_naive(m, n - 1))


# memoized solution with more recursive base cases
def ackermann(m, n, cache={0: {0: 0, 1: 2}, 1: {0: 2, 1: 3}}):
    if m in cache and n in cache[m]:
        return cache[m][n]
    else:
        result = 0
        if m == 0:
            result = n + 1
        elif m == 1:
            result = n + 2
        elif m == 2:
            result = 2 * n + 3
        elif m == 3:
            result = 2 ** (n + 3) - 3
        elif m > 3 and n == 0:
            result = ackermann(m - 1, 1, cache)
        else:
            result = ackermann(m - 1, ackermann(m, n - 1, cache), cache)
        if m not in cache:
            cache[m] = {}
        cache[m][n] = result
    return result
