ANSWER = 100


def main():
    nom = []
    denom = []
    for i in range(1, 10):
        for a in range(1, 10):
            for b in range(a + 1, 10):
                if (10 * i + a) / (10 * b + i) == a / b:
                    nom.append(10 * i + a)
                    denom.append(10 * b + i)
                if (10 * a + i) / (10 * i + b) == a / b:
                    nom.append(10 * a + i)
                    denom.append(10 * i + b)
    a = 1
    for k in denom:
        a *= k
    for k in nom:
        if a % k == 0:
            a //= k
    return a


if __name__ == '__main__':
    print(main())
