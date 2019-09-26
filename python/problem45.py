import euler


ANSWER = 1533776805


def main():
    t_index = 285
    p_index = 165
    h_index = 143
    pentagonal = euler.pentagonal(p_index)
    hexagonal = euler.hexagonal(h_index)
    while True:
        t_index += 1
        triangular = euler.triangular(t_index)
        if triangular > pentagonal:
            p_index += 1
            pentagonal = euler.pentagonal(p_index)
        if triangular > hexagonal:
            h_index += 1
            hexagonal = euler.hexagonal(h_index)
        if triangular == pentagonal == hexagonal:
            break
    return triangular


if __name__ == '__main__':
    print(main())
