import euler


ANSWER = 18407904
LIMIT = 120000


def main():
    prime_list = euler.prime_list(LIMIT + 1000)
    rads = [1 for _ in range(LIMIT)]
    for prime in prime_list:
        for i in range(prime, LIMIT, prime):
            rads[i] *= prime
    squares = [i * i for i in range(2, int(LIMIT ** 0.5) + 1)]
    square_divisibles = sorted(
        {sq * i for sq in squares for i in range(1, LIMIT // sq + 1)}
    )
    count = 0
    for i_c, c in enumerate(square_divisibles):
        if c >= LIMIT:
            break
        if c % 1000 == 0:
            print(c)
        c_2 = c // 2
        d = c / rads[c]
        for i_b in range(i_c - 1, -1, -1):
            b = square_divisibles[i_b]
            if b <= c_2:
                break
            if rads[c - b] * rads[b] < d:
                if euler.gcd1(b, c):
                    count += c
    return count


if __name__ == '__main__':
    print(main())
