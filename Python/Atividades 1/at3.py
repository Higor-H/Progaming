# Construa um programa em Python que leia 2 números inteiros.
# • Imprimir uma mensagem informando qual dos dois é o maior ou se são iguais.

a = int(input("Informe um valor para A: "))
b = int(input("Informe um valor para B: "))
if (a > b):
    print("O número %s é MAIOR que %s" %(a,b))
elif (b > a):
    print("O número %s é MAIOR que %s" %(b,a))
else:
    print("Os números são iguais")
