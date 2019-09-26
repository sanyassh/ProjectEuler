ANSWER = 5537376230
DIGITS = 10


def main():
    return int(
        str(
            sum(
                (
                    int(line)
                    for line in open('../txt/problem013.txt')
                )
            )
        )[:DIGITS]
    )


if __name__ == '__main__':
    print(main())
