from fractions import Fraction
import collections

import euler


ANSWER = 301
LIMIT = 80


PRIME_LST = euler.prime_list(LIMIT + 1)
FRACTIONS = [Fraction(1, n * n) if n else 0 for n in range(LIMIT + 1)]


def prepare_dict_23():
    set23 = [0]
    for n in range(3, LIMIT + 1):
        if euler.prime_divisors(n, PRIME_LST) <= {2, 3}:
            new_set23 = set23.copy()
            for f in set23:
                new_set23.append(f + FRACTIONS[n])
            set23 = new_set23
    dict_23 = collections.defaultdict(int)
    for f in set23:
        dict_23[f] += 1
    return dict_23


def prepare_fraction_sets():
    sets = {5: [[]], 7: [[]], 13: [[]]}
    for prime in [5, 7, 13]:
        sums = [FRACTIONS[i] for i in range(LIMIT // prime + 1)]
        indices_lst = [[i] for i in range(LIMIT // prime + 1)]
        for _ in range(LIMIT // prime):
            new_indices_lst = []
            new_sums = []
            for summ, indices in zip(sums, indices_lst):
                for i in range(1, indices[-1]):
                    f = summ + FRACTIONS[i]
                    new_indices = indices + [i]
                    if f.numerator % (prime * prime) == 0:
                        sets[prime].append(new_indices)
                    new_sums.append(f)
                    new_indices_lst.append(new_indices)
            indices_lst = new_indices_lst
            sums = new_sums
    fractions_set = {n: [] for n in sets}
    for n in sets:
        for lst in sets[n]:
            fractions_set[n].append({FRACTIONS[i * n] for i in lst})
    return fractions_set


def main():
    dict_23 = prepare_dict_23()
    fraction_sets = prepare_fraction_sets()
    result = 0
    for set5 in fraction_sets[5]:
        for set7 in fraction_sets[7]:
            for set13 in fraction_sets[13]:
                union = set5 | set7 | set13
                result += dict_23[Fraction(1, 4) - sum(union)]
    return result


if __name__ == '__main__':
    print(main())
