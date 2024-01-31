# import game_functions
# Using assertEqual, write various unit tests that test each function in game_functions individually, try to be exhaustive

# ========================================================================================================== #

import unittest
import game_functions


class MyTestCase(unittest.TestCase):
    def test_check_straight_yes(self):
        self.assertEqual(game_functions.check_straight('S2', 'S3', 'S4'), 4)

    def test_check_straight_yes2(self):
        self.assertEqual(game_functions.check_straight('SQ', 'SJ', 'SK'), 13)

    def test_check_straight_no(self):
        self.assertEqual(game_functions.check_straight('S2', 'SQ', 'S4'), 0)

    def test_check_straight_no2(self):
        self.assertEqual(game_functions.check_straight('S2', 'SQ', 'SK'), 0)

    def test_check_3ofa_kind_yes(self):
        self.assertEqual(game_functions.check_3ofa_kind('S5', 'S5', 'S5'), 5)

    def test_check_3ofa_kind_no(self):
        self.assertEqual(game_functions.check_3ofa_kind('S5', 'S5', 'S9'), 0)

    def test_check_3ofa_kind_no2(self):
        self.assertEqual(game_functions.check_3ofa_kind('S5', 'S2', 'S9'), 0)

    def test_check_royal_flush_yes(self):
        self.assertEqual(game_functions.check_royal_flush('SQ', 'SK', 'SA'), 14)

    def test_check_royal_flush_straight_notroyal(self):
        self.assertEqual(game_functions.check_royal_flush('S4', 'S5', 'S6'), 0)

    def test_check_royal_flush_notstraight_notroyal(self):
        self.assertEqual(game_functions.check_royal_flush('S4', 'SQ', 'SA'), 0)

    def test_play_cards_leftwin_withstraight_over3ofakind(self):
        self.assertEqual(game_functions.play_cards('S4', 'S5', 'S6', 'S9', 'S9', 'S9'), -1)

    def test_play_cards_leftwin_with_both_straight(self):
        self.assertEqual(game_functions.play_cards('S8', 'S8', 'S8', 'S5', 'S5', 'S5'), -1)

    def test_play_cards_draw_nopoints(self):
        self.assertEqual(game_functions.play_cards('S2', 'S4', 'S7', 'SQ', 'S10', 'S5'), 0)

    def test_play_cards_draw_both_straights(self):
        self.assertEqual(game_functions.play_cards('S6', 'S6', 'S6', 'S6', 'S6', 'S6'), 0)

    def test_play_cards_rightwin_royalflush(self):
        self.assertEqual(game_functions.play_cards('S5', 'S3', 'S9', 'SQ', 'SK', 'SA'), 1)

    def test_play_cards_rightwin_both_3ofakind(self):
        self.assertEqual(game_functions.play_cards('S6', 'S6', 'S6', 'S10', 'S10', 'S10'), 1)

    def test_play_cards_rightstraight_left3ofakind_rightwin(self):
        self.assertEqual(game_functions.play_cards('SA', 'SA', 'SA', 'S4', 'S5', 'S6'), 1)

    def test_play_cards_leftstraight_right3ofakind_leftwin(self):
        self.assertEqual(game_functions.play_cards('S4', 'S5', 'S6', 'SA', 'SA', 'SA'), -1)


if __name__ == '__main__':
    unittest.main()
