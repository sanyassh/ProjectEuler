import euler


ANSWER = 871198282


def main():
    return sum(
        (i + 1) * euler.alphabetical_value(name) for i, name in enumerate(
            sorted(euler.data(__file__)[0][1:-1].split('","'))
        )
    )


if __name__ == '__main__':
    print(main())
