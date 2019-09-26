ANSWER = 127035954683


def numbers(n):
    str_n = str(n)
    return [str_n.count(str(i)) for i in range(10)]


def main():
    lst = [numbers(i ** 3) for i in range(10000)]
    for i in range(10000):
        if lst.count(lst[i]) == 5:
            return i ** 3
    return 0


if __name__ == '__main__':
    print(main())
