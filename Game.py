from Player import Player
from CardDeck import CardDeck


class Trick:
    def __init__(self, current_round):
        self.current_cards = []
        # adds current trick to round
        current_round.tricks.append(self)

    def add_to_trick(self, card):
        self.current_cards.append(card)

    def determine_winner(self, current_suit, trump_suit):
        trump_cards = []
        current_suit_cards = []
        for card in self.current_cards:
            if card.suit == trump_suit:
                trump_cards.append(card)
            if card.suit == current_suit:
                current_suit_cards.append(card)


class Round:
    card_values = {
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 10,
        "Jack": 1,
        "Queen": 2,
        "King": 3,
        "Ace": 4
    }

    def __init__(self, trump_suit, team_a, team_b):
        self.tricks = []
        self.trump_suit = trump_suit
        self.high_winner = None
        self.low_winner = None
        self.jack_winner = None
        self.point_winner = None
        self.current_high_card = None
        self.current_low_card = None

class Game:
    def __init__(self, team_a_name, team_b_name):
        self.team_a = []
        self.team_b = []
        self.team_a_name = team_a_name
        self.team_b_name = team_b_name
        self.team_a_points = 0
        self.team_b_points = 0
        self.game_deck = CardDeck()

    def add_member_to_team_a(self, player):
        if player is not Player:
            raise TypeError
        self.team_a.append(player)

    def add_member_to_team_b(self, player):
        if player is not Player:
            raise TypeError
        self.team_b.append(player)

    def add_point_to_team_a(self):
        self.team_a_points += 1

    def add_point_to_team_b(self):
        self.team_b_points += 1

    def print_score(self):
        if self.team_a_points > self.team_b_points:
            return f"Team {self.team_a_name} is winning! \n" \
                   f"Current Score: Team {self.team_a_name}: {self.team_a_points}, Team {self.team_b_name}: {self.team_a_points}"