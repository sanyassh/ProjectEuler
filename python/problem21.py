import euler


ANSWER = 31626


def main():
    total = 0
    for num in range(2, 10000):
        sum_divisors = euler.sum_divisors(num)
        if sum_divisors != num:
            if euler.sum_divisors(sum_divisors) == num:
                total += num
    return total


if __name__ == '__main__':
    print(main())
