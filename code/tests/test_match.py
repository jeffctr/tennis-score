import unittest

from classes.match import Match
from classes.match import Player
from helpers.constant import (
    PLAYER_NAME_ONE,
    PLAYER_NAME_TWO
)


class TestMatch(unittest.TestCase):

    def test_point_won_by(self):
        player_one = Player(PLAYER_NAME_ONE)
        player_two = Player(PLAYER_NAME_TWO)
        match = Match(player_one, player_two)
        match.point_won_by(PLAYER_NAME_TWO)

        self.assertEqual(match.score, '0 - 0, 0 - 15')

    def test_match_winner_set_one(self):
        player_one = Player(PLAYER_NAME_ONE)
        player_two = Player(PLAYER_NAME_TWO)
        match = Match(player_one, player_two)
        game_points = 4
        set_points = 6

        for index in range(game_points * set_points):
            match.point_won_by(PLAYER_NAME_TWO)

        self.assertEqual(match.score, f'Winner {PLAYER_NAME_TWO} Set: 0 - 1 | Game: 0 - 6')

    def test_match_winner_set_one_tie_breaker(self):
        player_one = Player(PLAYER_NAME_ONE)
        player_two = Player(PLAYER_NAME_TWO)
        match = Match(player_one, player_two)
        game_points = 4
        set_points = 5

        # Player two winning 5 games
        for index in range(game_points * set_points):
            match.point_won_by(PLAYER_NAME_TWO)

        self.assertEqual(match.score, f'0 - 5, Winner {PLAYER_NAME_TWO}')

        # Player one winning 5 games
        for index in range(game_points * set_points):
            match.point_won_by(PLAYER_NAME_ONE)

        self.assertEqual(match.score, f'5 - 5, Winner {PLAYER_NAME_ONE}')

        # Player two winning 6 games
        for index in range(game_points):
            match.point_won_by(PLAYER_NAME_TWO)

        self.assertEqual(match.score, f'5 - 6, Winner {PLAYER_NAME_TWO}')

        # Player one winning 6 games
        for index in range(game_points):
            match.point_won_by(PLAYER_NAME_ONE)

        self.assertEqual(match.score, f'6 - 6, Winner {PLAYER_NAME_ONE}')

        # Tie breaker game
        for index in range(7):
            match.point_won_by(PLAYER_NAME_ONE)
            match.point_won_by(PLAYER_NAME_TWO)

        self.assertEqual(match.score, f'6 - 6, 7 - 7')

        # Tie breaker player one winner
        match.point_won_by(PLAYER_NAME_ONE)
        match.point_won_by(PLAYER_NAME_ONE)

        self.assertEqual(match.score, f'Winner {PLAYER_NAME_ONE} Set: 1 - 0 | Game: 7 - 6')

    def test_match_winner(self):
        player_one = Player(PLAYER_NAME_ONE)
        player_two = Player(PLAYER_NAME_TWO)
        match = Match(player_one, player_two)
        game_points = 4
        set_points = 6

        # Player two winning 6 games one set
        for index in range(game_points * set_points):
            match.point_won_by(PLAYER_NAME_TWO)

        # Player two winning 6 games one set
        for index in range(game_points * set_points):
            match.point_won_by(PLAYER_NAME_ONE)

        # Player two winning 6 games two set
        for index in range(game_points * set_points):
            match.point_won_by(PLAYER_NAME_TWO)

        self.assertEqual(match.score, f'Winner {PLAYER_NAME_TWO} Set: 1 - 2 | Game: 0 - 6')
