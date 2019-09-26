import euler


ANSWER = 26241


def main():
    diff = 2
    primes = 3
    total = 5
    ratio = primes / total
    temp = 9
    while ratio >= 0.1:
        diff += 2
        for _ in range(3):
            temp += diff
            if euler.miller_rabin(temp):
                primes += 1
        temp += diff
        total += 4
        ratio = primes / total
    return diff + 1


if __name__ == '__main__':
    print(main())
