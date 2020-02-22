from random import *


# jogada simples de dados, que retorna a soma, e se sao iguais
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


# jogada padrao
def player_move():
    print("Jogue os dados")
    double = True
    index = 0
    movement = 0
    # verifica se 3 duplas foram encontradas, repete jogada enquanto forem duplas
    while index < 3 and double:
        mov, double = throw_dices()
        movement += mov
        index += 1
        # quebra de funcao ao nao serem duplas, ou seja, jogada legal
        if not double:
            print(f"Jogada concluida! Por favor mova {movement} casas")
            return movement, False, index
        print("Uma dupla! Com isso, você tem direito a mais uma jogada de dados")
    # chegando aqui, while acaba por conta de index e nao double, ou seja, foram 3 duplas, jogada ilegal
    print("Uh oh... Você tirou tres duplas! Va para a prisao!!")
    return 0, True, index


# jogada para escapar da prisao caso parametro prision_try seja true
def prison_escape(money):
    print("Você esta na prisão. Para sair, consiga uma dupla nos dados. Você tem 3 tentativas.")
    # 3 tentativas para escapar
    for index in range(0,3):
        print(f"Tentativa N° {index+1}:")
        movement, double = throw_dices()
        # condicao de escape encontrada, retornando movimento dos ultimos dados e diminuindo dinheiro em 50
        if double:
            print(f"Parabens, uma dupla!! Saia da prisao e ande {movement} casas! Mas antes, pague 50")
            return movement, False, money - 50
    print("Nenhuma dupla... Tente novamente na proxima rodada")
    return 0, True, money


# decide se esta na prisao ou nao, e resolve os casos
def default_move(piece, prison_try, money):
    print(f"Vez de {piece}")
    if not prison_try:
        play = player_move()
        prison_try = play[1]
    else:
        play = prison_escape(money)
        prison_try = play[1]
        money = play[2]
    # retorna os valores atualizados, com um dado adicional de casas a se movimentar (armazenado na pos 0 de play[])
    return piece, prison_try, money, play[0]


print(default_move("Teste Prisioneiro", True, 500))
print(default_move("Teste Standard", False, 500))