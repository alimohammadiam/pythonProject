import random


def deal(num_hands, n=5, deck=[r + s for r in '23456789TJQKA' for s in 'HDSC']):
    random.shuffle(deck)
    return [deck[i*n:(i+1)*n] for i in range(num_hands)]


def poker(hands):
    return max(hands, key=hand_rank)


def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return 8, max(ranks)
    elif kind(4, ranks):
        return 7, kind(4, ranks), kind(1, ranks)
    elif kind(3, ranks) and kind(3, ranks):
        return 6, kind(3, ranks), kind(2, ranks)
    elif flush(hand):
        return 5, ranks
    elif straight(ranks):
        return 4, max(ranks)
    elif kind(2, ranks):
        return 3, max(ranks), ranks
    elif two_pair(ranks):
        return 2, two_pair(ranks), ranks
    elif kind(2, ranks):
        return 1, kind(2, ranks), ranks
    else:
        return 0, ranks


def card_ranks(hand):
    ranks = ['__23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks


def straight(ranks):
    return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5


def flush(hand):
    return len(set([s for r, s in hand])) == 1


def kind(n, ranks):
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None


def two_pair(ranks):
    pair = kind(2, ranks)
    low_pair = kind(2, list(reversed(ranks)))
    if pair and pair != low_pair:
        return pair, low_pair
    return None


def test():
    sf1 = '6C 7C 8C 9C TC'.split()
    sf2 = '6D 7D 8D 9D TD'.split()
    fk = '9D 9H 9S 9C 7D'.split()
    fh = 'TD TC TH 7C 7D'.split()
    tp = '5D 2C 2H 9H 5C'.split()

    #  Testing card_ranks
    assert card_ranks(sf1) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]

    #  Testing straight
    assert straight(card_ranks(sf1)) is True
    assert straight(card_ranks(fk)) is False
    assert straight(card_ranks(fh)) is False
    assert straight(card_ranks(sf2)) is True

    #  Testing flush
    assert flush(sf1) is True
    assert flush(sf2) is True
    assert flush(fh) is False
    assert flush(fk) is False

    #  Testing n-kind
    assert kind(4, card_ranks(fk)) == 9
    assert kind(3, card_ranks(fh)) == 10
    assert kind(2, card_ranks(fh)) == 7

    #  Testing two pair
    assert two_pair(card_ranks(tp)) == (5, 2)
    assert two_pair(card_ranks(fk)) is None

    #  Testing Poker
    assert poker([sf1, fk, tp]) == sf1
    assert poker([fh, fk, tp]) == fk

    return 'All Tests Passes'


print(test())



















