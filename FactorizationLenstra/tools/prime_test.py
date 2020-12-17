import random

# Miller Rabin test - prime number
def miller_rabin(d, n):
    a = 2 + random.randint(1, n - 4)
    x = pow(a, d, n)
    if x == 1 or x == n - 1: return True
    while d != n - 1:
        x, d = pow(x, 2, n), d * 2
        if x == 1: return False
        if x == n - 1: return True

    return False


# Check prime number
def prime_test(n):
    if n <= 1 or n == 4: return False
    if n <= 3: return True
    t = n - 1
    while not t % 2: t //= 2
    return miller_rabin(t, n)