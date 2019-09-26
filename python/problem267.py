import euler


ANSWER = 0.999992836187
LIMIT = 10 ** 9
POWER = 1000


def main():
    min_power = POWER
    for q in (i * 0.001 for i in range(500)):
        for power in range(POWER, -1, -1):
            if (1 + q * 2) ** power * (1 - q) ** (POWER - power) < LIMIT:
                min_power = min(min_power, power + 1)
                break
    combinations = [euler.combination(POWER, k) for k in range(POWER + 1)]
    return round(sum(combinations[min_power:]) / sum(combinations), 12)


if __name__ == '__main__':
    print(main())
