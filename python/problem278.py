import euler


ANSWER = 1228215747273908452
LIMIT = 5 * 10 ** 3


def main():
    prime_list = euler.prime_list(LIMIT)
    r_sums = []
    temp = 0
    for r in reversed(prime_list):
        temp += r
        r_sums.append(temp)
    r_sums.reverse()
    r_sums_1 = [s - len(prime_list) + i for i, s in enumerate(r_sums)]
    total = 0
    for i, p in enumerate(prime_list):
        for j in range(i + 1, len(prime_list) - 1):
            q = prime_list[j]
            f_p_q = (p - 1) * (q - 1) - 1
            p_q = p * q
            total += p_q * r_sums_1[j + 1] + f_p_q * r_sums[j + 1]
    return total


if __name__ == '__main__':
    print(main())
