ANSWER = 1366
POWER = 1000


def main():
    return sum(int(d) for d in str(2 ** POWER))


if __name__ == '__main__':
    print(main())
