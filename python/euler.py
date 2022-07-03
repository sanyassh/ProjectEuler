"""
SLOW = True - mark for problem solutions that run slower than 10 seconds
"""


import array
import functools
import math
import operator
import os
import re
import string


SQRT_LIMIT = 10 ** 14


FACTORIALS = [1]
for _ in range(1, 1001):
    FACTORIALS.append(FACTORIALS[-1] * _)


def data(filename):
    number = re.search(r'problem(?P<number>(\d)*).py', filename).group('number')
    number = '0' * (3 - len(number)) + number
    data_path = os.path.abspath(
        os.path.join(__file__, '..', '..', 'txt', f'problem{number}.txt')
    )
    with open(data_path, encoding='utf-8') as file:
        return file.readlines()


# divisors


def divisors(n):
    d = set()
    sqrt = int_sqrt(n)
    for i in range(1, sqrt + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return d


def divisors_list(n):
    result = [[] for _ in range(n)]
    for i in range(1, n):
        for j in range(i, n, i):
            result[j].append(i)
    return result


def prime_divisors(n, prime_lst=None):
    d = set()
    sqrt = int_sqrt(n) + 1
    i = 0 if prime_lst else 2
    prime_lst = prime_lst or list(range(sqrt + 1))
    prime = prime_lst[i]
    while prime < sqrt and n > 1:
        if not n % prime:
            d.add(prime)
            while not n % prime:
                n //= prime
        i += 1
        prime = prime_lst[i]
    if n > 1:
        d.add(n)
    return d


def low_divisors(n):
    d = set()
    sqrt = int_sqrt(n)
    for i in range(1, sqrt + 1):
        if n % i == 0:
            d.add(i)
    return d


def count_divisors(n):
    d = 0
    sqrt = int_sqrt(n)
    for i in range(1, sqrt + 1):
        if n % i == 0:
            d += 2
    if n == sqrt * sqrt:
        d -= 1
    return d


def count_prime_divisors(n, prime_lst=None):
    count = 0
    sqrt = int_sqrt(n) + 1
    prime_lst = prime_lst or list(range(2, sqrt))
    i = 0
    prime = prime_lst[i]
    while prime < sqrt:
        if not n % prime:
            count += 1
            while not n % prime:
                n //= prime
            sqrt = int_sqrt(n) + 1
        i += 1
        prime = prime_lst[i]
    if n > 1:
        count += 1
    return count


def sum_divisors(n):
    d = 1
    sqrt = int_sqrt(n)
    for i in range(2, sqrt + 1):
        if n % i == 0:
            d += i + n // i
    if n == sqrt * sqrt:
        d -= sqrt
    return d


def gcd1(a, b):
    return math.gcd(a, b) == 1


def is_not_divisible(num, lst, ind):
    # ind = len(lst)
    result = num
    for i in range(ind):
        r = num // lst[i]
        if not r:
            break
        result -= is_not_divisible(r, lst, i)
    return result


def max_divisors(iterable):
    lst = list(iterable)
    divisors_lst = [1 for _ in lst]
    length = len(lst)
    for i, n in enumerate(lst):
        if n > 1:
            for j in range(i, length, n):
                if not lst[j] % n:
                    divisors_lst[j] = max(divisors_lst[j], n)
                    while not lst[j] % n:
                        lst[j] //= n
    return divisors_lst


# primes


def _check(a, s, d, n):
    x = pow(a, d, n)
    if x == 1:
        return True
    n_1 = n - 1
    for _ in range(s - 1):
        if x == n_1:
            return True
        x = pow(x, 2, n)
    return x == n_1


def miller_rabin(n, k=10):
    if n < 2:
        return False
    if n < 4:
        return True
    if not n & 1:
        return False
    s = 0
    d = n - 1
    while not d & 1:
        d >>= 1
        s += 1
    for a in range(3, n - 2, max((n - 5) // k, 1)):
        if not _check(a, s, d, n):
            return False
    return True


def is_prime(n, prime_lst=None, prime_lst_with_zeros=None):
    if prime_lst_with_zeros:
        try:
            return bool(prime_lst_with_zeros[n])
        except IndexError:
            pass
    square = int(n ** 0.5)
    prime_lst = prime_lst or range(2, square + 1)
    for prime in prime_lst:
        if prime > square:
            return True
        if not n % prime:
            return False
    return True


def prime_list_with_zeros(n):
    index = array.array('L', (range(n)))
    index[1] = 0
    for i in range(n):
        if index[i]:
            for j in range(2 * i, n, i):
                index[j] = 0
    return index


def clean_zeros(prime_lst):
    return array.array('L', (i for i in prime_lst if i))


def prime_list(n):
    return clean_zeros(prime_list_with_zeros(n))


def list_of_prime_factors(n):
    factors = []
    prime = 2
    while prime <= n:
        if not n % prime:
            factors.append(prime)
            n //= prime
        else:
            prime += 1
    return factors


def prime_cycle_length(prime):
    n = 1
    length = 0
    while True:
        n = (n * 10) % prime
        length += 1
        if n <= 1:
            return length


# pythagorean


def pythagorean_trio(a):
    """Doesn't produce all triplets"""
    a_2 = a * a
    for b in range(1, a):
        b_2 = b * b
        yield a_2 - b_2, 2 * a * b, a_2 + b_2


def pythagorean_trio_my(c):
    c_double = 2 * c
    c_double_square = c_double * c
    for a in low_divisors(c_double_square):
        b = c_double_square // a
        yield a + c_double, b + c_double, a + b + c_double


def pythagorean_unique_trio(a):
    a_2 = a * a
    for b in range(1, a):
        b_2 = b * b
        x = a_2 - b_2
        y = 2 * a * b
        if gcd1(x, y):
            yield x, y, a_2 + b_2


# special numbers


def is_palindrome(num):
    str_n = str(num)
    return str_n == str_n[::-1]


def is_pandigital(n):
    str_n = str(n)
    return len(str_n) == len(set(str_n))


def is_pandigital_without_zero(n):
    str_n = str(n)
    return '0' not in str_n and len(str_n) == len(set(str_n))


def is_pandigital_1n(n):
    str_n = str(n)
    return len(str_n) == len(set(str_n)) == int(max(str_n))


def triangular(n):
    return n * (n + 1) // 2


def pentagonal(n):
    return n * (3 * n - 1) // 2


def hexagonal(n):
    return n * (2 * n - 1)


def is_pentagonal(n):
    a = (1 + (1 + 24 * n) ** 0.5) / 6
    return round(a) == round(a, 7)


# strings


def alphabetical_value(word):
    return sum(string.ascii_uppercase.index(letter) + 1 for letter in word)


# digits


def digit_sum(n):
    return sum(int(digit) for digit in str(n))


# combinatorics


def combination(n, k):
    return FACTORIALS[n] // FACTORIALS[k] // FACTORIALS[n - k]


# other


def product(sequence, initial=1):
    return functools.reduce(operator.mul, sequence, initial)


def int_sqrt(n):
    if n < SQRT_LIMIT:
        return int(n ** 0.5)
    sqrt = 1
    sqr = 1
    while sqr <= n:
        sqrt <<= 1
        sqr <<= 2
    sqrt >>= 1
    temp = sqrt >> 1
    while temp:
        if pow(sqrt + temp, 2) <= n:
            sqrt += temp
        temp >>= 1
    return sqrt


def int_cbrt(n):
    sqrt = 1
    sqr = 1
    while sqr <= n:
        sqrt <<= 1
        sqr <<= 3
    sqrt >>= 1
    temp = sqrt >> 1
    while temp:
        if pow(sqrt + temp, 3) <= n:
            sqrt += temp
        temp >>= 1
    return sqrt


def is_square(n):
    if n > SQRT_LIMIT:
        while not n & 3:
            n >>= 2
        if not n & 1:
            return False
    return pow(int_sqrt(n), 2) == n


def is_cube(n):
    return pow(int_cbrt(n), 3) == n


def totient(n, prime_lst):
    result = n
    for prime in prime_lst:
        if prime > n:
            break
        if n % prime == 0:
            result -= result // prime
    return result


def totient_list(n):
    result = array.array('L', (i for i in range(n)))
    for i in range(2, n):
        if result[i] == i:
            for j in range(i, n, i):
                result[j] -= result[j] // i
    return result


def lagged_fibonacci_generator():
    lst = [
        (100003 - 200003 * i + 300007 * i ** 3) % 1000000 - 500000
        for i in range(56)
    ]
    for n in lst:
        yield n
    while True:
        lst.append((lst[-24] + lst[-55]) % 1000000 - 500000)
        lst.pop(0)
        yield lst[-1]


def parse_fraction(lst):
    b = 1
    a = lst[-1]
    for i in range(len(lst) - 1):
        a, b = a * lst[-2 - i] + b, a
    return a, b


def square_fraction(n, length):
    sqrt = n ** 0.5
    a = int(sqrt)
    diff = -a
    denom = 1
    current_length = 0
    lst = []
    while True:
        lst.append(a)
        current_length += 1
        denom = (n - diff * diff) // denom
        a = int((sqrt - diff) / denom)
        diff = -diff - a * denom
        if current_length > length:
            break
    return lst


def max_sum_sub_sequence(sequence):
    old_start, old_end, max_sum, new_start, new_end, temp_sum = 0, 0, 0, 0, 0, 0
    for i, n in enumerate(sequence, start=1):
        new_sum = temp_sum + n
        if new_sum <= 0:
            new_start, new_end = i, i
            temp_sum = 0
        else:
            new_end += 1
            temp_sum = new_sum
        if temp_sum > max_sum:
            max_sum = temp_sum
            old_start, old_end = new_start, new_end
    return old_start, old_end, max_sum
