from sympy.geometry import Point
from sympy.geometry import Triangle


ANSWER = 228


def main():
    lst = [
        [int(c) for c in line.split(',')]
        for line in open('../txt/problem102.txt')
    ]
    total = 0
    zero = Point(0, 0)
    for k in lst:
        point1, point2, point3 = Point(*k[:2]), Point(*k[2:4]), Point(*k[4:])
        if Triangle(point1, point2, point3).encloses_point(zero):
            total += 1
    return total


if __name__ == '__main__':
    print(main())
