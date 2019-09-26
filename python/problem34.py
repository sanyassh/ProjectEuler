import euler


ANSWER = 40730


def main():
    return sum(
        i for i in range(10, 2177280)
        if i == sum(euler.FACTORIALS[int(digit)] for digit in str(i))
    )


if __name__ == '__main__':
    print(main())
