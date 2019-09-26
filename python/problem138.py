ANSWER = 1118049290473932


def main():
    lst = [17, 305]
    for _ in range(10):
        lst.append(18 * lst[-1] - lst[-2])
    return sum(lst)


if __name__ == '__main__':
    print(main())
