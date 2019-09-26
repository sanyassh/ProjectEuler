ANSWER = 333082500
LIMIT = 1000


def main():
    return sum(
        max(
            2 * a * n % (a * a)
            for n in range(3, LIMIT * 2 + 1, 2)
        )
        for a in range(3, LIMIT + 1)
    )


if __name__ == '__main__':
    print(main())
