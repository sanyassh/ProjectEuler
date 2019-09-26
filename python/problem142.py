import itertools
import collections
import math

import euler


ANSWER = 1006193


def calculate(trio1, trio2):
    d, e, a = trio1
    f, c, a = trio2
    if c < e:
        d, e, f, c = f, c, d, e
    b_2 = c * c - e * e
    if euler.is_square(b_2):
        x_2 = a * a + b_2
        if x_2 % 2 == 0:
            x = x_2 // 2
            y = a * a - x
            z = c * c - x
            b = euler.int_sqrt(b_2)
            x_y_z = int(x + y + z)
            return x_y_z, min(a, b, c, d, e, f), max(a, b, c, d, e, f)
    return None, None, None


def main():
    min_x_y_z = math.inf
    max_param = math.inf
    triplets = collections.defaultdict(list)
    for gen_c in itertools.count(1):
        for trio in euler.pythagorean_trio_my(gen_c):
            lst = triplets[trio[-1]]
            lst.append(trio)
            for trio1, trio2 in itertools.combinations(lst, 2):
                x_y_z, min_param, new_max_param = calculate(trio1, trio2)
                if x_y_z and x_y_z < min_x_y_z:
                    min_x_y_z = x_y_z
                    max_param = new_max_param
                if min_param and min_param > max_param:
                    return min_x_y_z
    return 0


if __name__ == '__main__':
    print(main())
