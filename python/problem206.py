ANSWER = 1389019170
LIMIT = '1_2_3_4_5_6_7_8_9_0'


def main():
    i = int(int(LIMIT.replace('_', '0')) ** 0.5)
    while True:
        i += 10
        s = str(i ** 2)
        for dig1, dig2 in zip(LIMIT, s):
            if '_' != dig1 != dig2:
                break
        else:
            return i
        if s[2] > '2':
            i += 400000
        elif s[2] < '1':
            i += 400000
        elif s[4] > '3':
            i += 4000
        elif s[4] < '2':
            i += 4000
        elif s[6] > '4':
            i += 40
        elif s[6] < '3':
            i += 40


if __name__ == '__main__':
    print(main())
