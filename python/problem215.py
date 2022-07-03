ANSWER = 806844323190414
LENGTH = 32
HEIGHT = 10


def build_walls():
    walls = []
    indices = [0]
    builds = [[0 for _ in range(LENGTH + 1)]]
    while indices:
        index = indices.pop()
        build = builds.pop()
        if index == LENGTH - 3:
            walls.append(build)
        elif index == LENGTH - 2:
            walls.append(build)
        elif index != LENGTH - 1:
            for addition in 2, 3:
                indices.append(index + addition)
                new_build = build[:]
                new_build[index + addition] = 1
                builds.append(new_build)
    return walls


def main():
    walls = build_walls()
    length = len(walls)
    can = [[1 for _ in range(length)] for _ in range(length)]
    for i in range(length):
        for j in range(i + 1, length):
            can[i][j] = not any(
                crack1 and crack2
                for crack1, crack2 in zip(walls[i], walls[j])
            )
    for i in range(length):
        can[i][i] = 0
        for j in range(i + 1, length):
            can[j][i] = can[i][j]
    counts = [1 for _ in range(length)]
    for _ in range(HEIGHT - 1):
        new_counts = [0 for _ in range(length)]
        for i in range(length):
            c = counts[i]
            for j in range(length):
                if can[i][j]:
                    new_counts[j] += c
        counts = new_counts
    return sum(counts)


if __name__ == '__main__':
    print(main())
