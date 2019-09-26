ANSWER = 21124
# LIMIT


ONES = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    ]

TENS = [
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen',
    ]

BIG_TENS = [
    '',
    '',
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety',
    ]


def count(num):
    result = 0
    if (num // 100) and (num % 100):
        result += len('and')

    rest = num // 100
    if rest:
        result += len(ONES[rest]) + len('hundred')

    rest = (num // 10) % 10
    if rest:
        if rest == 1:
            rest2 = num % 10
            result += len(TENS[rest2])
            return result
        result += len(BIG_TENS[rest])

    rest = num % 10
    if rest:
        result += len(ONES[rest])
    return result


def main():
    result = len('one') + len('thousand')
    for num in range(1, 1000):
        result += count(num)
    return result


if __name__ == '__main__':
    print(main())
