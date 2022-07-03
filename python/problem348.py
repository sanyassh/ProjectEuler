import collections


ANSWER = 1004195061
SLOW = True


def main():
    d = collections.defaultdict(int)
    cubes = [c * c * c for c in range(1000)]
    for i in range(1, 80000):
        i_2 = i * i
        for j in range(1, 1000):
            a = i_2 + cubes[j]
            s = str(i_2 + cubes[j])
            if s == s[::-1]:
                d[a] += 1
    total = 0
    n = 0
    for number in sorted(d.keys()):
        if d[number] == 4:
            total += number
            n += 1
            if n == 5:
                break
    return total


if __name__ == '__main__':
    print(main())
