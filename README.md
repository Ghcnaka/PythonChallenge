# PythonChallenge
 Exercícios para o desafio em Python proposto

 		No exercício 1, utiliza-se de uma função básica, onde se joga 2 dados, que retorna sua soma e se são iguais.
 	Funções que tratam de cada caso (se o player está na prisão ou não) organizam as jogadas.
 	A função principal retorna os valores atualizados, com a adição do número de casas a serem percorridas.


 		No exercício 2, ao invés de se criar 2 listas (ou "linhas", como estava no problema), utiliza-se apenas uma.
 	Por uma delas ser uma lista de valores decrescentes ([10, 9, 8 ... 2] ou [9, 8 ... 2]), é utilizado o próprio loop como referência.
 	Por fim se compara os dígitos verificadores encontrados e os que foram passados.


 		No exercício 3, são criadas funções mais genéricas, onde, dado uma string, verificam se há exatamente 3 caracteres '?', retornando "True" caso verdade.
 	Por fim, a função que é chamada pelo usuário verifica a string completa, atribuindo posições de início e fim ao encontrar inteiros.
 	Ao encontrar pelo menos dois inteiros, verifica-se se são maiores ou iguais a 10. Se sim, utilizam das funções genéricas citadas.
 	A string é percorrida até as funções genéricas retornarem falso, ou seja, se a condição falha pelo menos uma vez.
 	Note que se as funções genéricas retornarem "True", o inteiro-referência final vira o inicial, e inicia-se uma nova busca por um inteiro de referência. 


# Utilizado para pequenas dúvidas pontuais de sintaxe
https://docs.python.org/3/

# Utilizado no exercício 2
https://stackoverflow.com/questions/39945615/converting-input-string-of-integers-to-list-then-to-ints-in-python


Feito por Gustavo Nakagawa