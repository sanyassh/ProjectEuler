import collections

import euler


ANSWER = 18769


def word_anagram(word1, word2):
    return all(word1.count(letter) == word2.count(letter) for letter in word1)


def word_mask(word):
    mask = collections.defaultdict(list)
    for i, letter in enumerate(word):
        mask[letter].append(i)
    return mask


def suit_mask(mask1, mask2):
    return all(lst in mask2.values() for lst in mask1.values())


def form(square, word1, word2):
    d = {}
    for letter in word1[::-1]:
        d[letter] = square % 10
        square //= 10
    result = 0
    for letter in word2:
        result = result * 10 + d[letter]
    return result


def main():
    lst = euler.data(__file__)[0][1:-1].split('","')

    word_dict = collections.defaultdict(list)
    for word in lst:
        word_dict[len(word)].append(word)

    word_pairs = []
    for lst in word_dict.values():
        for j, word1 in enumerate(lst):
            for word2 in lst[j + 1:]:
                if word_anagram(word1, word2):
                    word_pairs.append((word1, word2))

    squares = []
    j = 1
    for i in range(10):
        squares.append(set())
        ten = 10 ** i
        while j ** 2 < ten:
            squares[i].add(j ** 2)
            j += 1

    result = 0
    for word1, word2 in word_pairs:
        length = len(word1)
        mask = word_mask(word1)
        for square in squares[length]:
            if suit_mask(word_mask(str(square)), mask):
                n = form(square, word1, word2)
                if n in squares[length] and n > result:
                    result = n
    return result


if __name__ == '__main__':
    print(main())
