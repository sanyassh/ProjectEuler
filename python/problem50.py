import euler


ANSWER = 997651
LIMIT = 10 ** 6


def main():
    lst = euler.prime_list_with_zeros(LIMIT)
    prime_list = [n for n in lst if n != 0]
    length = len(prime_list)
    prime = 0
    max_j = 0
    for i in range(length):
        for j in range(1, length - i):
            total = sum(prime_list[i:i + j])
            if total > 1000000:
                if j < max_j:
                    return prime
                break
            if lst[total] != 0:
                prime = max(prime, total)
                max_j = max(max_j, j)
    return prime


if __name__ == '__main__':
    print(main())
