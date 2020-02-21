from random import *


def throw_dices():
    double = False
    a = randint(1,6)
    print(f"Dado N° 1: {a}")
    b = randint(1,6)
    print(f"Dado N° 2: {b}")
    if a == b:
        print("Dois dados iguais!")
        double = True
    return a+b, double


def player_move():
    print("Jogue os dados")
    double = True
    index = 0
    movement = 0
    while index < 3 and double:
        mov, double = throw_dices()
        movement += mov
        index += 1
        if not double:
            print(f"Jogada concluída! Por favor mova {movement} casas")
            return movement, False, index
        print("Uma dupla! Com isso, você tem direito a mais uma jogada de dados")
    print("Uh oh... Você tirou três duplas! Vá para a prisão!!")
    return 0, True, index


def prison_escape(money):
    print("Você está na prisão. Para sair, consiga uma dupla nos dados. Você tem 3 tentativas.")
    for index in range(0,3):
        print(f"Tentativa N° {index+1}:")
        movement, double = throw_dices()
        if double:
            print(f"Parabéns, uma dupla!! Saia da prisão e ande {movement} casas! Mas antes, pague 50")
            return movement, False, money - 50
    print("Nenhuma dupla... Tente novamente na próxima rodada")
    return 0, True, money


def default_move(piece, prison_try, money):
    print(f"É a vez de {piece}")
    if not prison_try:
        play = player_move()
        prison_try = play[1]
    else:
        play = prison_escape(money)
        prison_try = play[1]
        money = play[2]
    return piece, prison_try, money, play[0]


print(default_move("Teste Prisioneiro", True, 500))
print(default_move("Teste Standard", False, 500))