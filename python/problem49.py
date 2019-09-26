import euler


ANSWER = 296962999629


def main():
    lst = euler.prime_list_with_zeros(10000)
    for i in range(1000, 10000):
        if (
                lst[i] != 0 and
                lst[i] != 1487
        ):
            for diff in range(500, (10000 - i) // 2):
                if (
                        lst[i + diff] != 0 and
                        lst[i + 2 * diff] != 0 and
                        (
                            set(str(lst[i])) ==
                            set(str(lst[i + diff])) ==
                            set(str(lst[i + 2 * diff]))
                        )
                ):
                    return int(
                        str(lst[i]) +
                        str(lst[i + diff]) +
                        str(lst[i + 2 * diff])
                    )
    return 0


if __name__ == '__main__':
    print(main())
