# Cup Guessing Game
from random import randint
print('Cup Game')
feeling_brave = True
score = 0
while feeling_brave:
    ball_cup = randint(1, 3)
    print('Three cups to chose...')
    print('A ball under one.')
    print('Which cup do you chose?')
    cup = input('1, 2, or 3?')
    cup_num = int(cup)
    if cup_num == ball_cup:
        print('Ball!')
        score = score + 1
        feeling_brave = False
        

    else:
        print('No ball. :( ')
        print('Better luck next time!')
        print('Game over! You scored', score)

       

