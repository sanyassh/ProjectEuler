import string


ANSWER = '5a411d7b'
DIGITS = string.digits + string.ascii_lowercase
BASE = 14
LIMIT = 10 ** 4


def transform(n, base):
    power = base
    while power < n:
        power *= base
    result = ''
    while power:
        result += DIGITS[n // power]
        n %= power
        power //= base
    if result[0] != '0':
        return result
    return result[1:]


def main():
    total = 16
    numbers = [7, 8]
    digit_sums = [7, 8]
    base_power = BASE
    for _ in range(2, LIMIT + 1):
        new_numbers = []
        new_digit_sums = []
        add = base_power
        base_power *= 14
        for start, digit_sum in zip(numbers, digit_sums):
            for digit, n in enumerate(range(start, base_power, add)):
                if not (n - 1) * n % base_power:
                    new_numbers.append(n)
                    new_sum = digit_sum + digit
                    if digit:
                        total += new_sum
                    new_digit_sums.append(new_sum)
                    break
        numbers = new_numbers
        digit_sums = new_digit_sums
    return transform(total, 14)


if __name__ == '__main__':
    print(main())
