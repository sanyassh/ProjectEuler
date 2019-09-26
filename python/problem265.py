ANSWER = 209110240768
LIMIT = 5


def main():
    strings = ['0' * LIMIT]
    for _ in range(2 ** LIMIT - 1):
        new_strings = []
        for string in strings:
            for digit in '01':
                new_string = string + digit
                if new_string[-LIMIT:] not in string:
                    new_strings.append(new_string)
        strings = new_strings
    return sum(int(string[:-LIMIT + 1], 2) for string in strings)


if __name__ == '__main__':
    print(main())
