ANSWER = 1587000


def is_increasing(n):
    str_n = str(n)
    for i in range(len(str_n)-1):
        if str_n[i] > str_n[i+1]:
            return False
    return True


def is_decreasing(n):
    str_n = str(n)
    for i in range(len(str_n)-1):
        if str_n[i] < str_n[i+1]:
            return False
    return True


def is_bouncy(n):
    return not (is_increasing(n) or is_decreasing(n))


def main():
    i = 21780
    bouncy = i - 2178
    while bouncy / i < 0.99:
        i += 1
        bouncy += is_bouncy(i)
    return i


if __name__ == '__main__':
    print(main())
