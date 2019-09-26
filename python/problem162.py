ANSWER = '3D58725572C62302'
LIMIT = 16


def main():
    d = {
        '': 13,
        'A': 1,
        '1': 1,
        '0': 0,
        '1A': 0,
        '0A': 0,
        '01': 0,
        '01A': 0,
    }
    total = 0
    for _ in range(LIMIT - 1):
        new_d = {
            '': d[''] * 13,
            'A': d['A'] * 14 + d[''],
            '1': d['1'] * 14 + d[''],
            '0': d['0'] * 14 + d[''],
            '1A': d['1A'] * 15 + d['1'] + d['A'],
            '0A': d['0A'] * 15 + d['0'] + d['A'],
            '01': d['01'] * 15 + d['0'] + d['1'],
            '01A': d['01A'] * 16 + d['01'] + d['0A'] + d['1A'],
        }
        total += new_d['01A']
        d = new_d
    return format(total, 'x').upper()


if __name__ == '__main__':
    print(main())
