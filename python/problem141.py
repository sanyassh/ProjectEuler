ANSWER = 878454337159
LIMIT = 10 ** 12


def main():
    squares = {i * i for i in range(1, int(LIMIT ** 0.5) + 1)}
    s = set()
    for n in range(2, int(LIMIT ** (1 / 3)) + 1):
        n_3 = n * n * n
        for a in range(1, LIMIT):
            if a * (a * n_3 + 1) > LIMIT:
                break
            for m in range(1, n):
                q = a * m * (a * n_3 + m)
                if q > LIMIT:
                    break
                if q in squares:
                    s.add(q)
    return sum(s)


if __name__ == '__main__':
    print(main())
