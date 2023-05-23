# Com base no diagrama de blocos e algoritmo em português (Portugol), desenvolver um
# programa em Python, que:
# • receba um valor válido (entre 0 e 10),
# • se o valor informado for inválido o algoritmo deve exibir uma mensagem que o valor
# informado foi inválido e solicitar a inserção de um novo valor até que o usuário informe
# um valor válido, e
# • ao final o algoritmo deve mostrar o valor informado.

valor = int(input("Digite um valor entre 0 e 10: "))
while (valor < 0 or valor > 10):
    print("Erro! O valor informado é inválido.")
    valor = int(input("Digite um valor entre 0 e 10: "))

print("PARABÉNS! O valor válido informado foi: ", valor)