import random
from collections import Counter

SUITS = ["♠", "♥", "♦", "♣"]
RANKS = {2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8",
         9: "9", 10: "10", 11: "J", 12: "Q", 13: "K", 14: "A"}


def make_deck():
    return [(r, s) for r in RANKS for s in SUITS]


def is_straight(ranks):
    values = sorted(set(ranks))
    if len(values) != 5:         
        return False
    if values[-1] - values[0] == 4:
        return True
    return values == [2, 3, 4, 5, 14]   # A-2-3-4-5


def classify(hand):
    ranks = [r for r, _ in hand]
    counts = sorted(Counter(ranks).values(), reverse=True)

    if counts == [4, 1]:
        return "Four of a Kind"
    if counts == [3, 2]:
        return "Full house"
    if is_straight(ranks):
        return "Straight"
    if counts == [3, 1, 1]:
        return "Three of a Kind"
    if counts == [2, 2, 1]:
        return "two Pair"
    if counts == [2, 1, 1, 1]:
        return "One Pair"
    return "single"


def show(hand):
    return "  ".join(f"{s}{RANKS[r]}" for r, s in hand)


def main():
    hand = random.sample(make_deck(), 5)  
    hand.sort()
    print("your card:", show(hand))
    print("Poker Hand:", classify(hand))


if __name__ == "__main__":
    main()