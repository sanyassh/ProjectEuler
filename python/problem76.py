ANSWER = 190569291
LIMIT = 100


def main():
    lst = [[1]]
    for i in range(1, LIMIT + 1):
        new_row = [0 for _ in range(i)]
        i_j_1 = i
        for j in range(i):
            i_j_1 -= 1
            new_row[j] = lst[i_j_1][0]
            if len(lst[i_j_1]) > 1:
                lst[i_j_1][0] = sum(lst[i_j_1][:2])
                lst[i_j_1].pop(1)
        lst.append(new_row)
    return sum(lst[LIMIT]) - 1


if __name__ == '__main__':
    print(main())
