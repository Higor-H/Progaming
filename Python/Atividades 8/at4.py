# Faça um Programa em Python que
# recebe duas matrizes A e B 2x2 de
# valores inteiros e imprima a matriz C
# que é a soma das matrizes A e B.

matriza = [[0,0],[0,0]]
matrizb = [[0,0],[0,0]]
matrizc = [[0,0],[0,0]]

print("PREENCHENDO A MATRIZ A----------------")
for lin in range(len(matriza)):
    for col in range(len(matriza[lin])):
        matriza [lin] [col] = int(input("Digite um número na posição [%s][%s]: " %(lin,col)))
        
print("PREENCHENDO A MATRIZ B----------------")
for lin in range(len(matrizb)):
    for col in range(len(matrizb[lin])):
        matrizb [lin] [col] = int(input("Digite um número na posição [%s][%s]: " %(lin,col)))
        

print('=================================')
print('IMPRIMINDO A MATRIZ A') #imprimindo a Matriz
for lin in range(len(matriza)):
    for col in range(len(matriza[lin])):
        print('|', end='\t')
        print(matriza [lin] [col], end='\t')
    print('|')
    print('-------------------------------')
    
print('=================================')
print('IMPRIMINDO A MATRIZ B') #imprimindo a Matriz
for lin in range(len(matrizb)):
    for col in range(len(matrizb[lin])):
        print('|', end='\t')
        print(matrizb [lin] [col], end='\t')
    print('|')
    print('-------------------------------')
    
for lin in range(len(matrizc)):
    for col in range(len(matrizc[lin])):
         matrizc [lin] [col] = matriza [lin] [col] + matrizb[lin] [col]
         
print('=================================')
print('IMPRIMINDO A MATRIZ C') #imprimindo a Matriz
for lin in range(len(matrizc)):
    for col in range(len(matrizc[lin])):
        print('|', end='\t')
        print(matrizc [lin] [col], end='\t')
    print('|')
    print('-------------------------------')
    