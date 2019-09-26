ANSWER = 2544559
LIMIT = 50 * 10 ** 6


def main():
    lst = [0 for _ in range(LIMIT)]
    for d in range(1, LIMIT // 4 + 1):
        const = 3 * d * d
        double_d = 2 * d
        for z in range(1, d + 1):
            n = const + double_d * z - z * z
            if n >= LIMIT:
                break
            lst[n] += 1
        for z in range(3 * d - 1, d, -1):
            n = const + double_d * z - z * z
            if n >= LIMIT:
                break
            lst[n] += 1
    return lst.count(1)


if __name__ == '__main__':
    print(main())
