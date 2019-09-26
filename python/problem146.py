import euler


ANSWER = 676333270
ADDITIONS = [1, 3, 7, 9, 13, 27]
LIMIT = 150 * 10 ** 6


def prepare_lst():
    prime_list = euler.prime_list(1000)
    prime_list.remove(2)
    lst = {2}
    prod = 2
    for prime in prime_list:
        rest = set()
        for i in range(prime):
            q = i * i
            for j in ADDITIONS:
                if not (q + j) % prime:
                    break
            else:
                rest.add(i)
        new_lst = set()
        for a in lst:
            for i in range(prime):
                q = a + prod * i
                if q < LIMIT:
                    if q % prime in rest:
                        new_lst.add(q)
                else:
                    break
        lst = new_lst
        prod *= prime
    return lst


def main():
    lst = prepare_lst()
    result = {10}
    for a in sorted(lst):
        for addition in ADDITIONS:
            if not euler.miller_rabin(a * a + addition):
                break
        else:
            for addition in (19, 21):
                if euler.miller_rabin(a * a + addition):
                    break
            else:
                result.add(a)
    return sum(result)


if __name__ == '__main__':
    print(main())
