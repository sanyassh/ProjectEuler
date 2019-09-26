ANSWER = 743

ROMAN_TO_TEN_MAPPING = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}


def roman_to_ten(roman):
    result = 0
    last = ROMAN_TO_TEN_MAPPING[roman[0]]
    for i in range(1, len(roman)):
        temp = ROMAN_TO_TEN_MAPPING[roman[i]]
        if temp <= last:
            result += last
        else:
            result -= last
        last = temp
    result += last
    return result


def ten_to_roman(n):
    result = ''
    result += 'M' * (n // 1000)
    n %= 1000
    r = n // 100
    if r == 9:
        result += 'CM'
    elif r == 4:
        result += 'CD'
    else:
        if r >= 5:
            result += 'D'
        result += (r % 5) * 'C'
    n %= 100
    r = n // 10
    if r == 9:
        result += 'XC'
    elif r == 4:
        result += 'XL'
    else:
        if r >= 5:
            result += 'L'
        result += (r % 5) * 'X'
    r = n % 10
    if r == 9:
        result += 'IX'
    elif r == 4:
        result += 'IV'
    else:
        if r >= 5:
            result += 'V'
        result += (r % 5) * 'I'
    return result


def main():
    return sum(
        len(line) - len(ten_to_roman(roman_to_ten(line)))
        for line in (line[:-1] for line in open('../txt/problem089.txt'))
    )


if __name__ == '__main__':
    print(main())
