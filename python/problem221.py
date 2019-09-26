ANSWER = 1884161251122450
LIMIT = 150000


def main():
    r_2_1 = [r * r + 1 for r in range(10 ** 5)]
    s = set()
    big = 10 ** 16
    for d in range(1, 10 ** 5):
        if d % 1000 == 0:
            if len(s) >= LIMIT:
                last = big
                lst = sorted(s)[:LIMIT + 1]
                big = lst[-1]
                if big == last:
                    return big
                s = set(lst)
        rests = [r for r in range(d - 1, -1, -1) if not r_2_1[r] % d]
        if not rests:
            continue
        start = 0
        while True:
            alexandrian = 0
            for r in rests:
                b = start + r
                a = b + d
                a_b = a * b
                alexandrian = a_b * (a_b + 1) // d
                s.add(alexandrian)
            if alexandrian > big:
                break
            start += d


if __name__ == '__main__':
    print(main())
