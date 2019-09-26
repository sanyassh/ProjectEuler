import euler


ANSWER = 227485267000992000
LIMIT = 18


def permutations(lst, s):
    result = euler.combination(s - 1, lst[0])
    s -= lst[0]
    for i in range(1, 10):
        result *= euler.combination(s, lst[i])
        s -= lst[i]
    return result


def main():
    list_of_lists = [[0 for _ in range(10)] for _ in range(10)]
    for i in range(10):
        list_of_lists[i][i] = 1
    for i in range(2, LIMIT + 1):
        new_lst = []
        for lst in list_of_lists:
            ind = 0
            for j in range(9, -1, -1):
                if lst[j] != 0:
                    ind = j
                    break
            for j in range(ind, 10):
                if lst[j] < 3:
                    new_lst.append(lst[:])
                    new_lst[-1][j] += 1
        list_of_lists = new_lst
    result = 0
    for lst in list_of_lists:
        result += permutations(lst, 18)
    return result


if __name__ == '__main__':
    print(main())
