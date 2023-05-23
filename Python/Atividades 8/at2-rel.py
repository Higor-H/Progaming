# Faça um Programa em Python que:
# • Cria uma matriz contendo 2 linhas e 3 colunas, para armazenar em cada
# elemento um numero inteiro.
# • O programa deve exibir a posição do elemento e solicitar a digitação do número.
# • Ao final o programa deve imprimir a matriz.

matriz = [[0,0,0],[0,0,0]]

print("PREENENCHENDO A MATRIZ-----------------------------------")
for lin in range(len(matriz)):
    for col in range(len(matriz[lin])):
        matriz [lin] [col] = int(input("Digite um numero para a posição [%s][%s]" %(lin,col)))
        
print('======================================================')
print('IMPRIMINDO A MATRIZ') #imprimindo a Matriz
for lin in range(len(matriz)):
    for col in range(len(matriz[lin])):
        print('|', end='\t')
        print(matriz [lin] [col], end='\t')
    print('|')
    print('---------------------------------------------------')