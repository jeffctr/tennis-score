# TENNIS-SCORE

## Requirements

To be able to run this project without any issue you will require to install or have running in you machine Docker and Docker-compose
- [docker]()
- [docker-compose]()

## Installation
1. Cone the whole repository
1. Run `docker-compose up --build -d`
1. Check that the project is running `docker ps`
1. If you have a container with the name `tennis-score` it means everything is perfect.
1. Login into the container run `docker exec -it tennis-score bash`

## Running application
If you have done the previous steps and you are inside the container you just need to run the following command
- Run `python main.py`

## Running test files
This application has implemented the native package for testing called `unittest`
- Run `python -m unittest tests/test_player.py`
- Run `python -m unittest tests/test_game.py`
- Run `python -m unittest tests/test_set.py`
- Run `python -m unittest tests/test_match.py`

## Functionality

### Main.py
This file will call the the class Match and will run through the full logic. In addition, this file also receives the inputs from the user.

### Match.py
The match class receive two Players that are going to start a game. Then this class will decide when a Match has finished or if the there is a winner.

## Set.py
A player needs to win two set to be able to win the match. Then, this class will keep track of the Sets of will check if is necessary to start a new set because there is a set winner.

## Game.py
Perhaps the most important class. This class has the logic of how a game is played or if there is a tie-breaker. This class with configure and validate each game. Then will update the player score and provide the respective information.

