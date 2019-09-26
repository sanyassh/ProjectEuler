import euler


ANSWER = 39782849136421
LIMIT = 10 ** 7
LIMIT1 = LIMIT + 1
SLOW = True


def main():
    power_list = euler.prime_list_with_zeros(LIMIT1)
    fast_list = power_list[:]
    max_divisors = euler.max_divisors(range(LIMIT1))
    total = 0
    for i in range(len(power_list)-1, -1, -1):
        if power_list[i]:
            temp = i
            while temp < LIMIT1:
                power_list[temp] = 1
                temp *= i
    for n in range(2, LIMIT1):
        if power_list[n]:
            total += 1
        elif not n & 1 and fast_list[n >> 1]:
            total += (n >> 1) + 1
        else:
            max_divisor = max_divisors[n]
            r = n // max_divisor
            for a in range(r - 1, 0, -1):
                a_m = a * max_divisor
                if not a_m * (a_m + 1) % n:
                    total += a_m + 1
                    break
                if not a_m * (a_m - 1) % n:
                    total += a_m
                    break
    return total


if __name__ == '__main__':
    print(main())
