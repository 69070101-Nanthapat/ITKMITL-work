"""name of card"""
s = input().strip().upper()

rank = s[:-1]
suit = s[-1]

ranks = {
    "A": "Ace",
    "J": "Jack",
    "Q": "Queen",
    "K": "King"
}

suits = {
    "D": "Diamonds",
    "H": "Hearts",
    "S": "Spades",
    "C": "Clubs"
}

rank = ranks.get(rank, rank)
suit = suits.get(suit, "")

print(f"{rank} of {suit}")
