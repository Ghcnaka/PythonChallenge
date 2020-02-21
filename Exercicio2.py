def transform_list(cpf):
    try:
        cpf_in_list = [int(i) for i in cpf]
        return cpf_in_list
    except ValueError:
        print("Por favor, insira apenas números, sem espaçamento ou pontuações")
        return []


def num_verif(cpf_in_list, times):
    final_num = 0
    times = times + 1
    for index in range(0, times - 1):
        num = cpf_in_list[index]
        final_num = (num * (times - index)) + final_num
    final_num = 11 - final_num % 11
    if final_num > 9:
        final_num = 0
    verif_number = final_num
    return verif_number


def valida(cpf_in_list):
    copia = cpf_in_list[:-2]
    verif_num_1 = num_verif(copia, 9)
    copia.append(verif_num_1)
    verif_num_2 = num_verif(copia, 10)
    if verif_num_1 == cpf_in_list[-2] and verif_num_2 == cpf_in_list[-1]:
        print("CPF VALIDO")
        return True
    print("CPF INVALIDO")
    return False


while True:
    cpf = input("CPF: ")
    cpf_in_list = transform_list(cpf)
    if cpf_in_list != []:
        if len(cpf_in_list) == 11:
            break
        print("Favor inserir 11 números")

valida(cpf_in_list)