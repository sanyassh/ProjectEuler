import euler


ANSWER = 5437849
LIMIT = 50 * 10 ** 6
LIMIT1 = LIMIT + 1
SLOW = True


def main():
    total = 0
    lst = list(range(LIMIT1))
    lst[1] = 0
    nums = [2 * n * n - 1 for n in range(1000)]
    for prime in euler.prime_list(1000):
        for rest in range(1, prime):
            num = nums[rest]
            if not num % prime:
                if num == prime:
                    total += 1
                for i in range(rest, LIMIT1, prime):
                    lst[i] = 0
    for n in lst:
        if n:
            num = 2 * n * n - 1
            if euler.miller_rabin(num):
                total += 1
            for i in range(n, LIMIT1, num):
                lst[i] = 0
    return total


if __name__ == '__main__':
    print(main())
