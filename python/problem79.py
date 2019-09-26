ANSWER = 73162890


def main():
    lst = [line.split()[0] for line in open('../txt/problem079.txt')]

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

    password = ''
    for _ in range(len(before)):
        for digit in before.copy():
            if not before[digit]:
                password += digit
                for digit_after in before:
                    before[digit_after].discard(digit)
                before.pop(digit)
    return password


if __name__ == '__main__':
    print(main())
