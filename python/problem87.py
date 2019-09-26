import euler


ANSWER = 1097343
LIMIT = 50 * 10 ** 6


def main():
    primes_for_square = euler.prime_list_with_zeros(int(LIMIT ** 0.5))
    primes_for_cube = euler.clean_zeros(
        primes_for_square[:int(LIMIT ** (1 / 3))]
    )
    primes_for_forth_power = euler.clean_zeros(
        primes_for_square[:int(LIMIT ** 0.25)]
    )
    primes_for_square = euler.clean_zeros(primes_for_square)
    numbers = set()
    for i in primes_for_forth_power:
        for j in primes_for_cube:
            temp = i ** 4 + j ** 3
            if temp >= LIMIT:
                break
            for k in primes_for_square:
                n = temp + k ** 2
                if n < LIMIT:
                    numbers.add(n)
    return len(numbers)


if __name__ == '__main__':
    print(main())
