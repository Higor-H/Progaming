# Construir um programa em Python para somar os números
# impares entre um intervalo informado pelo usuário e mostre o
# valor da soma.

s = 0
i1 = int(input("Informe um número inicial: "))
i2 = int(input("Informe um número final: "))
for i in range (i1,i2 +1):
    if i %2 != 0:
        s = s + i
print(s)
