ANSWER = 518408346
LIMIT = 10 ** 9
SLOW = True


def brute_force():
    total = 0
    for n in range(4, LIMIT // 3 + 3, 2):
        p_1 = 3 * n + 2
        p_2 = p_1 - 4
        c_1, c_2 = p_1 * (n + 2), p_2 * (n - 2)
        if c_1 == round(c_1 ** 0.5) ** 2:
            total += p_1
        if c_2 == round(c_2 ** 0.5) ** 2:
            total += p_2
    return total


def brute_force_2():
    total = 0
    for z in range(1, int(LIMIT / 16.392)):
        z28 = (z * z) << 3
        z2plus = (z << 1) + 1
        x_1 = (-z2plus + ((z2plus * z2plus) + z28) ** 0.5) / 2
        if x_1.is_integer():
            p_1 = round(6 * x_1 + 12 * z + 2)
            total += p_1
        else:
            z2minus = (z << 1) - 1
            x_2 = (-z2minus + ((z2minus * z2minus) + z28) ** 0.5) / 2
            if x_2.is_integer():
                p_2 = round(6 * x_2 + 12 * z - 2)
                total += p_2
    return total


def main():
    return brute_force_2()


if __name__ == '__main__':
    print(main())
