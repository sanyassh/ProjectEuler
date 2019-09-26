ANSWER = 840


def main():
    # (a+n)**2 + (b+n)**2 = (a+b+n)** 2 -> n**2 = 2*a*b
    lst = [0 for _ in range(1001)]
    for n in range(1, 200):
        for a in range(1, 125):
            if n ** 2 % (2 * a) == 0:
                b = n ** 2 // (2 * a)
                p = 2 * a + 2 * b + 3 * n
                if p <= 1000:
                    lst[p] += 1
    return lst.index(max(lst))


if __name__ == '__main__':
    print(main())
