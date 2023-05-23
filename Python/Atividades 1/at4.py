# Faça um programa em Python para encontrar o menor número
# num conjunto de 3 dados, fornecidos pelo usuário.
# • Apresentar qual foi o menor numero encontrado.

a = int(input("Informe um valor para A: "))
b = int(input("Informe um valor para B: "))
c = int(input("Informe um valor para C: "))
if (a < b and a < c):
    print("O menor número é %s" %(a))
elif (b < a and b < c):
    print("O menor número é %s" %(b))
elif (c < b and c < a):
    print("O menor número é %s" %(c))
else:
    print("Os números são iguais")