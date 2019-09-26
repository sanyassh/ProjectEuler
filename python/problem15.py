import euler


ANSWER = 137846528820
GRID = 20, 20


def main():
    return (
        euler.FACTORIALS[GRID[0] + GRID[1]] //
        euler.FACTORIALS[GRID[0]] //
        euler.FACTORIALS[GRID[1]]
    )


if __name__ == '__main__':
    print(main())
