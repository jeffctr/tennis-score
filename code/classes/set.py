from classes.player import Player
from classes.game import Game
from helpers.constant import POINT_DIFFERENCE, LIMIT_START_TIE_BREAKER, RESET_SCORE


class Set(object):
    """ Instance local constant variables """
    GAME_LIMIT = 6

    def __init__(self, player_one: Player, player_two: Player):
        self.player_one = player_one
        self.player_two = player_two
        self.is_tie_breaker = self.tie_breaker()
        self.game = Game(self.player_one, self.player_two, self.is_tie_breaker)
        self.score = '0 - 0, 0 - 0'
        self.winner = None

    def tie_breaker(self) -> bool:
        """ Check if it is necessary to play a tie-breaker game """
        if self.player_one.game == LIMIT_START_TIE_BREAKER and self.player_two.game == LIMIT_START_TIE_BREAKER:
            return True

        return False

    def check_set_winner(self):
        """ Check if there is any winner of this set with min six won games an advatage of two games """
        diff = self.player_one.game - self.player_two.game

        if self.player_one.game >= self.GAME_LIMIT or self.player_two.game >= self.GAME_LIMIT:
            if abs(diff) >= POINT_DIFFERENCE:
                self.winner = self.player_one if diff >= 0 else self.player_two

        if self.is_tie_breaker and self.game.winner:
            self.winner = self.player_one if diff >= 0 else self.player_two

        if self.winner:
            self.winner.set += 1
            self.score = f'{self.game.score} Set: {self.player_one.set} - {self.player_two.set} | Game: {self.player_one.game} - {self.player_two.game}'
            self.player_two.game = RESET_SCORE
            self.player_one.game = RESET_SCORE

    def play_game(self, player: str):
        """ Play a game, then check if there is any winner or if it is necessary to play a tie breaker """

        # Check if there is a game winner then start a new game
        if self.game.winner:
            self.is_tie_breaker = self.tie_breaker()
            self.game = Game(self.player_one, self.player_two, self.is_tie_breaker)

        # Winner point
        self.game.score = player
        # Check if there is a set winner
        self.check_set_winner()

        if not self.winner:
            self.score = f'{self.player_one.game} - {self.player_two.game}, {self.game.score}'

    @property
    def score(self) -> str:
        return self._score

    @score.setter
    def score(self, score: str):
        self._score = score
