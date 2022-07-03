ANSWER = 8581146
LIMIT = 10 ** 7
SLOW = True


def square(n):
    return sum(int(digit) ** 2 for digit in str(n))


def main():
    lst = list(range(1000))
    total = 0
    for n in range(1, LIMIT):
        temp = n
        while True:
            temp = square(temp)
            if lst[temp] == 1:
                break
            if lst[temp] == 89:
                total += 1
                break
        if n < 1000:
            lst[n] = lst[temp]
    return total


if __name__ == '__main__':
    print(main())
