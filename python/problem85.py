import math


ANSWER = 2772
LIMIT = 2 * 10 ** 6


def rectangles(x, y):
    return sum((x - i) * (y - j) for i in range(x) for j in range(y))


def main():
    near_i, near_j = 0, 0
    difference = math.inf
    max_length = int((LIMIT * 2) ** 0.5)
    for i in range(max_length):
        for j in range(max_length):
            diff = abs(LIMIT - rectangles(i, j))
            if diff < difference:
                difference = diff
                near_i, near_j = i, j
            elif diff > LIMIT:
                break
    return near_i * near_j


if __name__ == '__main__':
    print(main())
