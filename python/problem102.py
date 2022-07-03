import collections
import math

import euler


ANSWER = 228


Point = collections.namedtuple('Point', ['x', 'y'])


def distance(p_1, p_2):
    return math.hypot(p_1.x - p_2.x, p_1.y - p_2.y)


def area(p_1, p_2, p_3):
    a, b, c = distance(p_1, p_2), distance(p_1, p_3), distance(p_2, p_3)
    half_p = (a + b + c) / 2
    return math.sqrt(half_p * (half_p - a) * (half_p - b) * (half_p - c))


def contains(p_1, p_2, p_3, p):
    return math.isclose(
        area(p_1, p_2, p) + area(p_1, p_3, p) + area(p_2, p_3, p),
        area(p_1, p_2, p_3)
    )


def main():
    lst = [
        [int(c) for c in line.split(',')]
        for line in euler.data(__file__)
    ]
    total = 0
    zero = Point(0, 0)
    for coordinates in lst:
        p1x, p1y, p2x, p2y, p3x, p3y = coordinates
        p_1, p_2, p_3 = Point(p1x, p1y), Point(p2x, p2y), Point(p3x, p3y)
        if contains(p_1, p_2, p_3, zero):
            total += 1
    return total


if __name__ == '__main__':
    print(main())
