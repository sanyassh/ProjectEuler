import string
import itertools


ANSWER = 129448


def decrypt(lst, key):
    text = []
    i = 0
    key_len = len(key)
    for n in lst:
        text.append(chr(n ^ key[i]))
        i = (i + 1) % key_len
    return ''.join(text)


def is_word(word):
    for symbol in word:
        if symbol not in string.ascii_letters:
            return False
    return True


def main():
    lst = [int(n) for n in open('../txt/problem059.txt').readline().split(',')]
    spaces = len(lst) // 10
    keyset = [ord(s) for s in string.ascii_lowercase]
    for key in itertools.product(keyset, repeat=3):
        text = decrypt(lst, key)
        if text.count(' ') < spaces:
            continue
        words = text.split()
        count = sum(is_word(word) for word in words)
        if count < len(words) / 1.5:
            continue
        for symbol in text:
            if symbol not in string.printable:
                break
        else:
            return sum(ord(s) for s in text)
    return 0


if __name__ == '__main__':
    print(main())
