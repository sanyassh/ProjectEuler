import euler


ANSWER = 5777
LIMIT = 10 ** 2


def main():
    lst = euler.prime_list_with_zeros(LIMIT ** 2)
    double_squares = [2 * i ** 2 for i in range(1, LIMIT + 1)]
    number = 33
    while True:
        number += 2
        if lst[number] == 0:
            for i in range(LIMIT):
                must_be_prime = number - double_squares[i]
                if must_be_prime > 0:
                    if lst[must_be_prime] != 0:
                        break
                else:
                    return number


if __name__ == '__main__':
    print(main())
