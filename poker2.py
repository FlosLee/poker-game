import random

SUITS = ["♠", "♥", "♦", "♣"]
RANKS = {2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8",
         9: "9", 10: "10", 11: "J", 12: "Q", 13: "K", 14: "A"}


def make_deck():
    return [(r, s) for r in RANKS for s in SUITS]


def show(hand):
    return "  ".join(f"{s}{RANKS[r]}" for r, s in hand)


def main():
    hand = random.sample(make_deck(), 5)
    print("Your cards:", show(hand))


if __name__ == "__main__":
    main()