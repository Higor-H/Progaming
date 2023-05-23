# Desenvolver um programa em Python que solicite qual tabuada
# o usuário gostaria que o programa imprima na tela.

dit = int(input("Qual tabuada deseja imprimir: "))
for i in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
    tab = dit * i
    print ("%s X %s = %s" % (dit, i, tab))