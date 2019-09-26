import euler


ANSWER = 248155780267521
LIMIT = 30


def main():
    lst = []
    for i in range(2, 500):
        for j in range(2, 50):
            num = i ** j
            if euler.digit_sum(num) == i:
                lst.append(num)
    lst.sort()
    return lst[LIMIT - 1]


if __name__ == '__main__':
    print(main())
