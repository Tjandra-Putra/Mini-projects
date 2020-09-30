# todo: This is a rock, paper, scissors game with a bot for those who felt lonely >:D
from random import randint

options = ['r', 'p', 's']
user_score = 0
bot_score = 0

# Order matters
game_logic = [
    ['win', 'r', 's'],
    ['win', 's', 'p'],
    ['win', 'p', 'r'],
    ['lose', 's', 'r'],
    ['lose', 'p', 's'],
    ['lose', 'r', 'p']
]

while True:
    user_input = input(">>>").lower()
    bot_input = options[randint(0, 2)]

    for pattern in game_logic:
        players_inputs = user_input + bot_input
        game_answer = pattern[1] + pattern[2]

        if user_input == bot_input:
            print("This round is a DRAW!")
            print("Your score: {}, Opponent's score: {}".format(user_score, bot_score))
            print("You chose '{}' and opponent chose '{}'".format(user_input, bot_input))
            break

        if user_input not in options:
            print("ERROR: Choose only {}".format(options))
            break

        if players_inputs == game_answer:
            match_status = pattern[0]

            if match_status == "win":
                user_score += 1
                bot_score += 0
                print('---------------------')
                print("You won this round!")
                print("Your score: {}, Opponent's score: {}". format(user_score, bot_score))
                print("You chose '{}' and opponent chose '{}'".format(user_input, bot_input))
                print('---------------------')
            elif match_status == "lose":
                user_score += 0
                bot_score += 1
                print('---------------------')
                print("You lost this round!")
                print("Your score: {}, Opponent's score: {}".format(user_score, bot_score))
                print("You chose '{}' and opponent chose '{}'".format(user_input, bot_input))
                print('---------------------')


