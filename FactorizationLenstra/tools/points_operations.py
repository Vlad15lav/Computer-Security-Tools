import math
from classes.point import Point
from tools.prime_test import prime_test


# 2P operation
def doubling(point, curve):
    if point.y != 0 and point.z != 0:
        a = curve.a * pow(point.z, 2, curve.n) + 3 * pow(point.x, 2, curve.n)
        b = point.y * point.z
        c = point.x * point.y * b
        h = pow(a, 2, curve.n) - 8 * c

        x2 = (2 * h * b) % curve.n
        y2 = (a * (4 * c - h) - 8 * pow(point.y, 2, curve.n) * pow(b, 2, curve.n)) % curve.n
        z2 = pow(2 * b, 3, curve.n)

        return Point(x2, y2, z2)
    else:
        return Point(0, 1, 0) if not point.y else point


# Сложение точек P + Q
def add(point_1, point_2, curve):
    if point_1.z == 0: return point_2
    if point_2.z == 0: return point_1

    a1 = point_2.y * point_1.z % curve.n
    a2 = point_1.y * point_2.z % curve.n
    b1 = point_2.x * point_1.z % curve.n
    b2 = point_1.x * point_2.z % curve.n

    if b1 != b2:
        b = (b1 - b2) % curve.n
        a = (a1 - a2) % curve.n
        e = (point_1.z * point_2.z) % curve.n
        c = pow(a, 2, curve.n) * e - pow(b, 3, curve.n) - 2 * pow(b, 2, curve.n) * b2
        x3 = (b * c) % curve.n
        y3 = (a * (pow(b, 2, curve.n) * b2 - c) - pow(b, 3, curve.n) * a2) % curve.n
        z3 = (pow(b, 3, curve.n) * e) % curve.n
        return Point(x3, y3, z3)
    else:
        return doubling(point_1, curve) if a1 == a2 else Point(0, 1, 0)


# Function kPoint
def k_multiply(point_1, k_1, curve):
    if k_1 == 1: return point_1
    point_2, k_2 = Point(0, 1, 0), 0
    bit = 1 << (len(bin(k_1)) - 3)
    while k_1 != k_2:
        k_2 = k_2 << 1 # 2P
        if k_2: point_2 = doubling(point_2, curve)
        if k_1 & bit: point_2, k_2 = add(point_2, point_1, curve), k_2 + 1 # P + Q
        bit = bit >> 1
    return point_2


# Calculation M value for MP point
def find_m(b):
    m = 1
    for p in range(2, b):
        if prime_test(p):
            m *= pow(p, int(math.log(b, p)))
    return m