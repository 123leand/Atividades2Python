# 1. Adicione os números de 1 a 10 à lista "minha_lista" utilizando um loop, em seguida imprima esses valores na tela e por fim
# mostre o tamanho dessa lista.

#  for i in range(1, 11):
#      minha_lista.append(i)

#  # Imprimindo os valores na tela
#  for numero in minha_lista:
#      print(numero)

#  # Mostrando o tamanho da lista
#  tamanho_lista = len(minha_lista)
#  print("Tamanho da lista:", tamanho_lista)

#  1
#  2
#  3
#  4
#  5
#  6
#  7
#  8
#  9
#  10
#  Tamanho da lista: 10



#  # 2. Crie uma lista com os números pares de 0 a 20
#   e em seguida atenda os seguintes comandos:
#  # a) Inverta a ordem dos elementos da lista.
#  # b) Inverta a ordem dos elementos da lista.
#  # c) Remova os números múltimos de 5 da lista.

# minha_lista = list(range(0, 21, 2))
# minha_lista.reverse()
# print("Listagem após a primeira inversão:", minha_lista)
# minha_lista = minha_lista[::-1]
# print("Listagem após a segunda inversão:", minha_lista)
# minha_lista = [numero for numero in minha_lista if numero % 5 != 0]
# print("Listagem após a remoção dos múltiplos de 5:", minha_lista)

#  3. Crie uma lista chamada "lista_concatenada" que seja a concatenação das listas criadas na questão 1 e na questão 2.

# lista_concatenada = minha_lista
# print("Lista concatenada:", lista_concatenada)

#  4. Remova todos os elementos da lista "lista_concatenada".
#  lista_concatenada.clear()
#  print("Lista após a remoção dos elementos:", lista_concatenada)

#  5. Crie uma lista chamada "lista_repetida" com 5 repetições da lista "lista_concatenada".
# lista_repetida = lista_concatenada * 5
# print("Lista repetida:", lista_repetida)

#  6. Copie a lista "lista_concatenada" para uma nova lista chamada "copia_lista_concatenada" sem utilizar o operador de atribuição direta.

# copia_lista_concatenada = list(lista_concatenada)
# print("Cópia da lista ():", copia_lista_concatenada)

# 7. Faça um programa que leia nome e idade de 5 pessoas e coloque os nomes em uma lista e as idades em outra. 
# Apresente as duas listas preenchidas.

# nomes = []
# idades = []

# for i in range(5):
#     nome = input("Digite o nome da pessoa: ")
#     idade = int(input("Digite a idade da pessoa: "))

#     nomes.append(nome)
#     idades.append(idade)

# print("Lista de nomes:", nomes)
# print("Lista de idades:", idades)

# 8.Faça um script que leia números do usuário, enquanto ele não digitar 0. 
# Armazene esses números em uma lista e ao final informe quantos números foram digitados, ignorando o 0, 
# o valor máximo e o valor mínimo.

# numeros = []
# numero = int(input("Digite um número (ou 0 para sair): "))

# while numero != 0:
#     numeros.append(numero)
#     numero = int(input("Digite um número (ou 0 para sair): "))

# if len(numeros) > 0:
#     quantidade_numeros = len(numeros)
#     valor_maximo = max(numeros)
#     valor_minimo = min(numeros)

#     print("Quantidade de números digitados (excluindo o 0):", quantidade_numeros)
#     print("Valor máximo:", valor_maximo)
#     print("Valor mínimo:", valor_minimo)
# else:
#     print("Nenhum número foi digitado.")




# 9.Faça um script que informe o fatorial de um número.
# Utilize obrigatoriamente o comando for

# numero = int(input("Digite um número inteiro: "))

# fatorial = 1
# for i in range(1, numero + 1):
#     fatorial *= i

# print("O fatorial de", numero, "é", fatorial)


# 10.Informe, de forma decrescente todos os pares entre N (número fornecido pelo usuário) e -N.
# Se N for par, ele também deve ser incluído no output (vide exemplo para N = 2)

# N = int(input("Digite um número inteiro: "))

# if N % 2 != 0:
#     N -= 1

# for item in range(N, -N - 1, -2 ):
#     print(item)


# 11. Faça um script que peça ao usuário para digitar um número n e some todos os números de 1 a n.

# n = int(input("Digite um número inteiro: "))

# soma = 0
# for i in range(1, n + 1):
#     soma += i

# print("A soma dos números de 1 a", n, "é", soma)


 # 12. Faça um programa que recebe um número inteiro do usuário e imprime na tela a quantidade 
 # de divisores desse número e quais são eles.


# numero = int(input("Digite um número inteiro: "))

# divisores = []
# for i in range(1, numero + 1):
#     if numero % i == 0:
#         divisores.append(i)

# quantidade_divisores = len(divisores)

# print("Quantidade de divisores:", quantidade_divisores)
# print("Divisores:", divisores)

# Exercicios 6 


# 1.Faça um programa que pede para o usuário digitar uma palavra e imprima cada letra em uma linha.

# palavra = input("Digite uma palavra: ")

# for letra in palavra:
#     print(letra)


# 2.Faça um programa que pede para o usuário digitar uma palavra e cria uma nova string igual, porém com espaço entre cada letra, depois imprima a nova string: Exemplo: se o usuário digitar "python" o programa deve imprimir "p y t h o n "

# palavra = input("Digite uma palavra: ")
# nova_string = ""

# for letra in palavra:
#     nova_string += letra + " "

# print("Nova string:", nova_string)


# 3.Faça um programa que receba uma string e retorne uma nova string substituindo: 'a' por '4' 'e' por '3' 'I' por '1' 't' por '7'

# def substituir_caracteres(string):
#     string = string.replace('a', '4')
#     string = string.replace('e', '3')
#     string = string.replace('I', '1')
#     string = string.replace('t', '7')
#     return string

# palavra = input("Digite uma palavra: ")
# nova_palavra = substituir_caracteres(palavra)
# print("Nova palavra:", nova_palavra)


# 4.Faça um programa que recebe uma string e retorna ela ao contrário. Exemplo: Recebe "teste" e retorna "etset".

# def inverter_string(string):
#     return string[::-1]

# palavra = input("Digite uma palavra: ")
# palavra_invertida = inverter_string(palavra)
# print("Palavra invertida:", palavra_invertida)


# 5. Escreva um programa que duas strings e gere uma terceira na qual os caracteres da segunda foram retirados da primeira.

# def remover_caracteres(string1, string2):
#     for caractere in string2:
#         string1 = string1.replace(caractere, '')
#     return string1

# primeira_string = input("Digite a primeira string: ")
# segunda_string = input("Digite a segunda string: ")

# nova_string = remover_caracteres(primeira_string, segunda_string)
# print("Nova string:", nova_string)


# 6. Escreva um programa que receba um texto e uma palavra, então verifique se a palavra está no texto..

def verificar_palavra(texto, palavra):
    palavras_texto = texto.split()
    for palavra_texto in palavras_texto:
        if palavra_texto == palavra:
            return True
    return False

texto = input("Digite um texto: ")
palavra = input("Digite uma palavra: ")

resultado = verificar_palavra(texto, palavra)

if resultado:
    print("A palavra está presente no texto.")
else:
    print("A palavra não está presente no texto.")





