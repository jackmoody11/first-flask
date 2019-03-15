from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def primes(n):
    primes = []
    for i in range(n):
        if is_prime(i):
            primes.append(i)
    return primes