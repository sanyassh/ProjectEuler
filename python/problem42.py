import euler


ANSWER = 162


def main():
    lst = open('../txt/problem042.txt').readline()[1:-1].split('","')
    triangles = {euler.triangular(i) for i in range(1, 50)}
    return sum(euler.alphabetical_value(word) in triangles for word in lst)


if __name__ == '__main__':
    print(main())
