from Player import Player
from CardDeck import CardDeck


class Trick:
    def __init__(self, current_round):
        self.current_card_player_pairs = []
        # adds current trick to round
        current_round.tricks.append(self)
        self.trick_winner = None

    def add_to_trick(self, card, player):
        self.current_card_player_pairs.append((card, player))

    def determine_winner(self, current_suit, trump_suit):
        trump_card_pairs = []
        current_suit_pairs = []
        for card_player_pair in self.current_card_player_pairs:
            if card_player_pair[0].suit == trump_suit:
                trump_card_pairs.append(card_player_pair)
            if card_player_pair[0].suit == current_suit:
                current_suit_pairs.append(card_player_pair)
        if len(trump_card_pairs) > 1:
            winner = None
            for pair in trump_card_pairs:
                if winner is None:
                    winner = pair
                if pair[0] > winner[0]:
                    winner = pair
            self.trick_winner = winner
            return

        # If no player played a trump card
        elif len(trump_card_pairs) == 0:
            winner = None
            for pair in current_suit_pairs:
                if winner is None:
                    winner = pair
                if pair[0] > winner[0]:
                    winner = pair
            self.trick_winner = winner
            return

        # If only one player played a trump card
        else:
            # returns the pair who played the one trump card
            self.trick_winner = trump_card_pairs[1]
            return

    def return_played_cards(self):
        for pair in self.current_card_player_pairs:



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
        self.trump_suit = trump_suit
        self.team_a = team_a
        self.team_b = team_b
        self.tricks = []
        self.high_winner = None
        self.low_winner = None
        self.jack_winner = None
        self.point_winner = None
        self.current_high_card = None
        self.current_low_card = None
        self.team_a_won_cards = []
        self.team_b_won_cards = []

    def distribute_won_cards(self):
        """loops for list of tricks and distributes the won cards to each team's list"""
        for trick in self.tricks:
            if trick.trick_winner[1] is in team_a:


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