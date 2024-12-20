import random


def deal(num_hands, n=5, deck=[r + s for r in '23456789TJQKA' for s in 'HDSC']):
    random.shuffle(deck)
    return [deck[i*n:(i+1)*n] for i in range(num_hands)]


def poker(hands):
    return max(hands, key=hand_rank)


def hand_rank(hand):
    return


def card_ranks(hand):
    ranks = ['__23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse=True)
    return ranks




















