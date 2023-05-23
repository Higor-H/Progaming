# Faça um programa em Python que obtenha como entrada a quantidade de km
# percorridos por um carro e a quantidade de dias pelos quais o carro foi alugado. Calcule e mostre o valor
# total gasto com diárias, o valor total gasto com km rodado e o valor total a pagar (total de diárias + total
# gasto pela quilometragem rodada), sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km
# percorrido.

dias = float(input("Quantos dias o carro ficou alugado: "))
km = float(input("Quantos Km foram rodados: "))
print("-------------------------------------")
pdias = dias * 60
pkm = km * 0.15
vt = pdias + pkm
print("Valor gasto com diária do carro: %s" %(pdias))
print("Valor gasto com Km rodado: %s" %(pkm))
print("Valor total a pagar: %s" %(vt))
