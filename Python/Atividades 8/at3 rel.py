# Faça um Programa em Python que recebe uma matriz 2x3 e apresente quantos
# valores são pares. O programa deve exibir a posição do elemento e solicitar a
# digitação do número.

matriz = [[0,0,0],[0,0,0]]
par=0
for lin in range(len(matriz)):
    for col in range(len(matriz[lin])):
        matriz [lin] [col] = int(input("[%s][%s]: " %(lin,col)))
        if  (matriz [lin] [col] % 2) == 0:
            par=par+1
print('======================================================')
print("N* de elementos (pares) %s" %(par))
print('======================================================')
print('IMPRIMINDO A MATRIZ') #imprimindo a Matriz
for lin in range(len(matriz)):
    for col in range(len(matriz[lin])):
        print('|', end='\t')
        print(matriz [lin] [col], end='\t')
    print('|')
    print('---------------------------------------------------')