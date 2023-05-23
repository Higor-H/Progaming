#Faça um programa em Python que:
#Leia 4 valores inteiros A, B, C, D. A seguir, se B for maior do que C e se D for maior do que A,
#e a soma de C com D for maior que a soma de A e B e se C e D, amos, forem positivos e se a variável A for par,
# escreva a mensagem “Valores Aceitos”, senão escreva “Valores nao aceitos”.

A = int(input("Informe o valor de A: "))
B = int(input("Informe o valor de B: "))
C = int(input("Informe o valor de C: "))
D = int(input("Informe o valor de D: "))
if (B > C):
    if (D > A) and ((C + D) > (A + B)):
        if (C and D) > 0:
            if (A % 2) == 0:
                print("Valores aceitos") 
else:
    print("Valores não aceitos")