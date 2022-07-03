import euler


ANSWER = 1677366278943
LIMIT = 40 * 10 ** 6
SLOW = True


def main():
    totient_list = euler.totient_list(LIMIT)
    chains = [0, 1]
    total = 0
    for i in range(2, LIMIT):
        chains.append(chains[totient_list[i]] + 1)
        if chains[-1] == 25 and totient_list[i] == i - 1:
            total += i
    return total


if __name__ == '__main__':
    print(main())
