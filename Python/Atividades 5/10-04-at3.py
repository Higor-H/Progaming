# Faça um programa em Python, onde o usuário deve informar um número e o programa
# deve calcular a soma de todos os números de 1 até ao número digitado.
# Por exemplo, se o usuário digitou o número 4, a saída deve ser 10 (1+2+3+4=10).
# Implementar a solução utilizando a estrutura de repetição FOR.

n = int(input("Por favor, insira um numero: "))
x=0
for i in range (1,n+1):
    x= x +i
print(x)
