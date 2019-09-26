import functools
import itertools


ANSWER = '1,13717420,8'
RECURSIVE_LIMIT = 10 ** 1000
LIMIT_F_N, LIMIT_F_N_1 = 123456789, 987654321


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


def wtf(j):
    i = 0
    while j > 2 ** i - 1:
        i += 1
    return i


def pos(j, i):
    return 2 ** (wtf(j) + i) + j


def is_power2(n):
    while not n & 1:
        n >>= 1
    return n == 1


def find(i, f_n, f_n_1):
    a = calc(pos(i, 0))
    b = calc(pos(i, 1)) - a
    c = calc(pos(i + 1, 0))
    d = calc(pos(i + 1, 1)) - c
    if is_power2(i + 1):
        c -= d
    num = c * f_n_1 - a * f_n
    denom = b * f_n - d * f_n_1
    if denom == 0 or num % denom != 0:
        return -1
    return num // denom


def _sbe(n):
    temp = n & 1
    count = 0
    s = []
    while n:
        while n & 1 == temp:
            count += 1
            n >>= 1
        s.insert(0, count)
        temp = 1 - temp
        count = 0
    return s


def sbe(i, j):
    sbe_list = _sbe(pos(i, 0) + 1)
    if j > 0:
        sbe_list[0] -= 1
        return '1,' + str(j) + ',' + ','.join(str(s) for s in sbe_list)
    return ','.join(str(s) for s in sbe_list)


def main():
    for i in itertools.count():
        found = find(i, LIMIT_F_N, LIMIT_F_N_1)
        if found >= 0:
            return sbe(i, found)
    return 0


if __name__ == '__main__':
    print(main())
