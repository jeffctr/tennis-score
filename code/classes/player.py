class Player(object):
    def __init__(self, name: str):
        self.name = name
        self.score = 0
        self.game = 0
        self.set = 0

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def score(self) -> int:
        return self._score

    @score.setter
    def score(self, score: int):
        self._score = score

    @property
    def game(self) -> int:
        return self._game

    @game.setter
    def game(self, game: int):
        self._game = game

    @property
    def set(self) -> int:
        return self._set

    @set.setter
    def set(self, set: int):
        self._set = set
