import euler


ANSWER = 871198282


def main():
    return sum(
        (i + 1) * euler.alphabetical_value(name) for i, name in enumerate(
            sorted(open('../txt/problem022.txt').readline()[1:-1].split('","'))
        )
    )


if __name__ == '__main__':
    print(main())
