ANSWER = 16475640049
LIMIT = 50


def main():
    ways = [0 for _ in range(LIMIT + 1)]
    ways[0] = 1
    for i in range(1, LIMIT + 1):
        ways[i] += ways[i - 1]
        if i >= 3:
            ways[i] += 1
        for j in range(i - 3):
            ways[i] += ways[i - j - 4]
    return ways[LIMIT]


if __name__ == '__main__':
    print(main())
