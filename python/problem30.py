ANSWER = 443839


def main():
    return sum(
        i for i in range(2, 300000)
        if i == sum(int(digit) ** 5 for digit in str(i))
    )


if __name__ == '__main__':
    print(main())
