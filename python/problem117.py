ANSWER = 100808458960497
LIMIT = 50


def main():
    ways = [0 for _ in range(LIMIT + 1)]
    ways[0] = 1
    for i in range(1, LIMIT + 1):
        for j in range(1, 5):
            if i >= j:
                ways[i] += ways[i - j]
    return ways[LIMIT]


if __name__ == '__main__':
    print(main())
