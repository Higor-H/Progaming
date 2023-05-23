# Elabore um programa em Python que leia um número.
# • Se o numero (incluindo o zero) for positivo apresente a
# mensagem “O numero é POSITIVO”, senão, apresente a
# mensagem “O numero é NEGATIVO”. 

num = float(input("Informe um número: "))
if (num >= 0):
    print("O número é POSITIVO")
else:
    print("O número é NEGATIVO")