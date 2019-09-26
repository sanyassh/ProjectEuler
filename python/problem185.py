import itertools


ANSWER = 4640261571849533
SLOW = True

DIGITS = {str(d) for d in range(10)}
GUESSES = [
    '5616185650518293',
    '3847439647293047',
    '5855462940810587',
    '9742855507068353',
    '4296849643607543',
    '3174248439465858',
    '4513559094146117',
    '7890971548908067',
    '8157356344118483',
    '2615250744386899',
    '8690095851526254',
    '6375711915077050',
    '6913859173121360',
    '6442889055042768',
    '2321386104303845',
    '2326509471271448',
    '5251583379644322',
    '1748270476758276',
    '4895722652190306',
    '3041631117224635',
    '1841236454324589',
    '2659862637316867',
]
HITS = [
    2,
    1,
    3,
    3,
    3,
    1,
    2,
    3,
    1,
    2,
    3,
    1,
    1,
    2,
    0,
    2,
    2,
    3,
    1,
    3,
    3,
    2,
]
LEN_GUESSES = len(GUESSES)
LEN_STRING = len(GUESSES[0])


def iteration_with_no_hits(result, available_indices):
    index = available_indices[0]
    for d in DIGITS:
        for guess in GUESSES:
            if guess[index] == d:
                break
        else:
            new_result = {index: d}
            new_result.update(result)
            new_available_indices = available_indices.copy()
            new_available_indices.remove(index)
            yield new_result, new_available_indices


def iteration(result, start_hits, available_indices):
    max_hits = max(start_hits)
    max_hits_index = start_hits.index(max_hits)
    if not available_indices:
        yield result, start_hits, available_indices
        return
    if max_hits == 0:
        for new_result, new_available_indices in iteration_with_no_hits(
                result, available_indices
        ):
            yield new_result, start_hits, new_available_indices
        return
    for i, comb in enumerate(
            itertools.combinations(available_indices, max_hits)
    ):
        new_result = {index: GUESSES[max_hits_index][index] for index in comb}
        new_result.update(result)
        new_available_indices = [i for i in available_indices if i not in comb]
        hits = start_hits.copy()
        possible = True
        for j in range(LEN_GUESSES):
            for index in comb:
                if GUESSES[max_hits_index][index] == GUESSES[j][index]:
                    hits[j] -= 1
                    if hits[j] < 0:
                        possible = False
                        break
            if not possible:
                break
        if possible:
            yield new_result, hits, new_available_indices


def build(result):
    lst = ['x' for _ in range(LEN_STRING)]
    for i in result:
        lst[i] = result[i]
    return ''.join(lst)


def check(string):
    return HITS == [
        sum(string[i] == GUESSES[j][i] for i in range(LEN_STRING))
        for j in range(LEN_GUESSES)
    ]


def main():
    result = {}
    available_indices = list(range(LEN_STRING))
    hits = HITS
    parameters = [(result, hits, available_indices)]
    for _ in range(LEN_STRING):
        parameters = [
            params
            for old_params in parameters
            for params in iteration(*old_params)
        ]
    for result, _, _ in parameters:
        string = build(result)
        if check(string):
            return string
    return 0


if __name__ == '__main__':
    print(main())
