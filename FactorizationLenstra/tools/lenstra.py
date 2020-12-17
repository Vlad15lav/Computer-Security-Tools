from tools.random_obj import get_random_point, get_random_curve
from tools.points_operations import k_multiply, find_m
import numpy as np
import time
import copy


# Lenstra's algorithm
def lenstra(n, b, curves, i):
    # Looking at the curves
    for i in range(i, curves):
        # get a random point and curve
        point = get_random_point(n)
        point_copy = copy.deepcopy(point)
        curve = get_random_curve(point, n)
        # Find the GCD
        g = np.gcd(n, 4 * pow(curve.a, 3) + 27 * pow(curve.b, 2))

        # Bad curve
        if g == n:
            continue

        elif 1 < g < n:
            return [g, int(n / g)], i + 1, point_copy, curve
        else:

            m = find_m(b)
            # Calculation MP point
            point = k_multiply(point, m, curve)
            # Search GCD
            gcd_nz = np.gcd(n, point.z)

            if gcd_nz > 1 and gcd_nz != n:
                return [gcd_nz, int(n / gcd_nz)],  i + 1, point_copy, curve
    return None
