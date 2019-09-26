ANSWER = 9183
LIMIT_A = LIMIT_B = 100


def main():
    return len(
        set(
            a ** b for a in range(2, LIMIT_A + 1)
            for b in range(2, LIMIT_B + 1)
        )
    )


if __name__ == '__main__':
    print(main())
