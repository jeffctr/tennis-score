import unittest

from classes.player import Player
from helpers.constant import (
    PLAYER_NAME_ONE,
    PLAYER_NAME_TWO
)


class TestPlayer(unittest.TestCase):

    def test_set_name(self):
        player_one = Player(PLAYER_NAME_ONE)

        self.assertIsInstance(player_one.name, str)

    def test_get_name(self):
        player_one = Player(PLAYER_NAME_ONE)
        player_two = Player(PLAYER_NAME_TWO)

        self.assertEqual(player_one.name, PLAYER_NAME_ONE)
        self.assertNotEqual(player_one.name, player_two.name)

    def test_set_score(self):
        player_score = 15

        player_one = Player(PLAYER_NAME_ONE)
        player_one.score = player_score

        self.assertIsInstance(player_one.score, int)

    def test_get_score(self):
        player_one_score = 15
        player_two_score = 30

        player_one = Player(PLAYER_NAME_ONE)
        player_one.score = player_one_score
        player_two = Player(PLAYER_NAME_TWO)
        player_two.score = player_two_score

        self.assertGreater(player_two.score, player_one.score)

    def test_set_game(self):
        player_game = 6

        player_one = Player(PLAYER_NAME_ONE)
        player_one.game = player_game

        self.assertIsInstance(player_one.game, int)

    def test_get_game(self):
        player_one_game = 1
        player_two_game = 3

        player_one = Player(PLAYER_NAME_ONE)
        player_one.game = player_one_game
        player_two = Player(PLAYER_NAME_TWO)
        player_two.game = player_two_game

        self.assertGreater(player_two.game, player_one.game)

    def test_set_set(self):
        player_set = 6

        player_one = Player(PLAYER_NAME_ONE)
        player_one.set = player_set

        self.assertIsInstance(player_one.set, int)

    def test_get_set(self):
        player_one_set = 1
        player_two_set = 3

        player_one = Player(PLAYER_NAME_ONE)
        player_one.set = player_one_set
        player_two = Player(PLAYER_NAME_TWO)
        player_two.set = player_two_set

        self.assertGreater(player_two.set, player_one.set)
