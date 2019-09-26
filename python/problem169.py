import functools


ANSWER = 178653872807
LIMIT = 10 ** 25  # no more that 10 ** 25000
RECURSIVE_LIMIT = 10 ** 1000


@functools.lru_cache(None)
def _recursive_calc(n):
    if n < 2:
        return 1
    if n & 1:
        return calc(n >> 1)
    r = 0
    while not n & 1:
        n >>= 1
        r += 1
    n >>= 1
    return _recursive_calc(n) + r * _recursive_calc(n << 1)


@functools.lru_cache(None)
def _iterative_calc(n):
    labels = [0]
    results = {}
    local_variables = []
    args = [n]
    while args:
        label = labels.pop()
        arg = args.pop()
        if label == 0:
            if arg in results:
                pass
            elif arg < 2:
                results[arg] = 1
            elif n & 1:
                labels.extend([1, 0])
                args.extend([arg, arg >> 1])
            else:
                r = 0
                save_arg = arg
                while not arg & 1:
                    arg >>= 1
                    r += 1
                arg >>= 1
                labels.extend([2, 0, 0])
                args.extend([save_arg, arg, arg << 1])
                local_variables.append([save_arg, r, arg, arg << 1])
        if label == 1:
            results[arg] = results[arg >> 1]
        if label == 2:
            save_arg, r, first_arg, second_arg = local_variables.pop()
            results[save_arg] = results[first_arg] + r * results[second_arg]
    return results[n]


@functools.lru_cache(None)
def calc(n):
    if n > RECURSIVE_LIMIT:
        return _iterative_calc(n)
    return _recursive_calc(n)


def main():
    return calc(LIMIT)


if __name__ == '__main__':
    print(main())
