ANSWER = 49


def main():
    return sum(
        len(str(i ** j)) == j
        for i in range(1, 100)
        for j in range(1, 200)
    )


if __name__ == '__main__':
    print(main())
