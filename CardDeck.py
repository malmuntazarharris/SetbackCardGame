from Card import Card
import random


class CardDeck:
    def __init__(self):
        """Initializes deck with 52 cards"""
        self.cards = []
        for suit in range(4):
            for rank in range(13):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        """"Overrides the str operator"""
        string = ""
        for card in self.cards:
            string + (str(card) + " ")
        return string

    def __len__(self):
        """Overrides the len operator"""
        return len(self.cards)

    def add_card(self, card):
        """Adds card to the deck"""
        self.cards.append(card)

    def pop_card(self):
        """"Returns top card"""
        return self.cards.pop(-1)

    def shuffle(self):
        """shuffle the deck of cards"""
        random.shuffle(self.cards)

    def sort(self):
        """"Sorts the cards in ascending order"""
        self.cards.sort()


