# Criar um programa em Python para criar a matriz apresentada contendo os dados
# apresentados na imagem abaixo, assim como, imprimir também os elementos que
# consta na posição [0] [0] e na posição [1] [0].

print("1-A================================================")
print("===================================================")
matriz =[['pedro', 22],['ana',15],['joão',12]]
print("O elemento que consta na linha 0 e colona 0 é:",matriz[0][0])
print("O elemento que consta na linha 1 e colona 0 é:",matriz[1][0])
print('================================')
print('IMPRIMINDO A MATRIZ') #imprimindo a Matriz
for lin in range(len(matriz)):
    for col in range(len(matriz[lin])):
        print('|', end='\t')
        print(matriz [lin] [col], end='\t')
    print('|')
    print('-------------------------------')


# No mesmo programa, incremente o código para executar ação de alterar a idade
# da Ana de 15 para 16 antes de exibir a matriz.

print("1-B================================================")
print("===================================================")
matriz[1][1] = 16
print('IMPRIMINDO A MATRIZ') #imprimindo a Matriz
for lin in range(len(matriz)):
    for col in range(len(matriz[lin])):
        print('|', end='\t')
        print(matriz [lin] [col], end='\t')
    print('|')
    print('-------------------------------')


# No mesmo programa, incremente o código para executar ação de inserir uma nova
# pessoa, conforme apresentado abaixo:

print("1-C================================================")
print("===================================================")
matriz[1][1] = 16
nova = ['Jean', 41]
matriz.insert(3,nova)
print('================================')
print('IMPRIMINDO A MATRIZ') #imprimindo a Matriz
for lin in range(len(matriz)):
    for col in range(len(matriz[lin])):
        print('|', end='\t')
        print(matriz [lin] [col], end='\t')
    print('|')
    print('-------------------------------')
    
    
# No mesmo programa, incremente o código para executar ação de remover a
# pessoa na posição [1] da matriz.

print("1-D================================================")
print("===================================================")
matriz[1][1] = 16
matriz.pop(1)
print('IMPRIMINDO A MATRIZ') #imprimindo a Matriz
for lin in range(len(matriz)):
    for col in range(len(matriz[lin])):
        print('|', end='\t')
        print(matriz [lin] [col], end='\t')
    print('|')
    print('-------------------------------')
  