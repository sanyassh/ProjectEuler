import euler


ANSWER = 249


def step(n):
    return n + int(str(n)[::-1])


def main():
    count = 0
    for i in range(1, 10000):
        for _ in range(50):
            i = step(i)
            if euler.is_palindrome(i):
                break
        else:
            count += 1
    return count


if __name__ == '__main__':
    print(main())
