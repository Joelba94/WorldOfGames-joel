import gussGame
import currencyRouletteGame
import memoryGame
import score
import utils
import mainScores

# reset the file number to zero
read_file = open(utils.SCORES_FILE_NAME, 'w')
read_file.write(str(0))


def welcome(name):
    print(f'Hello {name} and welcome to the World Of Games (WoG).\n'
          f'Here you can find many coll games to play.')


def load_game():
    game_number = 0
    game_difficulty = 0

    while game_number < 1 or game_number > 3:
        game_number = int(input(
            'Please choose a game to play:'
            '1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n'
            '2. Guess Game - guess a number and see if you chose like the computer\n'
            '3. Currency Roulette - try and guess the value of a random amount of USD in ILS'))

    while game_difficulty < 1 or game_difficulty > 5:
        game_difficulty = int(input('Please choose game difficulty from 1-5:'))

    if game_number == 1:
        if memoryGame.play(game_difficulty):
            score.add_score(game_difficulty)
            mainScores.score_server()
        else:
            mainScores.error()

    elif game_number == 2:
        if gussGame.play(game_difficulty):
            score.add_score(game_difficulty)
            mainScores.score_server()
        else:
            mainScores.error()

    elif game_number == 3:
        if currencyRouletteGame.play(game_difficulty):
            score.add_score(game_difficulty)
            mainScores.score_server()
        else:
            mainScores.error()

            # print(memoryGame.play(game_difficulty))
            # print(gussGame.play(game_difficulty))
            # print(currencyRouletteGame.play(game_difficulty))
