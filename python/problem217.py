import collections


ANSWER = 6273134
POWER = 47
LIMIT = 10 ** POWER
MODULUS = 3 ** 15


def main():
    result = 50040  # for POWER = 3
    sum_09 = {i: i for i in range(0, 10)}
    sum_19 = {i: i for i in range(1, 10)}
    count_09 = {i: 1 for i in range(0, 10)}
    count_19 = {i: 1 for i in range(1, 10)}
    for power in range(2, POWER // 2 + 1):
        new_sum_09 = collections.defaultdict(int)
        new_sum_19 = collections.defaultdict(int)
        new_count_09 = collections.defaultdict(int)
        new_count_19 = collections.defaultdict(int)
        for digit in range(10):
            for digit_sum, summ in sum_09.items():
                new_sum_09[digit + digit_sum] += (
                    summ * 10 + digit * count_09[digit_sum]
                )
            for digit_sum, summ in sum_19.items():
                new_sum_19[digit + digit_sum] += (
                    summ * 10 + digit * count_19[digit_sum]
                )
            for digit_sum, count in count_09.items():
                new_count_09[digit + digit_sum] += count
            for digit_sum, count in count_19.items():
                new_count_19[digit + digit_sum] += count
        sum_09 = new_sum_09
        sum_19 = new_sum_19
        count_09 = new_count_09
        count_19 = new_count_19
        for digit_sum in sum_19:
            n = (
                sum_19[digit_sum] * count_09[digit_sum] * 10 ** power * 101 +
                sum_09[digit_sum] * count_19[digit_sum] * 11 +
                45 * 10 ** power * count_19[digit_sum] * count_09[digit_sum]
            )
            result += n
    return result % MODULUS


if __name__ == '__main__':
    print(main())
