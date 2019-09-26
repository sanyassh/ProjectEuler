import itertools


ANSWER = 142857


def main():
    return next(
        number
        for number in itertools.count(start=1)
        if all(
            set(str(number * i)) == set(str(number))
            for i in range(2, 7)
        )
    )


if __name__ == '__main__':
    print(main())
