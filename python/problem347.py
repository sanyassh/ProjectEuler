import euler


ANSWER = 11109800204052
LIMIT = 10 ** 7


def m_func(p, q, n):
    product = p * q
    powers_of_q = 0
    while product <= n:
        product *= q
        powers_of_q += 1
    product //= q
    while product <= n:
        product *= p
    product //= p
    maximum = product
    for _ in range(powers_of_q - 1):
        product //= q
        while product <= n:
            product *= p
        product //= p
        maximum = max(maximum, product)
    return maximum


def s_func(n):
    result = 0
    sqrt = int((n + 1) ** 0.5)
    prime_list = euler.prime_list(n)
    for i in range(len(euler.prime_list(sqrt))):
        p = prime_list[i]
        ind = i + 1
        q = prime_list[ind]
        while p * q <= n:
            result += m_func(p, q, n)
            ind += 1
            q = prime_list[ind]
    return result


def main():
    return s_func(LIMIT)


if __name__ == '__main__':
    print(main())
