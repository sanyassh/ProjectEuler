import itertools


ANSWER = 126461847755
LIMIT = 40


def main():
    digits = list(range(10))
    all_sets = [
        set(s)
        for i in range(1, 11)
        for s in itertools.combinations(digits, i)
    ]
    len_sets = len(all_sets)
    list_of_sets = [
        [
            all_sets.index(all_sets[i].union({j}))
            for j in range(10)
        ]
        for i in range(len_sets)
    ]
    list_of_nums = [
        [0 for _ in range(10)]
        for _ in range(len_sets)
    ]
    for i in range(1, 10):
        list_of_nums[all_sets.index({i})][i] = 1
    result = 0
    ind = all_sets.index({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
    for _ in range(LIMIT - 1):
        new_lst = [[0 for _ in range(10)] for _ in range(len_sets)]
        for i in range(len_sets):
            for j in range(9):
                new_lst[list_of_sets[i][j]][j] += list_of_nums[i][j + 1]
                new_lst[list_of_sets[i][j + 1]][j + 1] += list_of_nums[i][j]
        list_of_nums = new_lst
        result += sum(list_of_nums[ind])
    return result


if __name__ == '__main__':
    print(main())
