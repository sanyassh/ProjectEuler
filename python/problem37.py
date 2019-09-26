import math

import euler


ANSWER = 748317
LIMIT = 10 ** 6


def main():
    lst = euler.prime_list_with_zeros(LIMIT)
    total = 0
    for i in range(10, LIMIT):
        if lst[i] != 0:
            ind = i
            while ind > 10:
                ind = ind // 10
                if lst[ind] == 0:
                    break
            else:
                ind = i
                while ind > 10:
                    ind = ind % 10 ** int(math.log(ind, 10))
                    if lst[ind] == 0:
                        break
                else:
                    total += i
    return total


if __name__ == '__main__':
    print(main())
