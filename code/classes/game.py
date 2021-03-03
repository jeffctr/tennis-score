from classes.player import Player
from helpers.constant import (
    DEUCE,
    ADVANTAGE,
    RESET_SCORE,
    PLAYER_NAME_ONE,
    PLAYER_NAME_TWO,
    POINT_DIFFERENCE,
    POINTS_TRANSFORMER,
    POINT_LIMIT_TIE_BREAKER
)


class Game(object):
    """ Instance local constant variables """
    DEUCE_LIMIT = 3
    POINT_LIMIT = 4
    AUTO_INCREMENT = 1

    def __init__(self, player_one: Player, player_two: Player, is_tie_break: bool):
        """ Instance variables """
        self.player_one = player_one
        self.player_two = player_two
        self.players = {PLAYER_NAME_ONE: self.player_one, PLAYER_NAME_TWO: self.player_two}
        self.is_tie_break = is_tie_break
        self.winner = None
        self.score = None

    def _check_winner(self, diff: int, limit: int) -> bool:
        """ Check if there is already a winner """
        # Check if diff is positive or negative then assign the player object
        if abs(diff) >= POINT_DIFFERENCE and (self.player_one.score >= limit or self.player_two.score >= limit):
            self.winner = self.player_one if diff >= 0 else self.player_two
            self.winner.game += 1
            self.player_two.score = RESET_SCORE
            self.player_one.score = RESET_SCORE
            return True

        return False

    def _check_score(self) -> str:
        """ Check which player is winning and match the correct score for a normal game """
        # Get the difference between both players and check which one is ahead
        diff = self.player_one.score - self.player_two.score

        if self._check_winner(diff, self.POINT_LIMIT):
            return f'Winner {self.winner.name}'

        if self.player_one.score >= self.DEUCE_LIMIT and self.player_two.score >= self.DEUCE_LIMIT:
            if diff == 0 and not self.is_tie_break:
                return DEUCE

            # Check if diff is positive or negative then assign the player name
            advantage_name = self.player_one.name if diff > 0 else self.player_two.name
            return f'{ADVANTAGE} {advantage_name}'

        return f'{POINTS_TRANSFORMER[self.player_one.score]} - {POINTS_TRANSFORMER[self.player_two.score]}'

    def _tie_breaker_score(self) -> str:
        """ Check which player is winning and establish the correct score just for tie breaker games """
        # Get the difference between both players and check which one is ahead
        diff = self.player_one.score - self.player_two.score

        if self._check_winner(diff, POINT_LIMIT_TIE_BREAKER):
            return f'Winner {self.winner.name}'

        return f'{self.player_one.score} - {self.player_two.score}'

    @property
    def score(self) -> str:
        return self._score

    @score.setter
    def score(self, player: str):
        """ Method setter that receives the new point won by a player """
        # Add the won point to the correct player
        if player in self.players.keys():
            self.players[player].score = self.players[player].score + self.AUTO_INCREMENT

        if self.is_tie_break:
            self._score = self._tie_breaker_score()
        else:
            self._score = self._check_score()
