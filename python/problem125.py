import euler


ANSWER = 2906969179
LIMIT = 10 ** 8


def main():
    s = set()
    for b in range(1, 10000):
        temp = b * (b + 1) * (2 * b + 1)
        for a in range(b - 2, -1, -1):
            result = (temp - a * (a + 1) * (2 * a + 1)) // 6
            if result > LIMIT:
                break
            if euler.is_palindrome(result):
                s.add(result)
    return sum(s)


if __name__ == '__main__':
    print(main())
