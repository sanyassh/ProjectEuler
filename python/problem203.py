import euler


ANSWER = 34029210557338
LIMIT = 8


def main():
    pascal = [[0 for _ in range(LIMIT)] for _ in range(51)]
    for i in range(51):
        pascal[i][0] = 1
    for i in range(1, LIMIT):
        for j in range(i + 1):
            pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
    pascal_set = {n for row in pascal for n in row}
    prime_squares = [
        i ** 2
        for i in euler.prime_list(int(max(pascal_set) ** 0.5) + 1)
    ]
    total = 0
    for n in pascal_set:
        for square in prime_squares:
            if n % square == 0:
                break
        else:
            total += n
    return total


if __name__ == '__main__':
    print(main())
