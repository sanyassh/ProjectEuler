ANSWER = 837799
LIMIT = 1000000


def main():
    tab = [0, 1]
    for i in range(2, LIMIT):
        temp = i
        length = 0
        while temp >= i:
            if temp % 2:
                temp = temp * 3 + 1
            else:
                temp //= 2
            length += 1
        tab.append(length + tab[temp])
    return tab.index(max(tab))


if __name__ == '__main__':
    print(main())
