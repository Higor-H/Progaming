# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# • Álcool:
# • até 20 litros, desconto de 3% por litro
# • acima de 20 litros, desconto de 5% por litro
# • Gasolina
# • até 20 litros, desconto de 4% por litro
# • acima de 20 litros, desconto de 6% por litro
# Faça um programa em Python que leia o número de litros vendidos e o tipo de combustível
# (codificado da seguinte forma: A-álcool, G-gasolina), se informar outra letra, apresente a
# mensagem “Combustível informado não localizado”, calcule e imprima o valor a ser pago
# pelo cliente sabendo-se que o preço do litro da gasolina é R$ 3,30 e o preço do litro do
# álcool é R$ 2,90.

t = str(input("Digite o tipo de combustivel [A-Álcool ou G-Gasolina]: "))
q = int(input("Informe a quantidade: "))
if (t == 'A'):
    print("Você abasteceu %s litros do combustivel %s" % (q, t))
    print("-------------------------------------------------------")
    if (q <= 20):
        vb = round((q * 2.90),2)
        print("Valor total bruto foi: R$%s" % (vb))
        va = ( 2.90 * 0.03)
        vl = round(( (2.90 - va) * q ),2)
        print("Valor TOTAL liquido foi: R$%s" % (vl))
    elif (q > 20):
        vb = round((q * 2.90),2)
        print("Valor total bruto foi: R$%s" % (vb))
        va = ( 2.90 * 0.05)
        vl = round(( (2.90 - va) * q ),2)
        print("Valor TOTAL liquido foi: R$%s" % (vl))
if (t== 'G'):
    print("Você abasteceu %s litros do combustivel %s" % (q, t))
    print("-------------------------------------------------------")
    if (q <= 20):
        vb = round((q * 3.30),2)
        print("Valor total bruto foi: R$%s" % (vb))
        va = ( 3.30 * 0.04)
        vl = round(( (2.90 - va) * q ),2)
        print("Valor TOTAL liquido foi: R$%s" % (vl))
    elif (q > 20):
        vb = round((q * 3.30),2)
        print("Valor total bruto foi: R$%s" % (vb))
        va = ( 3.30 * 0.06)
        vl = round(( (3.30 - va) * q ),2)
        print("Valor TOTAL liquido foi: R$%s" % (vl))
else:
    print("Combustível informado não localizado")