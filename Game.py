import Card
from Player import Player, Team
import CardDeck
# TODO: need to set up a text based main file
# TODO: finish game mechanic test

class Trick:
    def __init__(self, current_round):
        self.current_card_player_pairs = []
        # adds current trick to round
        current_round.tricks.append(self)
        self.trick_winner = None
        self.trick_is_over = False

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


class Round:

# TODO: set up the bidding system
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
        if team_a is not Team or team_b is not Team:
            raise TypeError
        self.trump_suit = trump_suit
        self.team_a = team_a
        self.team_b = team_b
        self.tricks = []
        self.high_winner = None
        self.low_winner = None
        self.jack_winner = None
        self.game_winner = None
        # first value of tuple is bid amount, second value is what team it is
        self.bid = ()

    def distribute_won_cards(self):
        """iterates through list of tricks and distributes the won cards to each team's list"""
        for trick in self.tricks:
            if trick.trick_winner[1] in self.team_a.players:
                for pair in trick.current_card_player_pairs:
                    self.team_a.won_cards.append(pair[0])
            elif trick.trick_winner[1] in self.team_b.players:
                for pair in trick.current_card_player_pairs:
                    self.team_b.won_cards.append(pair[0])

    def determine_high_winner(self):
        """iterates through the list of won cards, sets the winner of each card type"""
        # iterate through each list and find the max of all of them
        for card in self.team_a.won_cards:
            if card.suit == self.trump_suit and ((self.high_winner < card) or (self.high_winner is None)):
                self.high_winner = card
        for card in self.team_b.won_cards:
            if card.suit == self.trump_suit and ((self.high_winner < card) or (self.high_winner is None)):
                self.high_winner = card

    def determine_low_winner(self):
        # iterate through each list and find the min of all of them
        for card in self.team_a.won_cards:
            if card.suit == self.trump_suit and ((self.low_winner < card) or (self.low_winner is None)):
                self.low_winner = card
        for card in self.team_b.won_cards:
            if card.suit == self.trump_suit and ((self.low_winner < card) or (self.low_winner is None)):
                self.low_winner = card

    def determine_jack_winner(self):
        # '8' is the index for Jack
        for card in self.team_a.won_cards:
            if card.rank == Card.Card.jack_index and card.suit == self.trump_suit:
                self.jack_winner = self.team_a
        for card in self.team_b.won_cards:
            if card.rank == Card.Card.jack_index and card.suit == self.trump_suit:
                self.jack_winner = self.team_b

    def determine_game_winner(self):
        team_a_points = 0
        team_b_points = 0

        for card in self.team_a.won_cards:
            team_a_points += self.card_values[Card.Card.ranks[card.rank]]
        for card in self.team_b.won_cards:
            team_b_points += self.card_values[Card.Card.ranks[card.rank]]

        if team_a_points > team_b_points:
            self.game_winner = self.team_a
        elif team_b_points > team_a_points:
            self.game_winner = self.team_b
        else:
            self.game_winner = (self.team_a, self.team_b)

class Game:
    def __init__(self, team_a_name, team_b_name):
        self.team_a = []
        self.team_b = []
        self.team_a_name = team_a_name
        self.team_b_name = team_b_name
        self.team_a_points = 0
        self.team_b_points = 0
        self.game_deck = CardDeck.CardDeck()

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