import euler


ANSWER = 378158756814587
DIGITS = 3
LIMIT = 20
SUM = 9
TEN = 10 ** DIGITS
TEN1 = TEN // 10


def main():
    lst = [0 for _ in range(TEN)]
    for i in range(1, 10):
        lst[i] = 1
    sums = [euler.digit_sum(a) for a in range(TEN)]
    for _ in range(LIMIT - 1):
        new_lst = [0 for _ in range(TEN)]
        for i in range(TEN):
            s = sums[i]
            n = (i % TEN1) * 10
            for j in range(SUM + 1 - s + i // TEN1):
                new_lst[n + j] += lst[i]
        lst = new_lst
    return sum(lst)


if __name__ == '__main__':
    print(main())
