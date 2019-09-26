ANSWER = 171
START = 1901
STOP = 2001


MONTHS = [31,
          28,
          31,
          30,
          31,
          30,
          31,
          31,
          30,
          31,
          30,
          31]


def is_leap(year):
    if year % 4:
        return False
    if year % 100:
        return True
    if year % 400:
        return False
    return True


def main():
    temp = 1
    year = START
    result = 0
    while year != STOP:
        MONTHS[1] = 28 + is_leap(year)
        for i in range(12):
            temp = (temp + MONTHS[i]) % 7
            if temp == 6:
                result += 1
        year += 1
    return result


if __name__ == '__main__':
    print(main())
