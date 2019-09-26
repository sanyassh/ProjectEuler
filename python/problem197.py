ANSWER = 1.710637717


def main():
    a = b = -1
    ten = 10 ** -9
    for _ in range(600):
        a = b
        b = int(2**(30.403243784 - a*a))*ten
    return round(a + b, 9)


if __name__ == '__main__':
    print(main())
