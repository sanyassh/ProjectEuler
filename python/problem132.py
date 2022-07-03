import euler


ANSWER = 843296
LIMIT = 10 ** 9
SLOW = True


def find(n):
    rest = 1
    i = 1
    while rest:
        rest = (rest * 10 + 1) % n
        i += 1
    return i


def main():
    prime_list = euler.prime_list(1000000)
    prime_list.remove(2)
    prime_list.remove(5)
    total = 0
    count = 0
    for prime in prime_list:
        if LIMIT % find(prime) == 0:
            count += 1
            total += prime
            if count == 40:
                return total
    return 0


if __name__ == '__main__':
    print(main())
