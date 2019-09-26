ANSWER = 44043947822


def main():
    next_n = 5
    next_power_of_two = 8
    powers_of_two = 2
    p = powers_of_two / (next_n - 2)
    stop = 1 / 12345
    while p >= stop:
        if next_n == next_power_of_two:
            powers_of_two += 1
            next_power_of_two *= 2
        next_n += 1
        p = powers_of_two / (next_n - 2)
    return (next_n - 2) * (next_n - 1)


if __name__ == '__main__':
    print(main())
