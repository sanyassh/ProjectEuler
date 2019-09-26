ANSWER = 25164150
LIMIT = 100


def main():
    return (
        (LIMIT * (LIMIT + 1) // 2) ** 2 -
        (2 * LIMIT ** 3 + 3 * LIMIT ** 2 + LIMIT) // 6
    )


if __name__ == '__main__':
    print(main())
