ANSWER = 20492570929
LIMIT = 50


def main():
    total = 0
    for tile_len in 2, 3, 4:
        ways = [0 for _ in range(LIMIT + 1)]
        ways[0] = 1
        for i in range(1, LIMIT + 1):
            for j in 1, tile_len:
                if i >= j:
                    ways[i] += ways[i - j]
        total += ways[LIMIT] - 1
    return total


if __name__ == '__main__':
    print(main())
