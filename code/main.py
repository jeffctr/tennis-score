from classes.player import Player
from classes.match import Match
from helpers.constant import PLAYER_NAME_ONE, PLAYER_NAME_TWO

player_one = Player(PLAYER_NAME_ONE)
player_two = Player(PLAYER_NAME_TWO)

print('*******************************************************')
print(f'********* Playing a game {player_one.name} VS {player_two.name} *********')
print('*******************************************************')

match = Match(player_one, player_two)
players = {1: player_one.name, 2: player_two.name}

while True:
    if match.winner:
        print(match.score)
        break

    try:
        player = int(input('Who won the point Player (1) or Player (2):'))
        match.point_won_by(players[player])
    except Exception:
        continue

    print("\n======= SCORE ========")
    print(match.score)
    print("======================\n")
