import euler


ANSWER = 322303240771079935
LIMIT = 7208785
LIMIT2 = 5678027
PRIME_LIST = euler.prime_list(LIMIT)
SLOW = True


def start_of_row(n):
    return n * (n - 1) // 2 + 1


def number(n, i):
    if not 0 <= i < n:
        return 0
    return start_of_row(n) + i


def sieve_row(n):
    lst = [1 for _ in range(n)]
    start = start_of_row(n)
    for prime in PRIME_LIST:
        index = (prime - start % prime) % prime
        for i in range(index, n, prime):
            lst[i] = 0
    return lst


def primes_around(sieves, row, i):
    result = []
    for d_r in range(-1, 2):
        for d_i in range(-1, 2):
            check_row = row + d_r
            check_i = i + d_i
            if (
                    (d_r or d_i) and
                    (0 <= check_row < 5) and
                    (0 <= check_i < len(sieves[check_row]))
            ):
                if sieves[check_row][check_i]:
                    result.append((check_row, check_i))
    return result


def calculate_row(n):
    result = 0
    sieves = [sieve_row(m) for m in range(n - 2, n + 3)]
    for i in range(n):
        if sieves[2][i]:
            around = primes_around(sieves, 2, i)
            if len(around) > 1:
                result += number(n, i)
            elif len(around) == 1:
                if len(primes_around(sieves, *around[0])) > 1:
                    result += number(n, i)
    return result


def main():
    return calculate_row(LIMIT) + calculate_row(LIMIT2)


if __name__ == '__main__':
    print(main())
