import euler


ANSWER = 0
LIMIT = 10 ** 16


def main():
    total = 0
    for a in range(2, int(LIMIT ** 0.25) + 1):
        a_2 = a * a
        for b in range(1, a):
            if euler.gcd1(a, b):
                b_2 = b * b
                a2b2m = a_2 - b_2
                ab_2 = 2 * a * b
                a2b2p = a_2 + b_2
                if euler.gcd1(a2b2m, ab_2):
                    perfect_a = abs(ab_2 * ab_2 - a2b2m * a2b2m)
                    perfect_b = 2 * ab_2 * a2b2m
                    perfect_c = a2b2p * a2b2p
                    if perfect_c > LIMIT:
                        break
                    area = perfect_a * perfect_b // 2
                    if area % 6 and area % 28:
                        total += 1
    return total


if __name__ == '__main__':
    print(main())
