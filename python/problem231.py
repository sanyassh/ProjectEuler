import euler


ANSWER = 7526965179680
LIMIT_N = 20 * 10 ** 6
LIMIT_K = 15 * 10 ** 6


def main():
    prime_list = euler.prime_list(LIMIT_N)
    diff = LIMIT_N - LIMIT_K
    result = 0
    for prime in prime_list:
        temp = prime
        while temp <= LIMIT_N:
            result += prime * (LIMIT_N // temp - LIMIT_K // temp - diff // temp)
            temp *= prime
    return result


if __name__ == '__main__':
    print(main())
