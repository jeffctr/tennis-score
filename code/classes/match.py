from classes.player import Player
from classes.set import Set


class Match(object):

    def __init__(self, player_one: Player, player_two: Player):
        self.player_one = player_one
        self.player_two = player_two
        self.__set_game = Set(self.player_one, self.player_two)
        self.score = None
        self.winner = None

    def point_won_by(self, player: str):
        """ Assuming that there is not a winner yet and the player is valid """
        # Check if anyone won the set
        if self.__set_game.winner:
            # If someone won two set it is a match winner
            if self.__set_game.winner.set == 2:
                self.winner = self.__set_game.winner
                return None

            # Start a new set of games
            self.__set_game = Set(self.player_one, self.player_two)

        self.__set_game.play_game(player)
        self.score = self.__set_game.score

    @property
    def score(self) -> str:
        return self._score

    @score.setter
    def score(self, score: str):
        self._score = score
