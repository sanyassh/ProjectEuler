import euler


ANSWER = 162


def main():
    lst = euler.data(__file__)[0][1:-1].split('","')
    triangles = {euler.triangular(i) for i in range(1, 50)}
    return sum(euler.alphabetical_value(word) in triangles for word in lst)


if __name__ == '__main__':
    print(main())
