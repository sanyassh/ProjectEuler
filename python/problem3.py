import euler


ANSWER = 6857
NUMBER = 600851475143


def main():
    return euler.list_of_prime_factors(NUMBER)[-1]


if __name__ == '__main__':
    print(main())
