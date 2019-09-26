ANSWER = 48861552
LIMIT = 10 ** 4


def main():
    total = 0
    k = 1
    for n in range(5, LIMIT + 1):
        if (n / k) < (n / (k + 1)) ** ((k + 1) / k):
            k += 1
        copy_k = k
        while not copy_k & 1:
            copy_k >>= 1
        while not copy_k % 5:
            copy_k //= 5
        if n % copy_k:
            total += n
        else:
            total -= n
    return total


if __name__ == '__main__':
    print(main())
