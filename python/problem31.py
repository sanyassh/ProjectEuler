ANSWER = 73682
COINS = [1, 2, 5, 10, 20, 50, 100, 200]
SUM = 200


def find_ways(total, index):
    result = 0
    if total == SUM:
        result += 1
    elif total > SUM:
        pass
    else:
        for i in range(index, 8):
            result += find_ways(total + COINS[i], i)
    return result


def main():
    return find_ways(0, 0)


if __name__ == '__main__':
    print(main())
