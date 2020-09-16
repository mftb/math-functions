# iterative approach
def factorial(n):
    fact = 1
    if n > 1:
        while n >= 2:
            fact = fact * n
            n = n - 1
    return fact
