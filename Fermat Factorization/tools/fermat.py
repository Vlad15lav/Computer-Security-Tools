import math

def factorization(n: int) -> [int, int]:
    x = math.ceil(math.sqrt(n))
    q_x = x ** 2 - n
    while not math.sqrt(q_x).is_integer():
        x += 1
        q_x = x ** 2 - n
    return int(x + math.sqrt(q_x)), int(x - math.sqrt(q_x))