import array


ANSWER = 55374
DIVISOR = 10 ** 6


def main():
    lst = [array.array('L', (1,))]
    i = 0
    while True:
        i += 1
        new_row = array.array('L', (0 for _ in range(i)))
        i_j_1 = i
        for j in range(i):
            i_j_1 -= 1
            new_row[j] = lst[i_j_1][0]
            if len(lst[i_j_1]) > 1:
                lst[i_j_1][1] = (lst[i_j_1][0] + lst[i_j_1][1]) % DIVISOR
                lst[i_j_1].pop(0)
        if sum(new_row) % DIVISOR == 0:
            return i
        lst.append(new_row)


if __name__ == "__main__":
    print(main())
