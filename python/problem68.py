import itertools


ANSWER = 6531031914842725


def get_internal(external):
    result = [0, 0, 0, 0, 0]
    result[2] = external[0] - external[1]
    result[3] = external[4] - external[3]
    result[1] = result[3] + external[2] - external[1]
    result[4] = result[1] + external[0] - external[4]
    if len(set(result)) < 5:
        return None
    if max(result) - min(result) != 4:
        return None
    return [n + 5 - max(result) for n in result]


def main():
    maximum = 0
    lst = [7, 8, 9, 10]
    for permutation in itertools.permutations(lst, len(lst)):
        external = [6] + list(permutation)
        internal = get_internal(external)
        if internal:
            ring = ''
            for i in range(5):
                ring += str(external[i])
                ring += str(internal[i])
                ring += str(internal[(i + 1) % 5])
            maximum = max(maximum, int(ring))
    return maximum


if __name__ == '__main__':
    print(main())
