import euler


ANSWER = 376
RANKS = ''.join(str(i) for i in range(10)) + 'TJQKA'


def check_flush(str_hand):
    suit = str_hand[0][1]
    for card in str_hand:
        if card[1] != suit:
            return False
    return True


def check_straight(sort_hand):
    first = sort_hand[0]
    for i in range(1, 5):
        if sort_hand[i] - first != i:
            return False
    return True


def player1_wins(str1, str2):
    return str1 > str2


def construct_detailed_strength(strength, int_hand, count):
    for i in int_hand[::-1]:
        if int_hand.count(i) == count:
            strength.append(i)
    for i in int_hand[::-1]:
        if int_hand.count(i) != count:
            strength.append(i)


def get_strength(hand):
    int_hand = sorted(RANKS.index(card[0]) for card in hand)
    count = [int_hand.count(k) for k in int_hand]
    if check_straight(int_hand):
        if check_flush(hand):
            strength = [9] + int_hand[::-1]
        else:
            strength = [5] + int_hand[::-1]
    elif check_flush(hand):
        strength = [6] + int_hand[::-1]
    else:
        if count.count(4) == 4:
            strength = [8]
            construct_detailed_strength(strength, int_hand, 4)
        elif count.count(3) == 3:
            if count.count(2) == 2:
                strength = [7]
                construct_detailed_strength(strength, int_hand, 3)
            else:
                strength = [4]
                construct_detailed_strength(strength, int_hand, 3)
        elif count.count(2) == 4:
            strength = [3]
            construct_detailed_strength(strength, int_hand, 2)
        elif count.count(2) == 2:
            strength = [2]
            construct_detailed_strength(strength, int_hand, 2)
        else:
            strength = [1] + int_hand[::-1]
    return strength


def main():
    count = 0
    for hands in euler.data(__file__):
        cards = hands.split()
        hand1 = cards[:5]
        hand2 = cards[5:]
        count += player1_wins(get_strength(hand1), get_strength(hand2))
    return count


if __name__ == '__main__':
    print(main())
