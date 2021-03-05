class Hand:
    def __init__(self, cards, trump_suit, round_suit):
        """default constructor for hand"""
        self.cards = cards
        self.trump_suit = trump_suit
        self.round_suit = round_suit

    def __str__(self):
        """Return string representation of the hand"""
        string = ""
        for card in self.cards:
            string + (str(card) + " ")
        return string

    def has_suit(self, suit):
        """iterates through card list, checking for round suit"""
        for card in self.cards:
            if card.suit == suit:
                return True
        return False

    def num_card_in_suit(self, suit):
        """"counts the amount of trump cards """
        count = 0
        for card in self.cards:
            if card.suit == suit:
                count += 1
        return count

    def high_card(self, suit):
        """returns high card, prioritizes bid_suit -- if no bid_suit, then returns high card in another suit"""
        self.cards.sort()
        if self.has_suit(suit):
            for card in self.cards.sort(reverse=True):
                if card.suit == suit:
                    return card
        else:
            return self.cards.sort(reverse=True)[0]

    def low_card(self, suit):
        """returns low card, prioritizes bid_suit -- if no bid_suit, then returns low card in another suit"""
        self.cards.sort()
        if self.has_suit(suit):
            for card in self.cards.sort():
                if card.suit == suit:
                    return card
        else:
            return self.cards.sort()[0]

    def jack_card(self, suit):
        """returns jack suit of the trump suit"""
        for card in self.cards:
            if card.rank == 9:
                # 9 is the index for Jack in the rank list
                if card.suit == suit:
                    return card
        return

    def check_for_six_new_cards(self):
        """Checks if all cards are between 3 - 9 inclusive with no face cards. Returns true if so, false otherwise"""
        six_new_cards = True
        for card in self.cards:
            if card.rank in (0, 8, 9, 10, 11):
                # indices for ranks that are not 2 or a face card
                six_new_cards = False
        return six_new_cards

    def discard_card(self, card_index):
        """discards a specific card"""
        self.cards.pop(card_index)

    def replace_cards(self, card_indices, deck):
        """replaces the cards in the deck with random cards from the deck"""
        for card_num in card_indices:
            self.cards[card_num] = deck.pop_card



