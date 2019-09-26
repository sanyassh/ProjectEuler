import euler


ANSWER = 35407281
LIMIT = 500500


def main():
    prime_list = []
    ten = 10
    while len(prime_list) < LIMIT:
        ten *= 10
        prime_list = euler.prime_list(ten)
    prime_list = prime_list[:LIMIT]
    lst = [1 for _ in prime_list]
    begin = 0
    end = len(prime_list) - 1
    while lst[begin]:
        power = lst[begin] + 1
        if prime_list[begin] ** power < prime_list[end]:
            lst[end] = 0
            lst[begin] += power
            end -= 1
        else:
            begin += 1
    n = 1
    for prime, power in zip(prime_list, lst):
        n = (n * prime ** power) % 500500507
    return n


if __name__ == '__main__':
    print(main())
