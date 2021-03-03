import unittest

from classes.player import Player
from classes.game import Game
from helpers.constant import (
    PLAYER_NAME_ONE,
    PLAYER_NAME_TWO
)


class TestGame(unittest.TestCase):

    def test_set_score(self):
        player_one = Player(PLAYER_NAME_ONE)
        player_two = Player(PLAYER_NAME_TWO)

        game = Game(player_one, player_two, False)
        game.score = PLAYER_NAME_ONE
        self.assertIsInstance(game.score, str)

    def test_get_score(self):
        player_one = Player(PLAYER_NAME_ONE)
        player_two = Player(PLAYER_NAME_TWO)

        game = Game(player_one, player_two, False)
        game.score = PLAYER_NAME_ONE

        self.assertEqual(game.score, '15 - 0')

    def test_get_score_deuce(self):
        player_one = Player(PLAYER_NAME_ONE)
        player_two = Player(PLAYER_NAME_TWO)

        game = Game(player_one, player_two, False)
        for index in range(4):
            game.score = PLAYER_NAME_ONE
            game.score = PLAYER_NAME_TWO

        # Check the Deuce game
        self.assertEqual(game.score, 'Deuce')

    def test_get_score_advantage(self):
        player_one = Player(PLAYER_NAME_ONE)
        player_two = Player(PLAYER_NAME_TWO)

        game = Game(player_one, player_two, False)
        # Set previous score
        for index in range(3):
            game.score = PLAYER_NAME_ONE
            game.score = PLAYER_NAME_TWO

        # Set the advantage point
        game.score = PLAYER_NAME_TWO

        self.assertEqual(game.score, f'Advantage {PLAYER_NAME_TWO}')

    def test_get_winner(self):
        player_one = Player(PLAYER_NAME_ONE)
        player_two = Player(PLAYER_NAME_TWO)

        game = Game(player_one, player_two, False)
        # Set previous score
        for index in range(3):
            game.score = PLAYER_NAME_ONE
            game.score = PLAYER_NAME_TWO

        # Check the Winner game
        game.score = PLAYER_NAME_TWO
        game.score = PLAYER_NAME_TWO

        self.assertIsInstance(game.winner, Player)
        self.assertEqual(game.winner, player_two)
        self.assertEqual(game.winner.game, 1)

    def test_get_winner_2(self):
        player_one = Player(PLAYER_NAME_ONE)
        player_two = Player(PLAYER_NAME_TWO)

        game = Game(player_one, player_two, False)
        # Set previous score
        for index in range(3):
            game.score = PLAYER_NAME_ONE

        self.assertEqual(game.score, '40 - 0')
        # Check the Winner game
        game.score = PLAYER_NAME_ONE

        self.assertIsInstance(game.winner, Player)
        self.assertEqual(game.winner, player_one)
        self.assertEqual(game.winner.game, 1)

    def test_score_tie_breaker(self):
        player_one = Player(PLAYER_NAME_ONE)
        player_two = Player(PLAYER_NAME_TWO)

        game = Game(player_one, player_two, True)
        game.score = PLAYER_NAME_ONE

        self.assertEqual(game.score, '1 - 0')

    def test_get_score_tie_breaker_games(self):
        player_one = Player(PLAYER_NAME_ONE)
        player_two = Player(PLAYER_NAME_TWO)

        game = Game(player_one, player_two, True)
        for index in range(6):
            game.score = PLAYER_NAME_ONE
            game.score = PLAYER_NAME_TWO

        # Check score
        self.assertEqual(game.score, '6 - 6')

        game.score = PLAYER_NAME_TWO
        # Check score
        self.assertEqual(game.score, '6 - 7')

    def test_get_score_tie_breaker_winner(self):
        player_one = Player(PLAYER_NAME_ONE)
        player_two = Player(PLAYER_NAME_TWO)

        game = Game(player_one, player_two, True)
        for index in range(6):
            game.score = PLAYER_NAME_ONE
            game.score = PLAYER_NAME_TWO
        # Check score
        self.assertEqual(game.score, '6 - 6')

        game.score = PLAYER_NAME_TWO
        self.assertEqual(game.score, '6 - 7')
        game.score = PLAYER_NAME_ONE
        self.assertEqual(game.score, '7 - 7')

        game.score = PLAYER_NAME_TWO
        game.score = PLAYER_NAME_TWO

        self.assertIsInstance(game.winner, Player)
        self.assertEqual(game.winner, player_two)
        self.assertEqual(game.winner.game, 1)
