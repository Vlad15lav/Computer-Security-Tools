import random
from classes.curve import Curve
from classes.point import Point


# Get random value for curve
def get_random_point(n):
    return Point(*[random.randint(0, n) for _ in range(2)], 1)


# Get Elliptic Curve
def get_random_curve(point, n):
    a = random.randint(0, n)
    b = (pow(point.y, 2, n) - pow(point.x, 3, n) - a * point.x) % n
    return Curve(a, b, n)