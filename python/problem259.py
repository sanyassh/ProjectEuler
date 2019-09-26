ANSWER = 20101196798


class MyFraction:
    """ Don't use fractions.Fraction because they are much slower"""

    __slots__ = ('numerator', 'denominator')

    def __init__(self, a, b=1):
        self.numerator = a
        self.denominator = b

    def __add__(self, other):
        return MyFraction(
            self.numerator * other.denominator +
            self.denominator * other.numerator,
            self.denominator * other.denominator
        )

    def __sub__(self, other):
        return MyFraction(
            self.numerator * other.denominator -
            self.denominator * other.numerator,
            self.denominator * other.denominator
        )

    def __mul__(self, other):
        return MyFraction(
            self.numerator * other.numerator,
            self.denominator * other.denominator
        )

    def __truediv__(self, other):
        return MyFraction(
            self.numerator * other.denominator,
            self.denominator * other.numerator
        )

    def __hash__(self):
        return hash(self.numerator / self.denominator)

    def __eq__(self, other):
        return (
            self.numerator * other.denominator ==
            other.numerator * self.denominator
        )


def two_comb(a, b):
    if isinstance(a, str):
        fraction_a = MyFraction(int(a))
        if isinstance(b, str):
            fraction_b = MyFraction(int(b))
            str_ab = a + b
            return {
                fraction_a + fraction_b, fraction_a - fraction_b,
                fraction_a * fraction_b, fraction_a / fraction_b, str_ab
            }
        if b.numerator:
            return {
                fraction_a + b, fraction_a - b, fraction_a * b, fraction_a / b
            }
        return {fraction_a, MyFraction(0)}
    if isinstance(b, str):
        fraction_b = MyFraction(int(b))
        return {a + fraction_b, a - fraction_b, a * fraction_b, a / fraction_b}
    if b.numerator:
        return {a + b, a - b, a * b, a / b}
    return {a, MyFraction(0)}


def multi_comb(lst):
    length = len(lst)
    if length == 1:
        return {lst[0]}
    if length == 2:
        return two_comb(lst[0], lst[1])
    result = set()
    for i in range(1, length):
        part1 = multi_comb(lst[:i])
        part2 = multi_comb(lst[i:])
        for a in part1:
            for b in part2:
                result.update(two_comb(a, b))
    return result


def main():
    numbers = multi_comb([str(i) for i in range(1, 9 + 1)])
    natural_numbers = set()
    for n in numbers:
        if isinstance(n, str):
            n = MyFraction(int(n))
        if n.numerator * n.denominator > 0:
            if not n.numerator % n.denominator:
                natural_numbers.add(n.numerator // n.denominator)
    return sum(natural_numbers)


if __name__ == '__main__':
    print(main())
