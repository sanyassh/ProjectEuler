import euler


ANSWER = 272
N = 100


def main():
    nom1, denom1 = 3, 1
    nom2, denom2 = 8, 3
    i = 3
    step = 4
    while True:
        for _ in range(2):
            nom1, denom1, nom2, denom2 = (
                nom2, denom2, nom1 + nom2, denom1 + denom2
            )
            i += 1
            if i == N:
                return euler.digit_sum(nom2)
        nom1, denom1, nom2, denom2 = (
            nom2, denom2, nom1 + nom2 * step, denom1 + denom2 * step
        )
        step += 2
        i += 1
        if i == N:
            return euler.digit_sum(nom2)


if __name__ == '__main__':
    print(main())
