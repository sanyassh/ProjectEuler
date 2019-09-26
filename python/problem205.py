ANSWER = 0.5731441


def distribution(sides, amount):
    rolls = [[i + 1] for i in range(sides)]
    for _ in range(amount - 1):
        rolls = [lst + [i + 1] for lst in rolls for i in range(sides)]
    points = [0 for _ in range(sides * amount + 1)]
    for lst in rolls:
        points[sum(lst)] += 1
    return points


def main():
    pyramidal = distribution(4, 9)
    cubic = distribution(6, 6)
    wins = sum(
        sum(cubic[:i]) * pyramidal_i
        for i, pyramidal_i in enumerate(pyramidal)
    )
    return round(wins / (sum(pyramidal) * sum(cubic)), 7)


if __name__ == '__main__':
    print(main())
