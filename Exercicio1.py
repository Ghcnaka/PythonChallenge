from random import *


def throw_dices():
    double = False
    a = randint(1,6)
    b = randint(1,6)
    if a == b:
        double = True
    return a+b, double


def player_move():
    double = True
    index = 0
    movement = 0
    while index < 3 and double:
        mov, double = throw_dices()
        movement += mov
        index += 1
        if not double:
            return movement, False, index
    return 0, True, index


def prison_escape(money):
    for index in range(0,3):
        movement, double = throw_dices()
        if double:
            return movement, False, money - 50
    return 0, True, money


def default_move(piece, prison_try, money):
    if not prison_try:
        play = player_move()
        prison_try = play[1]
    else:
        play = prison_escape(money)
        prison_try = play[1]
        money = play[2]
    return piece, prison_try, money, play[0]


print(default_move('Teste', False, 500))