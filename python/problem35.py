import euler


ANSWER = 55
LIMIT = 10 ** 6


def get_round(n):
    string = str(n)
    return [int(string[i:] + string[:i]) for i in range(len(string))]


def main():
    lst = euler.prime_list_with_zeros(LIMIT)
    count = 0
    for n in lst:
        if n:
            for rounding in get_round(n):
                if lst[rounding] == 0:
                    break
            else:
                count += 1
    return count


if __name__ == '__main__':
    print(main())
