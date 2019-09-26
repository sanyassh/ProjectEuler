import collections


ANSWER = 21295121502550


Pair = collections.namedtuple('Pair', ['n', 'count'])
Interval = collections.namedtuple('Interval', ['pair1', 'pair2', 'delta'])


def work_with_interval(interval, digit, diffs):
    pairs = [interval.pair1]
    n = interval.pair1.n
    count = interval.pair1.count
    delta = interval.delta
    while n < interval.pair2.n:
        count += diffs[delta].count
        count += (
            delta *
            str((n + 1) // delta).count(str(digit))
        )
        n += delta
        pairs.append(Pair(n, count))
    intervals = []
    delta //= 10
    for i in range(len(pairs) - 1):
        if (
                pairs[i].n <= pairs[i + 1].count and
                pairs[i].count <= pairs[i + 1].n
        ):
            intervals.append(
                Interval(pairs[i], pairs[i + 1], delta)
            )
    return intervals


def main():
    base = []
    diffs = {}
    for power in range(21):
        n, count = 10 ** power - 1, int(power * 10 ** (power - 1))
        pair = Pair(n, count)
        diff = Pair(n + 1, count)
        base.append(pair)
        diffs[diff.n] = diff
    total = 0
    for i in range(len(base) - 1):
        start_interval = Interval(base[i], base[i + 1], base[i].n + 1)
        for digit in range(1, 10):
            delta = start_interval.delta
            intervals = [start_interval]
            while delta:
                delta //= 10
                new_intervals = []
                for interval in intervals:
                    new_intervals.extend(
                        work_with_interval(interval, digit, diffs)
                    )
                intervals = new_intervals
            for interval in intervals:
                if interval.pair1.n == interval.pair1.count:
                    total += interval.pair1.n
    return total


if __name__ == '__main__':
    print(main())
