def fibonacci(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    fib0 = 0
    fib1 = 1
    f = 1
    while n >= 2:
        f = fib0 + fib1
        fib1, fib0 = f, fib1
        n = n - 1
    return f
