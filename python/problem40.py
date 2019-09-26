import euler


ANSWER = 210


def main():
    string = ''.join(str(i) for i in range(0, 250000))
    return euler.product(int(string[10 ** i]) for i in range(7))


if __name__ == '__main__':
    print(main())
