import random
from collections import defaultdict


def trivial(p):
    n = len(p)
    swapped = [False] * n
    while not all(swapped):
        i, j = random.randrange(n), random.randrange(n)
        swap(p, i, j)
        swapped[i] = swapped[j] = True


def swap(p, i, j):
    p[i], p[j] = p[j], p[i]


def knuth(p):
    n = len(p)
    for i in range(n - 1):
        swap(p, i, random.randrange(i, n))


#  Q1: order on average? trivial: o(n^2), knuth: o(n)
#  Q2: fair or not?


def test_shuffle(shuffler, deck='abcd', n=10000):
    counts = defaultdict(int)
    for _ in range(n):
        input_deck = list(deck)
        shuffler(input_deck)
        counts[''.join(input_deck)] += 1





















