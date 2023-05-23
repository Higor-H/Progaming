# Criar um programa em Python que leia o comprimento e a largura de um terreno regular,
# calcule e imprima a área (area = comprimento * largura) do mesmo.
# Ao final de cada exibição, o programa deve perguntar se o usuário deseja fazer um novo
# cálculo, sendo, [s] para fazer um novo cálculo ou [n] para encerrar a execução.

op = "s"
while (op == "s"):
    l = float(input("Informe o valor da largura: "))
    c = float(input("Informe o valor da comprimento: "))
    a = c * l
    print("A área do retangulo é: %s" % (a))
    print("----------------------------------------------------")
    op = str(input("Informe [s] para fazer um novo cálculo ou [n] para sair: "))