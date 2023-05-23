# • Elabore um programa em Python que receba um numero inteiro
# e verifique se esse numero é par ou impar.
# • Para verificar se o número é par, utilizar a fórmula: ( num % 2 == 0).

num = int(input("Informe um número: "))
if (num %2 == 0):
    print("O número é par")
else:
    print("O número é impar")