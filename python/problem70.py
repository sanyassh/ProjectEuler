import euler


ANSWER = 8319823
LIMIT = 10 ** 7
SLOW = True


def main():
    lst = euler.totient_list(LIMIT)
    minimum = LIMIT
    n = 0
    sorted_strings = [sorted(str(i)) for i in range(LIMIT)]
    for i in range(2, LIMIT):
        phi = lst[i]
        if sorted_strings[i] == sorted_strings[phi]:
            ratio = i / phi
            if ratio < minimum:
                minimum = ratio
                n = i
    return n


if __name__ == '__main__':
    print(main())
