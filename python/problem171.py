import euler


ANSWER = 142989277
LIMIT = 20
LIMIT1 = LIMIT + 1


REPUNITS = [0]
for _ in range(1, LIMIT1):
    REPUNITS.append(REPUNITS[-1] * 10 + 1)

SQUARES_MASK = [False for i in range(45 * 45 + 1)]
for N in range(45 + 1):
    SQUARES_MASK[N * N] = True
DIGIT_SQUARES = [i * i for i in range(10)]


def check(lst):
    result = 0
    for i in range(1, 10):
        result += DIGIT_SQUARES[i] * lst[i]
    return SQUARES_MASK[result]


def permutations(lst, length):
    result = euler.FACTORIALS[length]
    for k in lst:
        result //= euler.FACTORIALS[k]
    return result


def summ(lst, length):
    total = 0
    for i in range(1, 10):
        total += i * lst[i]
    return total * permutations(lst, length) * REPUNITS[length] // length


def main():
    list_of_lists = []
    for i in range(10):
        list_of_lists.append([0 for _ in range(10)])
        list_of_lists[-1][i] = 1
    list_of_last = list(range(10))
    list_of_len = [1 for _ in range(10)]
    total = 0
    while list_of_lists:
        lst = list_of_lists.pop()
        last = list_of_last.pop()
        length = list_of_len.pop()
        if length == LIMIT:
            if check(lst):
                total += summ(lst, LIMIT)
        elif length < LIMIT:
            length1 = length + 1
            for i in range(last, 10):
                new_lst = lst[:]
                new_lst[i] += 1
                list_of_lists.append(new_lst)
                list_of_last.append(i)
                list_of_len.append(length1)
    return total % 10 ** 9


if __name__ == '__main__':
    print(main())
