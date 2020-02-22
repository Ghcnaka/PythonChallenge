def transform_list(cpf):
    # verifica se o que foi inserido foram apenas numeros
    try:
        # transforma os numeros em lista de numeros
        cpf_in_list = [int(i) for i in cpf]
        return cpf_in_list
    except ValueError:
        print("Por favor, insira apenas números, sem espaçamento ou pontuações")
        return []

# funcao generica onde pode-se utilizar nas duas iteracoes
def num_verif(cpf_in_list, times):
    verif_number = 0
    # como a linha que multiplica os numeros do cpf sao decrescentes, podemos utilizar isto como-
    # -uma forma de evitar utilizar loops desnecessarios, manipulando o "for"
    # ou seja, o proprio index do "for" multiplica os numeros do cpf, combinado com "times"
    for index in range(0, times):
        num = cpf_in_list[index]
        # multiplicacao entre as duas "linhas"
        verif_number = (num * (1 + times - index)) + verif_number
    # resultado do resto da divisao por 11, subtraido de 11
    verif_number = 11 - verif_number % 11
    if verif_number > 9:
        verif_number = 0
    return verif_number

# funcao onde se faz a verificacao de 2 passos do cpf
def valida(cpf_in_list):
    # copia-se numeros passados, excluindo digitos verificadores
    copia = cpf_in_list[:-2]
    # obtem o primeiro digito verificador, e adiciona ao final da lista
    verif_num_1 = num_verif(copia, 9)
    copia.append(verif_num_1)
    # faz novamente, com a adicao do primeiro digito verificador, para se obter o segundo
    verif_num_2 = num_verif(copia, 10)
    # compara os digitos verificadores obtidos e os que foram passados
    if verif_num_1 == cpf_in_list[-2] and verif_num_2 == cpf_in_list[-1]:
        print("CPF VALIDO")
        return True
    print("CPF INVALIDO")
    return False

# repete loop ate que valores corretos sejam inseridos
while True:
    cpf = input("CPF: ")
    cpf_in_list = transform_list(cpf)
    if cpf_in_list != []:
        if len(cpf_in_list) == 11:
            break
        print("Favor inserir 11 números")

valida(cpf_in_list)