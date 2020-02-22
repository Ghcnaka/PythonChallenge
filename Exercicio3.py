# funcao base: verifica se ha exatamente 3 interrogacoes
def verify(string):
    count = 0
    for index in string:
        if index == "?":
            count += 1
        # otimizacao, se passou de 3 nao faz sentido continuar
        # porem, se desejado, pode-se contar ate o final
        # apagando assim este if
        if count > 3:
            break
    return count


# chama funcao base e retorna bool
def verify_interval(string):
    question = False
    if verify(string) == 3:
        question = True
    return question


# funcao que verifica o intervalo de string entre numeros
def question_mark(string):
    # valor em int do numero que precede a string a ser testada
    string_start = -1
    # analogamente, numero apos string. Foi escolhido o -1, pois '-' seria considerado como caractere no problema
    string_finish = -1
    count = 0
    # armazena posicao do numero inicial. Nao ha para o final, ja que podemos utilizar count
    first_index = 0
    boolean = True
    for index in string:
        # metodo para verificar se for inteiro ou nao
        # se nao for inteiro e o try falhar, itera novamente o "for"
        try:
            # caso nao haja, atribui (tenta) o char atual ao numero inicial ou final
            if string_start == -1:
                # lugar onde o try falha caso nao seja numero
                string_start = int(index)
                first_index = count
            elif string_finish == -1:
                string_finish = int(index)
            # se foram encontrados dois numeros, verifica se a soma >= 10
            if string_start + string_finish >= 10:
                # se condicao verdadeira, chama funcao principal, "cortando" a string de acordo com os indices
                boolean = verify_interval(string[first_index:count + 1])
                # sendo falso, quebra o loop, retornando falso a chamada principal
                if not boolean:
                    break
            # caso numeros sejam menor que 10, reseta o inicio da string, procurando por um novo numero
            if string_finish != -1:
                string_start = string_finish
                string_finish = -1
                first_index = count
        # captura os erros de atribuicao, mas ignora-os
        except ValueError or TypeError:
            True

        count += 1

    return boolean


if question_mark(input()):
    print("OK")
else:
    print("not OK")