import euler


ANSWER = 73162890


def main():
    lst = [line.split()[0] for line in euler.data(__file__)]

    digits = set()
    for n in lst:
        for digit in n:
            digits.add(digit)

    before = {}
    for digit in digits:
        before[digit] = set()
        for n in lst:
            i = n.find(digit)
            for j in range(i):
                before[digit].add(n[j])

    return ''.join(sorted(before.keys(), key=lambda digit: len(before[digit])))


if __name__ == '__main__':
    print(main())
