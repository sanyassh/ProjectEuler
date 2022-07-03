import euler


ANSWER = 1096883702440585
PRIME_LIST = euler.prime_list(190)
LIMIT = euler.product(PRIME_LIST)
SQRT = euler.int_sqrt(LIMIT)
GLOBAL = {'result': 0}
SLOW = True
INFINITE = True


def work(number, product, index):
    for i in range(42 - 1, index, -1):
        new_product = product * PRIME_LIST[i]
        new_number = number - number % new_product
        if new_number > GLOBAL['result']:
            if not LIMIT % new_number:
                GLOBAL['result'] = new_number
                print(GLOBAL['result'] % 10 ** 16)
            work(new_number, new_product, i)


def main():
    work(SQRT, 1, -1)
    return GLOBAL['result'] % 10 ** 16


if __name__ == '__main__':
    print(main())
