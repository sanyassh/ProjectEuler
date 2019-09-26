ANSWER = 8739992577
DIGITS = 10


def main():
    a = 1
    mod = 10 ** DIGITS
    for _ in range(7830457):
        a = (a << 1) % mod
    a = a * 28433 + 1
    return a % mod


if __name__ == '__main__':
    print(main())
