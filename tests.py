import unittest
import undtr


class TestDetermineWinningCard(unittest.TestCase):

    def test_two_same_suit(self):
        p1 = undtr.Player()
        p2 = undtr.Player()

        p1_card = undtr.Card(3, "CLUBS")
        p2_card = undtr.Card(8, "CLUBS")

        led_suit = "CLUBS"
        trump = "HEARTS"

        cards_d = {p1: p1_card, p2: p2_card}
        winner = undtr.determine_winning_card(cards_d, led_suit, trump)

        self.assertEqual(winner, p2)

    def test_three_same_suit(self):
        p1 = undtr.Player()
        p2 = undtr.Player()
        p3 = undtr.Player()

        p1_card = undtr.Card(10, "CLUBS")
        p2_card = undtr.Card(8, "CLUBS")
        p3_card = undtr.Card(4, "CLUBS")

        led_suit = "CLUBS"
        trump = "DIAMONDS"

        cards_d = {p1: p1_card, p2: p2_card, p3: p3_card}
        winner = undtr.determine_winning_card(cards_d, led_suit, trump)

        self.assertEqual(winner, p1)

    def test_all_trump(self):
        p1 = undtr.Player()
        p2 = undtr.Player()
        p3 = undtr.Player()

        p1_card = undtr.Card(3, "CLUBS")
        p2_card = undtr.Card(11, "CLUBS")
        p3_card = undtr.Card(6, "CLUBS")

        led_suit = "DIAMONDS"
        trump = "CLUBS"

        cards_d = {p1: p1_card, p2: p2_card, p3: p3_card}
        winner = undtr.determine_winning_card(cards_d, led_suit, trump)

        self.assertEqual(winner, p2)

    def test_one_trump(self):
        p1 = undtr.Player()
        p2 = undtr.Player()
        p3 = undtr.Player()

        p1_card = undtr.Card(3, "DIAMONDS")
        p2_card = undtr.Card(11, "CLUBS")
        p3_card = undtr.Card(6, "CLUBS")

        trump = "DIAMONDS"
        led_suit = "CLUBS"

        cards_d = {p1: p1_card, p2: p2_card, p3: p3_card}
        winner = undtr.determine_winning_card(cards_d, led_suit, trump)

        self.assertEqual(winner, p1)               

    def test_only_one_of_leading(self):
        p1 = undtr.Player()
        p2 = undtr.Player()
        p3 = undtr.Player()

        p1_card = undtr.Card(3, "DIAMONDS")
        p2_card = undtr.Card(11, "CLUBS")
        p3_card = undtr.Card(6, "CLUBS")

        trump = "HEARTS"
        led_suit = "DIAMONDS"

        cards_d = {p1: p1_card, p2: p2_card, p3: p3_card}
        winner = undtr.determine_winning_card(cards_d, led_suit, trump)

        self.assertEqual(winner, p1)       


if __name__ == "__main__":
    unittest.main()