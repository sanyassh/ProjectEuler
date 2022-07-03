import euler


ANSWER = 44680
SLOW = True


def main():
    str_lst = [
        str(prime) for prime in euler.prime_list(10 ** 8)
        if euler.is_pandigital_without_zero(prime)
    ]
    total = 0
    str_array = ['']
    index_array = [-1]
    lst_length = len(str_lst)
    while str_array:
        string1 = str_array.pop()
        ind = index_array.pop()
        for i in range(ind + 1, lst_length):
            new = string1 + str_lst[i]
            length = len(new)
            if length > 9:
                break
            if euler.is_pandigital_without_zero(new):
                if length == 9:
                    total += 1
                else:
                    str_array.append(new)
                    index_array.append(i)
    return total


if __name__ == '__main__':
    print(main())
