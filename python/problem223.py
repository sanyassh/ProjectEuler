import euler


ANSWER = 61614848
LIMIT = 25 * 10 ** 6
DIVISORS_LIST = euler.divisors_list(LIMIT // 3)


def divisors_of_n2_minus_1(n):
    return sorted(
        {
            i * j
            for i in DIVISORS_LIST[n - 1]
            for j in DIVISORS_LIST[n + 1]
        }
    )


def main():
    count = (LIMIT - 1) // 2
    for a in range(2, LIMIT // 3 - 1):
        a_mod_2 = a & 1
        a2_minus_1 = a * a - 1
        for c_minus_b in divisors_of_n2_minus_1(a):
            if c_minus_b & 1 != a_mod_2:
                c_plus_b = a2_minus_1 // c_minus_b
                if c_plus_b & 1 != a_mod_2:
                    c = (c_plus_b + c_minus_b) >> 1
                    b = c_plus_b - c
                    if b < a:
                        break
                    if a + b + c <= LIMIT:
                        count += 1
    return count


if __name__ == '__main__':
    print(main())
