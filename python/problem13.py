import euler


ANSWER = 5537376230
DIGITS = 10


def main():
    return int(str(sum(int(line) for line in euler.data(__file__)))[:DIGITS])


if __name__ == '__main__':
    print(main())
