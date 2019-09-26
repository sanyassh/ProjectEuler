ANSWER = 233168
LIMIT = 1000


def main():
    return sum(n for n in range(LIMIT) if not (n % 3 and n % 5))


if __name__ == '__main__':
    print(main())
