import copy


ANSWER = 24702


def load(number, lines):
    lines = lines[number * 10 + 1:(number + 1) * 10]
    return [
        [int(i) for i in line]
        for line in (line[:-1] for line in lines)
    ]


def is_solved(sudoku):
    return all(sudoku[i][j] for i in range(9) for j in range(9))


def solve_n_in_row(sudoku, can_be, n):
    solved = 0
    for i in range(9):
        index = -1
        for j in range(9):
            if can_be[i][j]:
                if index == -1:
                    index = j
                else:
                    index = -2
        if index > -1:
            solved += 1
            sudoku[i][index] = n
    return solved


def solve_n_in_column(sudoku, can_be, n):
    solved = 0
    for i in range(9):
        index = -1
        for j in range(9):
            if can_be[j][i]:
                if index == -1:
                    index = j
                else:
                    index = -2
        if index > -1:
            solved += 1
            sudoku[index][i] = n
    return solved


def solve_n_in_square(sudoku, can_be, n):
    solved = 0
    for isq in range(3):
        for jsq in range(3):
            index_i = -1
            index_j = -1
            for i in range(3 * isq, 3 * (isq + 1)):
                for j in range(3 * jsq, 3 * (jsq + 1)):
                    if not can_be[i][j]:
                        pass
                    elif index_i == -1:
                        index_i = i
                        index_j = j
                    else:
                        index_i = -2
            if index_i > -1:
                solved += 1
                sudoku[index_i][index_j] = n
    return solved


def solve_n(sudoku, can_be, n):
    return (
        solve_n_in_row(sudoku, can_be, n) +
        solve_n_in_column(sudoku, can_be, n) +
        solve_n_in_square(sudoku, can_be, n)
    )


def deduct(sudoku):
    solved = 0
    lst = {i: where_can_be(sudoku, i) for i in range(1, 10)}
    for i in range(9):
        for j in range(9):
            num = -1
            for n in range(1, 10):
                if lst[n][i][j]:
                    if num == -1:
                        num = n
                    else:
                        num = -2
            if num > -1:
                sudoku[i][j] = num
                solved += 1
    return solved


def guess(sudoku, n):
    can_be = where_can_be(sudoku, n)
    for i in range(9):
        for j in range(9):
            if can_be[i][j]:
                sudoku[i][j] = n
                return True
    return False


def solve(sudoku):
    while not is_solved(sudoku):
        check_progress = copy.deepcopy(sudoku)
        solved = 0
        for i in range(1, 10):
            can_be = where_can_be(sudoku, i)
            solved += solve_n(sudoku, can_be, i)
        if solved == 0:
            solved += deduct(sudoku)
        if solved == 0:
            for i in range(1, 10):
                sudoku_copy = copy.deepcopy(sudoku)
                if guess(sudoku_copy, i):
                    solution = solve(sudoku_copy)
                    if correct(solution):
                        return solution
        # incorrect guess sometimes loops infinitely
        if sudoku == check_progress:
            break
    return sudoku


def empty(sudoku):
    return [[1 if sudoku[i][j] == 0 else 0 for j in range(9)] for i in range(9)]


def where_can_be(sudoku, n):
    can_be = empty(sudoku)
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == n:
                for k in range(9):
                    can_be[i][k] = 0
                    can_be[k][j] = 0
                for k in range(3 * (i // 3), 3 * (i // 3 + 1)):
                    for q in range(3 * (j // 3), 3 * (j // 3 + 1)):
                        can_be[k][q] = 0
    return can_be


def correct(sudoku):
    for n in range(1, 10):
        for i in range(9):
            count = 0
            for j in range(9):
                if sudoku[i][j] == n:
                    count += 1
            if count != 1:
                return False
    for n in range(1, 10):
        for i in range(9):
            count = 0
            for j in range(9):
                if sudoku[j][i] == n:
                    count += 1
            if count != 1:
                return False
    return True


def main():
    result = 0
    lines = open('../txt/problem096.txt').readlines()
    for n in range(len(lines) // 10):
        sudoku = load(n, lines)
        solution = solve(sudoku)
        result += 100 * solution[0][0] + 10 * solution[0][1] + solution[0][2]
    return result


if __name__ == '__main__':
    print(main())
