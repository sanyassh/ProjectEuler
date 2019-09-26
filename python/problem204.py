import euler


ANSWER = 2944730
LIMIT = 10 ** 9


def main():
    prime_set = set(euler.prime_list(100))
    product_set = prime_set.copy()
    all_set = prime_set | {1}
    while product_set:
        product_set = {
            i * j
            for i in product_set
            for j in prime_set
            if i * j <= LIMIT
        }
        all_set.update(product_set)
    return len(all_set)


if __name__ == '__main__':
    print(main())
