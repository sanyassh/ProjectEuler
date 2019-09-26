import collections


ANSWER = 1918080160


LateAbsent = collections.namedtuple('LateAbsent', ['late', 'absent'])


def iteration_dct(dct):
    new_dct = {key: 0 for key in dct}
    for key, number in dct.items():
        if key.late:
            new_dct[LateAbsent(1, 0)] += number  # on time
            if key.absent == 0:
                new_dct[LateAbsent(1, 1)] += number  # absent
            if key.absent == 1:
                new_dct[LateAbsent(1, 2)] += number  # absent
        else:
            new_dct[LateAbsent(0, 0)] += number  # on time
            new_dct[LateAbsent(1, 0)] += number  # late
            if key.absent == 0:
                new_dct[LateAbsent(0, 1)] += number  # absent
            if key.absent == 1:
                new_dct[LateAbsent(0, 2)] += number  # absent
    return new_dct


def main():
    dct = {
        LateAbsent(0, 0): 1,
        LateAbsent(0, 1): 0,
        LateAbsent(0, 2): 0,
        LateAbsent(1, 0): 0,
        LateAbsent(1, 1): 0,
        LateAbsent(1, 2): 0,
    }
    for _ in range(30):
        dct = iteration_dct(dct)
    return sum(dct.values())


if __name__ == '__main__':
    print(main())
