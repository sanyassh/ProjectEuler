ANSWER = 1425480602091519
DIGITS = 16
DIVISOR = 250
LIMIT = 250250


def main():
    divisor_for_digits = 10 ** DIGITS
    rests = [0 for _ in range(DIVISOR)]
    rests[0] = 1
    for i in range(1, LIMIT + 1):
        rest = pow(i, i, DIVISOR)
        rests = [
            (rests[j] + rests[(j - rest) % DIVISOR]) % divisor_for_digits
            for j in range(DIVISOR)
        ]
    return rests[0] - 1


if __name__ == '__main__':
    print(main())
