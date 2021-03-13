import unittest

from Card import Card
from CardDeck import CardDeck


class TestCard(unittest.TestCase):
    def setUp(self):
        self.card = Card()
        self.cardDeck = CardDeck()


class TestInitCard(TestCard):
    def test_initial_values(self):
        self.assertEqual(self.card.rank, 0)
        self.assertEqual(self.card.suit, 0)


class TestCardMethods(TestCard):
    t1 = Card(3, 10)
    t2 = Card(3, 0)
    t3 = Card(3, 10)
    t4 = Card(0, 5)

    def test_gt(self):
        self.assertTrue(self.t1 > self.t2)
        self.assertFalse(self.t2 > self.t1)
        self.assertFalse(self.t2 > self.t2)

    def test_lt(self):
        self.assertTrue(self.t2 < self.t1)
        self.assertFalse(self.t1 < self.t2)
        self.assertFalse(self.t2 < self.t2)

    def test_eq(self):
        self.assertTrue(self.t1 == self.t1)
        self.assertFalse(self.t1 == self.t2)
        self.assertTrue(self.t1 == self.t3)

    def test_str(self):
        self.assertTrue("Hearts" in str(self.t1))
        self.assertTrue("Queen" in str(self.t1))
        self.assertTrue("Hearts" in str(self.t2))
        self.assertTrue("2" in str(self.t2))
        self.assertTrue("Diamonds" in str(self.t4))
        self.assertTrue("7" in str(self.t4))


class TestCardDeck(TestCard):
    def test_init(self):
        self.assertTrue("Ace of Diamonds" in str(self.cardDeck))
        self.assertTrue("Ace of Hearts" in str(self.cardDeck))
        self.assertTrue("Ace of Spades" in str(self.cardDeck))
        self.assertTrue("Ace of Clubs" in str(self.cardDeck))

    def test_len(self):
        self.assertEqual(len(self.cardDeck), 52)

    def test_pop_remove(self):
        self.assertEqual("Ace of Hearts", str(self.cardDeck.pop_card()))
        self.cardDeck.add_card(Card(3, 12))
        self.assertEqual("Ace of Hearts", str(self.cardDeck.cards[51]))

    def test_sort(self):
        self.cardDeck.shuffle()
        self.cardDeck.sort()
        self.assertEqual("Ace of Clubs", str(self.cardDeck.cards[51]))