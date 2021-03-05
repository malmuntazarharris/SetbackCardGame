class Card:
    suits = ["Diamonds", "Spades", "Clubs", "Hearts"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "Jack", "Queen", "King", "Ace"]

    def __init__(self, suit=0, rank=0):
        """Default constructor for each card"""
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """returns a string representation"""
        return f"{Card.ranks[self.rank]} of {Card.suits[self.suit]}"

    def __lt__(self, other):
        """Overriding < operator """
        t1 = self.rank
        t2 = other.rank
        return t1 < t2
