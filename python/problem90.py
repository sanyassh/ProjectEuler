import itertools


ANSWER = 1217

RULES = {
    0: [[1], [4], [6, 9]],
    1: [[8], [6, 9]],
    2: [[5]],
    3: [[6, 9]],
    4: [[6, 9]],
}


def missing_all(cube, lst):
    for n in lst:
        if cube[n]:
            return False
    return True


def check_rule(cube, need, digit, lists):
    if not cube[digit]:
        for lst in lists:
            if missing_all(cube, lst):
                return False
        need.add((digit,))
    else:
        for lst in lists:
            if missing_all(cube, lst):
                need.add(tuple(lst))
            else:
                need.add(tuple(lst) + (digit,))
    return True


def check_cube(cube):
    need = set()
    for digit, lists in RULES.items():
        if not check_rule(cube, need, digit, lists):
            return None
    return need


def compatible(i, cubes, need):
    result = 0
    for j in range(i, len(cubes)):
        for choice in need:
            for n in choice:
                if cubes[j][n]:
                    break
            else:
                break
        else:
            result += 1
    return result


def main():
    total = 0
    cubes = [
        [i in cube for i in range(10)]
        for cube in itertools.combinations(range(10), 6)
    ]
    for i, cube in enumerate(cubes):
        need = check_cube(cube)
        if need is not None:
            total += compatible(i, cubes, need)
    return total


if __name__ == '__main__':
    print(main())
