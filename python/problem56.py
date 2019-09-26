import euler


ANSWER = 972


def main():
    return max(
        euler.digit_sum(a ** b)
        for a in range(1, 100)
        for b in range(1, 100)
    )


if __name__ == '__main__':
    print(main())
