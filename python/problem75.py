ANSWER = 161667
LIMIT = 1500000


PERIMETERS: list = [set() for i in range(LIMIT + 1)]


def calculate_combinations(p):
    q = p + 1
    p_sqr = p * p
    q_sqr = q * q
    while True:
        a = q_sqr - p_sqr
        b = 2 * p * q
        c = q_sqr + p_sqr
        perimeter = a + b + c
        if perimeter <= LIMIT:
            a, b = min(a, b), max(a, b)
            for i in range(1, LIMIT // perimeter + 1):
                PERIMETERS[i * perimeter].add((a * i, b * i, c * i))
        else:
            break
        q += 1
        q_sqr = q * q


def main():
    for p in range(1, int(LIMIT ** 0.5) // 2 + 1):
        calculate_combinations(p)
    return sum(len(combinations) == 1 for combinations in PERIMETERS)


if __name__ == '__main__':
    print(main())
