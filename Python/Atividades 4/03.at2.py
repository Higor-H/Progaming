# Desenvolver um programa em Python para ler três números,
# mostre o índice. Ao final, mostre a somar dos valores
# informados.

i1 = int(input("Informe um número 1: "))
i2 = int(input("Informe um número 2: "))
i3 = int(input("Informe um número 3: "))
for i in (i1, i2, i3):
        s = (i1 + i2 + i3)
        print("O total da soma foi: %s" % (s))
        break