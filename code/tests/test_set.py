import unittest

from classes.player import Player
from classes.set import Set
from helpers.constant import (
    PLAYER_NAME_ONE,
    PLAYER_NAME_TWO
)


class TestGame(unittest.TestCase):
    def test_score(self):
        player_one = Player(PLAYER_NAME_ONE)
        player_two = Player(PLAYER_NAME_TWO)

        set_game = Set(player_one, player_two)
        self.assertEqual(set_game.score, '0 - 0, 0 - 0')
        set_game.play_game(PLAYER_NAME_TWO)
        self.assertEqual(set_game.score, '0 - 0, 0 - 15')

    def test_tie_breaker(self):
        player_one = Player(PLAYER_NAME_ONE)
        player_two = Player(PLAYER_NAME_TWO)

        set_game = Set(player_one, player_two)
        self.assertEqual(set_game.tie_breaker(), False)

    def test_play_game_deuce(self):
        player_one = Player(PLAYER_NAME_ONE)
        player_two = Player(PLAYER_NAME_TWO)

        set_game = Set(player_one, player_two)
        for index in range(4):
            set_game.play_game(PLAYER_NAME_ONE)
            set_game.play_game(PLAYER_NAME_TWO)

        self.assertEqual(set_game.score, '0 - 0, Deuce')

    def test_play_game_advantage(self):
        player_one = Player(PLAYER_NAME_ONE)
        player_two = Player(PLAYER_NAME_TWO)

        set_game = Set(player_one, player_two)

        for index in range(4):
            set_game.play_game(PLAYER_NAME_ONE)
            set_game.play_game(PLAYER_NAME_TWO)

        set_game.play_game(PLAYER_NAME_TWO)
        self.assertEqual(set_game.score, f'0 - 0, Advantage {PLAYER_NAME_TWO}')

    def test_play_game_win(self):
        player_one = Player(PLAYER_NAME_ONE)
        player_two = Player(PLAYER_NAME_TWO)

        set_game = Set(player_one, player_two)

        for index in range(3):
            set_game.play_game(PLAYER_NAME_TWO)

        # Check game score before decide the winner
        self.assertEqual(set_game.score, '0 - 0, 0 - 40')

        # Player two should win the game
        set_game.play_game(PLAYER_NAME_TWO)
        self.assertEqual(set_game.score, f'0 - 1, Winner {PLAYER_NAME_TWO}')

    def test_play_game_tie_breaker_score(self):
        player_one = Player(PLAYER_NAME_ONE)
        player_two = Player(PLAYER_NAME_TWO)
        player_two.game = 6
        player_one.game = 6

        set_game = Set(player_one, player_two)
        self.assertEqual(set_game.tie_breaker(), True)

        for index in range(11):
            set_game.play_game(PLAYER_NAME_TWO)
            set_game.play_game(PLAYER_NAME_ONE)

        # Check game score before decide the winner
        self.assertEqual(set_game.score, '6 - 6, 11 - 11')

    def test_play_game_tie_breaker_set_winner(self):
        player_one = Player(PLAYER_NAME_ONE)
        player_two = Player(PLAYER_NAME_TWO)
        player_two.game = 6
        player_one.game = 6

        set_game = Set(player_one, player_two)
        self.assertEqual(set_game.tie_breaker(), True)

        for index in range(8):
            set_game.play_game(PLAYER_NAME_TWO)
            set_game.play_game(PLAYER_NAME_ONE)

        # Check game score before decide the winner
        self.assertEqual(set_game.score, '6 - 6, 8 - 8')

        set_game.play_game(PLAYER_NAME_TWO)
        self.assertEqual(set_game.score, '6 - 6, 8 - 9')

        set_game.play_game(PLAYER_NAME_TWO)
        self.assertIsInstance(set_game.winner, Player)
        self.assertEqual(set_game.score, f'Winner {PLAYER_NAME_TWO} Set: 0 - 1 | Game: 6 - 7')

    def test_play_game_additional_game(self):
        player_one = Player(PLAYER_NAME_ONE)
        player_two = Player(PLAYER_NAME_TWO)
        player_two.game = 6
        player_one.game = 5

        set_game = Set(player_one, player_two)
        self.assertEqual(set_game.tie_breaker(), False)

        for index in range(3):
            set_game.play_game(PLAYER_NAME_TWO)

        self.assertEqual(set_game.score, '5 - 6, 0 - 40')
        set_game.play_game(PLAYER_NAME_TWO)
        self.assertEqual(set_game.score, f'Winner {PLAYER_NAME_TWO} Set: 0 - 1 | Game: 5 - 7')
        self.assertIsInstance(set_game.winner, Player)

    def test_play_game_set_winner(self):
        player_one = Player(PLAYER_NAME_ONE)
        player_two = Player(PLAYER_NAME_TWO)
        player_two.game = 5
        player_one.game = 4

        set_game = Set(player_one, player_two)

        for index in range(4):
            set_game.play_game(PLAYER_NAME_TWO)

        self.assertIsInstance(set_game.winner, Player)

    def test_play_game_new_games(self):
        player_one = Player(PLAYER_NAME_ONE)
        player_two = Player(PLAYER_NAME_TWO)

        set_game = Set(player_one, player_two)
        self.assertEqual(set_game.tie_breaker(), False)

        for index in range(3):
            set_game.play_game(PLAYER_NAME_TWO)

        self.assertEqual(set_game.score, '0 - 0, 0 - 40')
        set_game.play_game(PLAYER_NAME_TWO)
        self.assertEqual(set_game.score, f'0 - 1, Winner {PLAYER_NAME_TWO}')

        for index in range(3):
            set_game.play_game(PLAYER_NAME_TWO)
        self.assertEqual(set_game.score, '0 - 1, 0 - 40')
        set_game.play_game(PLAYER_NAME_TWO)
        self.assertEqual(set_game.score, f'0 - 2, Winner {PLAYER_NAME_TWO}')

        for index in range(15):
            set_game.play_game(PLAYER_NAME_TWO)
        self.assertEqual(set_game.score, '0 - 5, 0 - 40')
