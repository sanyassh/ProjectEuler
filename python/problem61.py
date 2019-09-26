ANSWER = 28684


def condition(n):
    return len(str(n)) == 4 and str(n)[2] != '0'


def main():
    polygonal_numbers = [
        [k for k in (i * (3 * i - 2) for i in range(200)) if condition(k)],
        [k for k in (i * (5 * i - 3) // 2 for i in range(200)) if condition(k)],
        [k for k in (i * (2 * i - 1) for i in range(200)) if condition(k)],
        [k for k in (i * (3 * i - 1) // 2 for i in range(200)) if condition(k)],
        [k for k in (i * i for i in range(200)) if condition(k)],
        [k for k in (i * (i + 1) // 2 for i in range(200)) if condition(k)]
    ]
    starts = [[str(n)[:2] for n in lst] for lst in polygonal_numbers]
    ends = [[str(n)[2:] for n in lst] for lst in polygonal_numbers]
    nums = [[i] for i in range(len(polygonal_numbers[0]))]
    used = [[0] for _ in polygonal_numbers[0]]
    while nums:
        num = nums.pop()
        use = used.pop()
        if len(use) == 6:
            if ends[use[-1]][num[-1]] == starts[use[0]][num[0]]:
                return sum(
                    polygonal_numbers[use[i]][num[i]]
                    for i in range(len(use))
                )
        else:
            for i in set(range(1, 6)) - set(use):
                for j in range(len(starts[i])):
                    if ends[use[-1]][num[-1]] == starts[i][j]:
                        new_use = use + [i]
                        new_num = num + [j]
                        used.append(new_use)
                        nums.append(new_num)


if __name__ == '__main__':
    print(main())
