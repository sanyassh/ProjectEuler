import euler


ANSWER = 453647705
LIMIT = 10 ** 5
SLOW = True


def find(n):
    rest = 1
    i = 1
    while rest:
        rest = (rest * 10 + 1) % n
        i += 1
    return i


def main():
    prime_list = euler.prime_list(LIMIT)
    prime_list.remove(2)
    prime_list.remove(5)
    result = 0
    for prime in prime_list:
        f = find(prime)
        while f % 2 == 0:
            f >>= 1
        while f % 5 == 0:
            f //= 5
        if f == 1:
            result += prime
    return sum(prime_list) - result + 2 + 5


if __name__ == '__main__':
    print(main())
