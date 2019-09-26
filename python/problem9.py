import euler


ANSWER = 31875000
SUM = 1000


def main():
    return euler.product(
        next(
            trio
            for c in range(SUM)
            for trio in euler.pythagorean_trio_my(c)
            if sum(trio) == SUM
        )
    )


if __name__ == '__main__':
    print(main())
