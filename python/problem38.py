ANSWER = 932718654


def main():
    digits = set(str(i) for i in range(1, 10))
    for i in range(9999, 9000 - 1, -1):
        concatenated_product = str(i) + str(i * 2)
        if set(concatenated_product) == digits:
            return int(concatenated_product)
    return 0


if __name__ == '__main__':
    print(main())
