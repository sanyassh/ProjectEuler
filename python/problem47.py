import euler


ANSWER = 134043
COUNT = 4


def main():
    prime_list = euler.prime_list(100000)
    biggest = COUNT
    divisors_count = [
        euler.count_prime_divisors(i, prime_list)
        for i in range(1, biggest + 1)
    ]
    while True:
        if all(count == COUNT for count in divisors_count):
            return biggest - COUNT + 1
        biggest += 1
        divisors_count = divisors_count[1:] + [
            euler.count_prime_divisors(biggest, prime_list)
        ]


if __name__ == '__main__':
    print(main())
