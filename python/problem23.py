import euler


ANSWER = 4179871
LIMIT = 28124


def abundant(num):
    return num < euler.sum_divisors(num)


def main():
    lst = [i for i in range(1, LIMIT) if abundant(i)]
    length = len(lst)
    half = LIMIT // 2
    cannot_be_written = list(range(LIMIT))
    for i in range(length):
        lst_i = lst[i]
        if lst_i >= half:
            break
        for j in range(i, length):
            num = lst_i + lst[j]
            if num >= LIMIT:
                break
            cannot_be_written[num] = 0
    return sum(cannot_be_written)


if __name__ == '__main__':
    print(main())
