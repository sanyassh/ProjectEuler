ANSWER = 45228


def main():
    products = set()
    pandigital_set = set(str(i) for i in range(1, 10))
    for i in range(1, 100):
        for j in range(100, 10000):
            k = i * j
            digits = str(i) + str(j) + str(k)
            if len(digits) > 9:
                break
            if set(digits) == pandigital_set:
                products.add(k)
    return sum(products)


if __name__ == '__main__':
    print(main())
