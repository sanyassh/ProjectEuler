ANSWER = 4617456485273129588
LIMIT = 13082761331670030


def main():
    return sum(
        i
        for i in range(153416670 + 1, LIMIT, 153416670)
        if pow(i, 3) % LIMIT == 1
    )


if __name__ == '__main__':
    print(main())
