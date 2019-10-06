import euler


ANSWER = 5673835352990
LIMIT = 30


def main():
    count = 0
    total = 0
    squares = [i * i for i in range(10000000)]
    ratios = [0.1, 0.1]
    for n in range(2, 10000000):
        n_2 = squares[n]
        for m in range(int(n * ratios[0]), n):
            m_2 = squares[m]
            m_n = m * n
            divisor = n_2 - m_n - m_2
            if divisor <= 0:
                break
            if euler.gcd1(m, n):
                numerator = m_n + 3 * m_2
                if numerator % divisor == 0:
                    ratios.append(m / n)
                    ratios.sort()
                    ratios.pop(0)
                    count += 1
                    total += numerator // divisor
                    if count == LIMIT:
                        return total
    return count


if __name__ == '__main__':
    print(main())
