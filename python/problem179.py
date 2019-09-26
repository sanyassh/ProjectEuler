ANSWER = 986262
LIMIT = 10 ** 7


def main():
    lst = [0 for _ in range(LIMIT + 1)]
    for i in range(2, int(LIMIT ** 0.5) + 1):
        for j in range(i * i, LIMIT + 1, i):
            lst[j] += 2
        lst[i * i] -= 1
    result = 0
    for i in range(2, LIMIT):
        if lst[i] == lst[i+1]:
            result += 1
    return result


if __name__ == '__main__':
    print(main())
