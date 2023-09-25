import random

bot_wins = 0
player_wins = 0

beatable_by = {
    'scissor': 'rock',
    'paper': 'scissor',
    'rock': 'paper'
}
options = list(beatable_by.keys())

while bot_wins < 3 and player_wins < 3:
    print('-------------------------------------')
    print('Bot score:', bot_wins)
    print('Your score:', player_wins)
    print('-------------------------------------')
    game_ended = False
    while not game_ended:
        player_choice = input('Your choice(rock, paper, scissor): ')
        if player_choice not in options:
            print('Your choice is not correct. Try again')
            continue

        bot_choice = random.choice(options)
        print(f"Bot choice is {bot_choice}")
        if bot_choice == player_choice:
            print("It's a draw! Again")
            continue

        if beatable_by[player_choice] == bot_choice:
            print('You lost!')
            bot_wins += 1
        else:
            print('You won!')
            player_wins += 1

        game_ended = True

if player_wins > bot_wins:
    print('You are the champion!')
elif player_wins < bot_wins:
    print('You are the loser! Try again')
else:
    print("Ooohhh... Tough game. It's a draw!")