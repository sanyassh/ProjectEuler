import euler


ANSWER = 409511334375


def strings_of_len_n(n):
    return (2**n-n-1)*euler.combination(26, n)


def main():
    return max(strings_of_len_n(n) for n in range(2, 26 + 1))


if __name__ == '__main__':
    print(main())
