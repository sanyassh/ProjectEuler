ANSWER = 168
LIMIT = 10 ** 6
M = 50


def main():
    ways = [1]
    while ways[-1] < LIMIT:
        ways.append(ways[-1])
        i = len(ways) - 1
        if i >= M:
            ways[i] += 1
        for j in range(i - M):
            ways[i] += ways[i - j - M - 1]
    return len(ways) - 1


if __name__ == '__main__':
    print(main())
