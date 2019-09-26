import euler


ANSWER = 5482660


def main():
    lst = [euler.pentagonal(i) for i in range(100000)]
    s = set(lst)
    for k in range(1, 100000):
        penta_k = lst[k]
        for j in range(1, k):
            penta_j = lst[j]
            if penta_k - penta_j in s:
                if penta_k + penta_j in s:
                    return penta_k - penta_j
    return 0


if __name__ == '__main__':
    print(main())
