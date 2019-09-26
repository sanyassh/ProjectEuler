ANSWER = 872187
LIMIT = 10 ** 6


def main():
    total = 0
    for i in range(1, 1000000, 2):
        if i == int(str(i)[::-1]):
            b = bin(i)[2:]
            if b == b[::-1]:
                total += i
    return total


if __name__ == '__main__':
    print(main())
