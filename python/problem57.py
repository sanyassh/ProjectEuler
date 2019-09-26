ANSWER = 153


def main():
    nom, denom = 3, 2
    total = 0
    for _ in range(1, 1000):
        nom, denom = nom + 2 * denom, nom + denom
        if len(str(nom)) > len(str(denom)):
            total += 1
    return total


if __name__ == '__main__':
    print(main())
