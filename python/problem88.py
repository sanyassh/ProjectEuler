import euler


ANSWER = 7587457
LIMIT = 12000


def main():
    arrays = {(2, 2)}
    d = {k: k * 2 for k in range(2, LIMIT + 1)}
    while arrays:
        new_arrays = set()
        for lst in arrays:
            product = euler.product(lst)
            k = product - sum(lst) + len(lst)
            if k > LIMIT:
                continue
            if d[k] > product:
                d[k] = product
            new_arrays.add((lst[0] + 1,) + lst[1:])
            for i in range(1, len(lst)):
                if lst[i - 1] > lst[i]:
                    new_arrays.add(lst[:i] + (lst[i] + 1,) + lst[i + 1:])
            new_arrays.add(lst + (2,))
        arrays = new_arrays
    return sum(set(d.values()))


if __name__ == '__main__':
    print(main())
