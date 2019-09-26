import euler


ANSWER = -59231


def main():
    maximum_l = 0
    maximum_a = 0
    maximum_b = 0
    lst = euler.prime_list(1000)
    for b in lst:
        for a in range(-b + 2, 1001, 2):
            n = 0
            length = 0
            c = b
            while c > 1 and euler.is_prime(c, lst):
                # miller-rabin is slow because they all are primes
                n += 1
                length += 1
                c = n ** 2 + a * n + b
            if length > maximum_l:
                maximum_l = length
                maximum_a = a
                maximum_b = b
    return maximum_a * maximum_b


if __name__ == '__main__':
    print(main())
