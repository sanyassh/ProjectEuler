ANSWER = 336108797689259276
LIMIT = 10 ** 12


def main():
    repunits = set()
    for base in range(2, int(LIMIT ** 0.5) + 1):
        num = base * base + base + 1
        while num < LIMIT:
            repunits.add(num)
            num = num * base + 1
    return sum(repunits) + 1


if __name__ == '__main__':
    print(main())
